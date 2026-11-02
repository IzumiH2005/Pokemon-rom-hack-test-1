// Tempête Sakura : animation de capacité originale (test VFX).
// Chaque pétale vole du lanceur vers la cible en arc, tourne autour d'elle
// (devant puis derrière, comme en 3D), puis s'envole vers l'extérieur.
#include "global.h"
#include "battle_anim.h"
#include "sprite.h"
#include "trig.h"
#include "graphics.h"

static void AnimSakuraPetal(struct Sprite *sprite);
static void AnimSakuraPetal_Step(struct Sprite *sprite);

static const union AnimCmd sAnim_SakuraFlutter[] =
{
    ANIMCMD_FRAME(0, 5),
    ANIMCMD_FRAME(4, 4),
    ANIMCMD_FRAME(8, 3),
    ANIMCMD_FRAME(12, 4),
    ANIMCMD_FRAME(8, 3),
    ANIMCMD_FRAME(4, 4),
    ANIMCMD_JUMP(0),
};

static const union AnimCmd *const sAnims_SakuraPetal[] =
{
    sAnim_SakuraFlutter,
};

// args : angle de départ (0-255), rayon d'orbite, hauteur de l'arc, durée d'orbite
const struct SpriteTemplate gSakuraPetalSpriteTemplate =
{
    .tileTag = ANIM_TAG_SAKURA,
    .paletteTag = ANIM_TAG_SAKURA,
    .oam = &gOamData_AffineOff_ObjNormal_16x16,
    .anims = sAnims_SakuraPetal,
    .images = NULL,
    .affineAnims = gDummySpriteAffineAnimTable,
    .callback = AnimSakuraPetal,
};

#define FLY_TIME   22
#define BURST_TIME 18

#define sState  data[0]
#define sTimer  data[1]
#define sStartX data[2]
#define sStartY data[3]
#define sAngle  data[4]
#define sRadius data[5]
#define sArc    data[6]
#define sOrbit  data[7]

static void AnimSakuraPetal(struct Sprite *sprite)
{
    sprite->sStartX = GetBattlerSpriteCoord(gBattleAnimAttacker, BATTLER_COORD_X_2);
    sprite->sStartY = GetBattlerSpriteCoord(gBattleAnimAttacker, BATTLER_COORD_Y_PIC_OFFSET);
    sprite->x = GetBattlerSpriteCoord(gBattleAnimTarget, BATTLER_COORD_X_2);
    sprite->y = GetBattlerSpriteCoord(gBattleAnimTarget, BATTLER_COORD_Y_PIC_OFFSET);
    sprite->sAngle = gBattleAnimArgs[0];
    sprite->sRadius = gBattleAnimArgs[1];
    sprite->sArc = gBattleAnimArgs[2];
    sprite->sOrbit = gBattleAnimArgs[3];
    sprite->sState = 0;
    sprite->sTimer = 0;
    // orientation variée selon l'angle : sinon tous les pétales pointent pareil
    sprite->hFlip = (gBattleAnimArgs[0] >> 6) & 1;
    sprite->vFlip = (gBattleAnimArgs[0] >> 7) & 1;
    StartSpriteAnim(sprite, 0);
    sprite->animDelayCounter = gBattleAnimArgs[0] & 3; // décale le battement entre pétales
    sprite->callback = AnimSakuraPetal_Step;
    AnimSakuraPetal_Step(sprite);
}

static void AnimSakuraPetal_Step(struct Sprite *sprite)
{
    s16 ox, oy, t;
    u8 targetSub = GetBattlerSpriteSubpriority(gBattleAnimTarget);

    switch (sprite->sState)
    {
    case 0: // vol en arc vers le point d'entrée de l'orbite
        t = sprite->sTimer;
        ox = Cos(sprite->sAngle, sprite->sRadius);
        oy = Sin(sprite->sAngle, sprite->sRadius / 3);
        // position absolue = départ + (arrivée - départ) * t / FLY_TIME, exprimée en décalage par rapport à la cible
        sprite->x2 = (sprite->sStartX - sprite->x) * (FLY_TIME - t) / FLY_TIME + ox * t / FLY_TIME;
        sprite->y2 = (sprite->sStartY - sprite->y) * (FLY_TIME - t) / FLY_TIME + oy * t / FLY_TIME
                   - Sin(t * 128 / FLY_TIME, sprite->sArc)
                   + Sin((t * 24 + sprite->sAngle) & 0xFF, 3);
        sprite->subpriority = targetSub - 1;
        if (++sprite->sTimer > FLY_TIME)
        {
            sprite->sTimer = 0;
            sprite->sState++;
        }
        break;
    case 1: // orbite autour de la cible, le rayon se resserre
        sprite->sAngle = (sprite->sAngle + 7) & 0xFF;
        t = sprite->sRadius - (sprite->sTimer * sprite->sRadius) / (sprite->sOrbit * 2);
        sprite->x2 = Cos(sprite->sAngle, t);
        sprite->y2 = Sin(sprite->sAngle, t / 3) + Sin((sprite->sTimer * 16) & 0xFF, 2);
        // devant la cible sur la moitié basse de l'ellipse, derrière sur la moitié haute
        sprite->subpriority = (sprite->sAngle < 128) ? targetSub - 1 : targetSub + 1;
        if (++sprite->sTimer >= sprite->sOrbit)
        {
            sprite->sTimer = 0;
            sprite->sStartX = sprite->x2; // on réutilise ces cases pour le point d'éclatement
            sprite->sStartY = sprite->y2;
            sprite->sState++;
        }
        break;
    case 2: // éclatement vers l'extérieur, en accélérant
        t = sprite->sTimer;
        sprite->x2 = sprite->sStartX + Cos(sprite->sAngle, t * t / 4 + t);
        sprite->y2 = sprite->sStartY + Sin(sprite->sAngle, t * t / 6 + t) - t / 2;
        sprite->subpriority = targetSub - 1;
        if (++sprite->sTimer > BURST_TIME)
            DestroyAnimSprite(sprite);
        break;
    }
}
