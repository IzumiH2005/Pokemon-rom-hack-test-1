# Installe Aventurine comme nouveau PNJ dans pokeemerald-expansion
import sys,re
sys.path.insert(0,'.')
R='/home/user/pokeemeraude-expansion/'
from avk import sheet,PAL
import importlib; m=importlib.import_module(sys.argv[1] if len(sys.argv)>1 else 'av5')
sheet(m.FR).save(R+'graphics/object_events/pics/people/aventurine.png')
open(R+'graphics/object_events/palettes/aventurine.pal','w').write(
    'JASC-PAL\r\n0100\r\n16\r\n'+''.join('%d %d %d\r\n'%c for c in PAL))
def edit(path,anchor,new,after=True,once_key=None):
    s=open(R+path).read()
    if (once_key or new.strip()) in s: return
    assert anchor in s,(path,anchor)
    s=s.replace(anchor,anchor+new if after else new+anchor,1)
    open(R+path,'w').write(s)
edit('include/constants/event_objects.h','    OBJ_EVENT_GFX_BREAKABLE_ROCK_FRLG,\n','    OBJ_EVENT_GFX_AVENTURINE,\n')
edit('include/constants/event_objects.h','#define OBJ_EVENT_PAL_TAG_SUBSTITUTE','#define OBJ_EVENT_PAL_TAG_AVENTURINE               0x1170\n',after=False)
edit('src/data/object_events/object_event_graphics.h',
 'const u32 gObjectEventPic_BreakableRockFrlg[] = INCGFX_U32("graphics/object_events/pics/misc/breakable_rock_frlg.png", ".4bpp", "-mwidth 2 -mheight 2");\n',
 'const u32 gObjectEventPic_Aventurine[] = INCGFX_U32("graphics/object_events/pics/people/aventurine.png", ".4bpp", "-mwidth 2 -mheight 4");\n'
 'const u16 gObjectEventPal_Aventurine[] = INCGFX_U16("graphics/object_events/palettes/aventurine.pal", ".gbapal");\n')
s=open(R+'src/data/object_events/object_event_pic_tables.h').read()
if 'sPicTable_Aventurine' not in s:
    s+='\nstatic const struct SpriteFrameImage sPicTable_Aventurine[] = {\n    overworld_ascending_frames(gObjectEventPic_Aventurine, 2, 4),\n};\n'
    open(R+'src/data/object_events/object_event_pic_tables.h','w').write(s)
s=open(R+'src/data/object_events/object_event_graphics_info.h').read()
if 'gObjectEventGraphicsInfo_Aventurine' not in s:
    s+='''
const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_Aventurine = {
    .tileTag = TAG_NONE,
    .paletteTag = OBJ_EVENT_PAL_TAG_AVENTURINE,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_NONE,
    .size = 256,
    .width = 16,
    .height = 32,
    .paletteSlot = PALSLOT_NPC_1,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .compressed = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_16x32,
    .subspriteTables = sOamTables_16x32,
    .anims = sAnimTable_Standard,
    .images = sPicTable_Aventurine,
};
'''
    open(R+'src/data/object_events/object_event_graphics_info.h','w').write(s)
edit('src/data/object_events/object_event_graphics_info_pointers.h','extern const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_BreakableRockFrlg;\n','extern const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_Aventurine;\n')
edit('src/data/object_events/object_event_graphics_info_pointers.h','    [OBJ_EVENT_GFX_BREAKABLE_ROCK_FRLG]      = &gObjectEventGraphicsInfo_BreakableRockFrlg,\n','    [OBJ_EVENT_GFX_AVENTURINE]               = &gObjectEventGraphicsInfo_Aventurine,\n')
edit('src/event_object_movement.c','    {gObjectEventPal_Substitute,            OBJ_EVENT_PAL_TAG_SUBSTITUTE},\n','    {gObjectEventPal_Aventurine,            OBJ_EVENT_PAL_TAG_AVENTURINE},\n',after=False)
print('installed')
