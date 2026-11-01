# V3 : corps fin de la V2 + bras dans le style du sprite d'origine (écartés, mains au bout)
from bv5 import B as B5
B=dict(B5)
NAPE='...fff4444fff...'
B['down']=(23,[
  '..f555e33e566f..',
  '.f55f55ee56f66f.',
  '.416f555e56f614.',
  '..4ffdccccdff4..',
  '....f787787f....',
  '...f67877877f...',
  '...f678ff877f...',
  '....fee..eef....'])
B['up']=(22,[NAPE,
  '..f5555ee5566f..',
  '.f55f555556f66f.',
  '.416f555566f614.',
  '..4ffdccccdff4..',
  '....f766667f....',
  '...f77877877f...',
  '...f778ff877f...',
  '....fee..eef....'])
def walk(top,chest,belly,waist,hak):
    A=[top,chest,
       '.f56'+belly+'f614.',
       '.41ffdccccdff4..',
       '..4.'+waist+'....',
       hak[0],hak[1],'....fee.........']
    Bw=[top,chest,
       '.416'+belly+'f66f.',
       '..4ffdccccdff14.',
       '....'+waist+'.4..',
       hak[0],hak[1],'.........eef....']
    return [(24,A),(24,Bw)]
B['down_wf']=walk('..f555e33e566f..','.f55f55ee56f66f.','f555e56','f787787f',
                  ['...f67877877f...','...f678ff877f...'])
up=walk('..f5555ee5566f..','.f55f555556f66f.','f555566','f766667f',
                  ['...f77877877f...','...f778ff877f...'])
B['up_wf']=[(23,[NAPE]+r) for s,r in up]
