# Installe le sprite de combat d'Aventurine + le dresseur + le combat dans pokeemerald-expansion.
# Usage : python3 install_combat.py /chemin/vers/pokeemerald-expansion
import sys, os, shutil, re
R = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
def edit(p, old, new, once=True):
    fp = os.path.join(R, p); s = open(fp).read()
    if new in s: return
    assert old in s, (p, old)
    open(fp, 'w').write(s.replace(old, new, 1))

shutil.copy(os.path.join(HERE, 'aventurine_combat.png'), os.path.join(R, 'graphics/trainers/front_pics/aventurine.png'))
shutil.copy(os.path.join(HERE, 'aventurine_combat.pal'), os.path.join(R, 'graphics/trainers/palettes/aventurine.pal'))

# 1) nouvelle image de dresseur
edit('include/constants/trainers.h', '    TRAINER_PIC_COUNT,', '    TRAINER_PIC_AVENTURINE,\n    TRAINER_PIC_COUNT,')
edit('src/data/graphics/trainers.h',
     'const u16 gTrainerPalette_PainterFrlg[] = INCGFX_U16("graphics/trainers/palettes/painter_frlg.pal", ".gbapal");',
     'const u16 gTrainerPalette_PainterFrlg[] = INCGFX_U16("graphics/trainers/palettes/painter_frlg.pal", ".gbapal");\n'
     'const u32 gTrainerFrontPic_Aventurine[] = INCGFX_U32("graphics/trainers/front_pics/aventurine.png", ".4bpp.smol");\n'
     'const u16 gTrainerPalette_Aventurine[] = INCGFX_U16("graphics/trainers/palettes/aventurine.pal", ".gbapal");')
edit('src/data/graphics/trainers.h',
     '        .frontPic = TRAINER_FRONT_PIC(gTrainerFrontPic_PainterFrlg, gTrainerPalette_PainterFrlg),\n    },\n};',
     '        .frontPic = TRAINER_FRONT_PIC(gTrainerFrontPic_PainterFrlg, gTrainerPalette_PainterFrlg),\n    },\n'
     '    [TRAINER_PIC_AVENTURINE] =\n    {\n        .frontPic = TRAINER_FRONT_PIC(gTrainerFrontPic_Aventurine, gTrainerPalette_Aventurine),\n    },\n};')

# 2) nouveau dresseur
edit('include/constants/opponents.h', '#define TRAINER_MAY_PLACEHOLDER             854\n',
     '#define TRAINER_MAY_PLACEHOLDER             854\n#define TRAINER_AVENTURINE                  855\n')
edit('include/constants/opponents.h', '#define TRAINERS_COUNT_EMERALD     855', '#define TRAINERS_COUNT_EMERALD     856')
fp = os.path.join(R, 'src/data/trainers.party'); s = open(fp).read()
if 'TRAINER_AVENTURINE' not in s:
    s = s.rstrip('\n') + '''

=== TRAINER_AVENTURINE ===
Name: AVENTURINE
Class: Gentleman
Pic: Aventurine
Gender: Male
Music: Male
Double Battle: No

Sableye
Level: 6
IVs: 0 HP / 0 Atk / 0 Def / 0 SpA / 0 SpD / 0 Spe

Gholdengo
Level: 7
IVs: 0 HP / 0 Atk / 0 Def / 0 SpA / 0 SpD / 0 Spe
'''
    open(fp, 'w').write(s)

# 3) le PNJ donne un Pokemon si l'equipe est vide, puis lance le combat
edit('data/maps/LittlerootTown/scripts.inc',
     'LittlerootTown_EventScript_Aventurine::\n\tmsgbox LittlerootTown_Text_Aventurine, MSGBOX_NPC\n\tend\n',
     '''LittlerootTown_EventScript_Aventurine::
\tlock
\tfaceplayer
\tgetpartysize
\tgoto_if_ne VAR_RESULT, 0, LittlerootTown_EventScript_AventurineDuel
\tmsgbox LittlerootTown_Text_Aventurine, MSGBOX_DEFAULT
\tgivemon SPECIES_TORCHIC, 10
\tmsgbox LittlerootTown_Text_AventurineGift, MSGBOX_DEFAULT
LittlerootTown_EventScript_AventurineDuel::
\ttrainerbattle_single TRAINER_AVENTURINE, LittlerootTown_Text_AventurineIntro, LittlerootTown_Text_AventurineDefeat
\tmsgbox LittlerootTown_Text_AventurineAfter, MSGBOX_DEFAULT
\trelease
\tend

LittlerootTown_Text_AventurineGift:
\t.string "Tu n'as même pas de POKéMON?\\n"
\t.string "Tiens, prends celui-ci… c'est ma mise.$"

LittlerootTown_Text_AventurineIntro:
\t.string "Allez, lançons les dés!\\n"
\t.string "Tapis!$"

LittlerootTown_Text_AventurineDefeat:
\t.string "Ha! La chance a tourné…\\n"
\t.string "Cette fois.$"

LittlerootTown_Text_AventurineAfter:
\t.string "Le jeu n'est jamais fini,\\n"
\t.string "seulement mis en pause.$"
''')
# 4) Aventurine reste sur place (au lieu de se balader) pour qu'on puisse lui parler facilement
fp = os.path.join(R, 'data/maps/LittlerootTown/map.json'); m = open(fp).read()
i = m.find('OBJ_EVENT_GFX_AVENTURINE')
if i >= 0:
    j = m.find('MOVEMENT_TYPE_WANDER_AROUND', i, i + 300)
    if j >= 0: m = m[:j] + 'MOVEMENT_TYPE_FACE_UP' + m[j+len('MOVEMENT_TYPE_WANDER_AROUND'):]
    open(fp, 'w').write(m)
print('ok')
