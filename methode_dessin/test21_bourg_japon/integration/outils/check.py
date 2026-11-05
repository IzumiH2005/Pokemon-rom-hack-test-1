import struct, json, sys
E='/home/user/pokeemeraude-expansion'
def load(lay, mp, starts):
    v=struct.unpack('<400H',open(f'{E}/data/layouts/{lay}/map.bin','rb').read())
    attr=struct.unpack('<%dH'%(len(open(f'{E}/data/tilesets/secondary/japon/metatile_attributes.bin','rb').read())//2),open(f'{E}/data/tilesets/secondary/japon/metatile_attributes.bin','rb').read())
    free=lambda x,y:0<=x<20 and 0<=y<20 and not (v[y*20+x]>>10&3)
    seen=set(starts); st=list(starts)
    while st:
        x,y=st.pop()
        for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
            n=(x+dx,y+dy)
            if free(*n) and n not in seen: seen.add(n); st.append(n)
    m=json.load(open(f'{E}/data/maps/{mp}/map.json')); bad=[]
    for o in m['object_events']:
        if 'TRUCK' in o['graphics_id']: continue
        if (o['x'],o['y']) not in seen: bad.append(('npc',o['graphics_id'],o['x'],o['y']))
    for w in m['warp_events']:
        if (w['x'],w['y']) not in seen: bad.append(('warp',w['x'],w['y']))
    for t in m['coord_events']:
        if (t['x'],t['y']) not in seen: bad.append(('trig',t['x'],t['y']))
    for b in m['bg_events']:
        if not any((b['x']+dx,b['y']+dy) in seen for dx,dy in((1,0),(-1,0),(0,1),(0,-1))): bad.append(('sign',b['x'],b['y']))
    # layer: blocked cell whose south neighbour is walkable must not be COVERED
    lay_bad=[(x,y) for x in range(20) for y in range(19) if not free(x,y) and free(x,y+1)
             and (v[y*20+x]&0x3ff)>=0x200 and attr[(v[y*20+x]&0x3ff)-0x200]>>12==1]
    print(mp,'reachable',len(seen),'problems',bad,'covered-over-head',lay_bad)
load('LittlerootTown','LittlerootTown',[(10,0)])
load('Route101','Route101',[(10,19)])
