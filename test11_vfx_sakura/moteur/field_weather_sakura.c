// Météo « Sakura » (test VFX) : des pétales de cerisier tombent en diagonale
// sur toute la carte en se balançant et en tournoyant.
#include "global.h"
#include "field_weather.h"
#include "random.h"
#include "sprite.h"
#include "trig.h"
#include "constants/weather.h"

#define NUM_SAKURA_PETALS 14
#define PALTAG_SAKURA (TAG_WEATHER_START + 8)

static const u32 sSakuraTiles[] = INCGFX_U32("graphics/weather/sakura.png", ".4bpp");
static const u16 sSakuraPal[] = INCGFX_U16("graphics/weather/sakura.png", ".gbapal");

static EWRAM_DATA struct Sprite *sPetals[NUM_SAKURA_PETALS] = {0};
static EWRAM_DATA u8 sPetalCount = 0;
static EWRAM_DATA u8 sTargetCount = 0;
static EWRAM_DATA u8 sSpawnTimer = 0;

static void UpdateSakuraPetal(struct Sprite *sprite);

static const struct OamData sSakuraOam =
{
    .affineMode = ST_OAM_AFFINE_OFF,
    .objMode = ST_OAM_OBJ_NORMAL,
    .bpp = ST_OAM_4BPP,
    .shape = SPRITE_SHAPE(16x16),
    .size = SPRITE_SIZE(16x16),
    .priority = 1, // au-dessus des personnages
};

static const struct SpriteFrameImage sSakuraImages[] =
{
    {sSakuraTiles + 0 * 32, 128},
    {sSakuraTiles + 1 * 32, 128},
    {sSakuraTiles + 2 * 32, 128},
    {sSakuraTiles + 3 * 32, 128},
};

// pétale qui tourne sur lui-même : face, profil, tranche, dos, profil...
static const union AnimCmd sAnim_Flutter[] =
{
    ANIMCMD_FRAME(0, 8),
    ANIMCMD_FRAME(1, 6),
    ANIMCMD_FRAME(2, 4),
    ANIMCMD_FRAME(3, 6),
    ANIMCMD_FRAME(2, 4),
    ANIMCMD_FRAME(1, 6),
    ANIMCMD_JUMP(0),
};
static const union AnimCmd *const sAnims_Sakura[] = { sAnim_Flutter };

static const struct SpriteTemplate sSakuraTemplate =
{
    .tileTag = TAG_NONE,
    .paletteTag = PALTAG_SAKURA,
    .oam = &sSakuraOam,
    .anims = sAnims_Sakura,
    .images = sSakuraImages,
    .affineAnims = gDummySpriteAffineAnimTable,
    .callback = UpdateSakuraPetal,
};

static const struct SpritePalette sSakuraSpritePal = {sSakuraPal, PALTAG_SAKURA};

#define sPosX   data[0] // position écran en 1/16 de pixel
#define sPosY   data[1]
#define sVelX   data[2]
#define sVelY   data[3]
#define sWave   data[4]
#define sWaveSp data[5]
#define sAmp    data[6]

// Les positions sont stockées dans le repère de la carte (comme la neige) :
// les pétales défilent avec le décor quand le joueur marche.
// écran = position + gSpriteCoordOffset
static void ResetPetal(struct Sprite *sprite, bool8 anywhere)
{
    u16 r = Random();
    s16 sx = anywhere ? (Random() % 280) : 40 + (Random() % 260);
    s16 sy = anywhere ? (Random() % 170) - 8 : -16;
    sprite->sPosX = (sx - gSpriteCoordOffsetX) * 16;
    sprite->sPosY = (sy - gSpriteCoordOffsetY) * 16;
    sprite->sVelX = -(6 + (r & 7));          // vent vers la gauche
    sprite->sVelY = 10 + ((r >> 3) & 7);      // chute lente
    sprite->sWave = r & 0xFF;
    sprite->sWaveSp = 2 + ((r >> 6) & 3);
    sprite->sAmp = 6 + ((r >> 8) & 7);
    sprite->hFlip = (r >> 11) & 1;
    StartSpriteAnim(sprite, 0);
    sprite->animCmdIndex = (r >> 12) % 6;   // chaque pétale démarre à un angle différent
}

static void UpdateSakuraPetal(struct Sprite *sprite)
{
    s16 x, y, sx, sy;

    sprite->sPosX += sprite->sVelX;
    sprite->sPosY += sprite->sVelY;
    sprite->sWave = (sprite->sWave + sprite->sWaveSp) & 0xFF;

    // balancement latéral + petite remontée à chaque oscillation
    x = (sprite->sPosX >> 4) + Sin(sprite->sWave, sprite->sAmp);
    y = (sprite->sPosY >> 4) + Cos((sprite->sWave * 2) & 0xFF, 2);
    sx = x + gSpriteCoordOffsetX;
    sy = y + gSpriteCoordOffsetY;

    if (sy > 176)                       // sorti par le bas : retombe d'en haut
    {
        ResetPetal(sprite, FALSE);
        return;
    }
    if (sy < -24)                       // le joueur descend : réapparaît en bas
        sprite->sPosY += 196 * 16;
    if (sx < -16)                       // sortie gauche -> entre à droite
        sprite->sPosX += 272 * 16;
    else if (sx > 256)                  // sortie droite -> entre à gauche
        sprite->sPosX -= 272 * 16;

    sprite->x = x;
    sprite->y = y;
}

static void CreatePetal(bool8 anywhere)
{
    u8 spriteId;
    if (sPetalCount >= NUM_SAKURA_PETALS)
        return;
    spriteId = CreateSpriteAtEnd(&sSakuraTemplate, 0, 0, 78);
    if (spriteId == MAX_SPRITES)
        return;
    gSprites[spriteId].coordOffsetEnabled = TRUE;
    ResetPetal(&gSprites[spriteId], anywhere);
    UpdateSakuraPetal(&gSprites[spriteId]);
    sPetals[sPetalCount++] = &gSprites[spriteId];
}

void Sakura_InitVars(void)
{
    gWeatherPtr->initStep = 0;
    gWeatherPtr->weatherGfxLoaded = FALSE;
    gWeatherPtr->targetColorMapIndex = 0;
    gWeatherPtr->colorMapStepDelay = 20;
    gWeatherPtr->noShadows = FALSE;
    sTargetCount = NUM_SAKURA_PETALS;
    sSpawnTimer = 0;
}

void Sakura_InitAll(void)
{
    // en entrant sur la carte : les pétales sont déjà répartis à l'écran
    Sakura_InitVars();
    LoadSpritePalette(&sSakuraSpritePal);
    sPetalCount = 0;
    while (sPetalCount < sTargetCount)
    {
        u8 before = sPetalCount;
        CreatePetal(TRUE);
        if (sPetalCount == before)
            break;
    }
    gWeatherPtr->weatherGfxLoaded = TRUE;
    gWeatherPtr->initStep = 1;
}

void Sakura_Main(void)
{
    // changement de météo en cours de route : les pétales arrivent un par un
    if (gWeatherPtr->initStep == 0)
    {
        LoadSpritePalette(&sSakuraSpritePal);
        sPetalCount = 0;
        gWeatherPtr->initStep++;
    }
    if (sPetalCount < sTargetCount && ++sSpawnTimer > 12)
    {
        sSpawnTimer = 0;
        CreatePetal(FALSE);
    }
    if (sPetalCount >= sTargetCount)
        gWeatherPtr->weatherGfxLoaded = TRUE;
}

bool8 Sakura_Finish(void)
{
    if (sPetalCount > 0)
    {
        DestroySprite(sPetals[--sPetalCount]);
        return TRUE;
    }
    FreeSpritePaletteByTag(PALTAG_SAKURA);
    return FALSE;
}
