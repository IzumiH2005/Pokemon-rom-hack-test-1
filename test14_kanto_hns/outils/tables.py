"""Tables écrites à la main pour la bascule des extérieurs."""

# Portes : case Rouge Feu -> case HnS. None = bâtiment absent du Kanto de HnS.
PORTES = {
 'PewterCity': {(17,6):(19,8), (25,4):(27,6), (15,16):(16,18), (28,18):(30,22), (33,11):(35,15),
                (17,25):(19,29), (9,30):(11,34)},
 'CeruleanCity': {(10,11):(18,11), (30,11):(38,11), (15,17):(23,17), (22,19):(30,19), (31,21):(39,21),
                  (13,28):(21,28), (29,28):(37,28), (1,12):(9,12), (10,8):None, (31,8):None, (31,9):None,
                  (14,28):(22,28), (23,28):None, (17,11):None},
 'LavenderTown': {(18,6):(22,6), (6,5):(10,5), (10,11):(12,11), (5,16):(5,16), (10,16):(12,16), (20,15):(4,6)},
 'VermilionCity': {(22,34):None, (23,34):None, (24,34):None, (9,6):(15,4), (15,6):(22,4), (12,17):(18,16),
                   (19,17):(25,16), (29,17):(38,16), (28,24):(38,22), (14,25):(21,23)},
 'CeladonCity': {(34,21):(35,21), (11,14):(11,14), (15,14):(15,14), (30,11):(30,11), (48,11):(48,11),
                 (39,20):None, (11,30):(12,30), (37,29):(37,29), (41,29):(41,29), (49,29):None,
                 (29,5):(30,4), (30,4):(30,4), (31,5):(30,4)},
 'FuchsiaCity': {(24,5):(26,5), (33,31):None, (11,15):(11,15), (28,16):None, (9,32):(9,32), (14,31):(14,31),
                 (25,31):(25,31), (38,31):(38,31), (39,28):(39,28), (39,29):(39,28), (19,31):(19,30)},
 'CinnabarIsland': {(8,3):None, (20,4):None, (8,9):None, (14,11):(45,29), (19,11):None},
 'SaffronCity': {(33,30):(25,30), (22,14):(19,21), (40,12):(32,12), (46,12):(38,12), (27,21):None,
                 (40,21):(32,21), (24,38):(16,38), (43,38):(35,38), (8,27):(0,27), (34,5):(26,5),
                 (58,27):(50,27), (34,46):(26,46), (35,46):(27,46), (35,5):(27,5), (47,21):None},
 'Route2': {(5,13):(5,13), (6,13):(6,13), (5,51):(5,51), (17,11):(17,11), (17,22):(17,22), (18,46):(18,46),
            (18,41):(18,40), (19,41):(19,40), (19,46):(19,46), (6,51):(6,51)},
 'Route4': {(19,5):(18,9), (32,5):(32,5), (12,5):(12,5)},
 'Route5': {(31,31):(31,31), (23,25):(23,25), (24,32):(24,32), (25,32):(25,32)},
 'Route6': {(19,13):(49,13), (12,5):(42,5), (13,5):(43,5)},
 'Route7': {(7,14):(7,33), (15,10):(15,30)},
 'Route8': {(13,4):(9,3), (7,10):(3,9)},
 'Route10': {(8,19):(16,19), (8,57):(16,57), (7,40):(15,40), (13,20):(21,20), (2,37):(10,37)},
 'Route11': {(6,7):None, (58,10):None, (65,10):None},
 'Route12': {(12,86):(12,85), (14,15):None, (15,15):None, (14,21):None},
 'Route15': {(9,11):(9,11), (16,11):(16,11)},
 'Route16': {(10,5):(10,5), (20,6):(20,13), (27,6):(27,13), (20,13):(20,13), (27,13):(27,13)},
 'Route18': {(41,9):(41,9), (48,9):(48,9)},
 'Route20': {(60,8):(60,8), (72,14):(72,14)},
 'Route22': {(8,5):(12,9), (9,5):(12,9)},
 'Route25': {(51,4):(51,8)},
}
# La Cave Taupiqueur sort à Carmin dans HnS, plus sur la Route 11.
PORTE_DEPLACEE = ('Route11', (6, 7), 'VermilionCity', (61, 10), 'DiglettsCave_SouthEntrance')

# Intérieurs : places fixées à la main (local_id -> case), pour les scènes dont le décor a changé de forme.
PLACES = {
    'PalletTown_ProfessorOaksLab': {
        'LOCALID_OAKS_LAB_PROF_OAK': (13, 11), 'LOCALID_OAKS_LAB_RIVAL': (12, 12),
        'LOCALID_BULBASAUR_BALL': (15, 13), 'LOCALID_SQUIRTLE_BALL': (16, 13), 'LOCALID_CHARMANDER_BALL': (17, 13),
        'LOCALID_POKEDEX_1': (9, 10), 'LOCALID_POKEDEX_2': (10, 10),
    },
}

# Cartes associées à la main : Rouge Feu -> Heart & Soul (zone de la Ligue et donjons redessinés).
# Dans Heart & Soul, la Route Victoire se traverse avant la Route 23 : Portail -> B2F -> B1F -> 1F -> Route 23.
PAIRES_FIXES = {
    'Route22_NorthEntrance': 'ReceptionGate', 'Route23': 'Route23', 'IndigoPlateau_Exterior': 'IndigoPlateau',
    'IndigoPlateau_PokemonCenter_1F': 'IndigoPlateau_PokemonCenter',
    'VictoryRoad_1F': 'VictoryRoadKanto_B2F', 'VictoryRoad_2F': 'VictoryRoadKanto_B1F',
    'VictoryRoad_3F': 'VictoryRoadKanto_1F',
    'PokemonLeague_LoreleisRoom': 'PokemonLeague_WillsRoom', 'PokemonLeague_BrunosRoom': 'PokemonLeague_KogasRoom',
    'PokemonLeague_AgathasRoom': 'PokemonLeague_BrunosRoom', 'PokemonLeague_LancesRoom': 'PokemonLeague_KarensRoom',
    'PokemonLeague_ChampionsRoom': 'PokemonLeague_ChampionsRoom', 'PokemonLeague_HallOfFame': 'PokemonLeague_HallOfFame',
    'ViridianForest': 'ViridianForest', 'Route2_ViridianForest_SouthEntrance': 'Gate_Route2_ViridianForest',
    'Route2_ViridianForest_NorthEntrance': 'Gate_ViridianForest_Route2',
    'MtMoon_1F': 'MtMoon_Cave',
    'DiglettsCave_B1F': 'DiglettsCave_Tunnel', 'DiglettsCave_NorthEntrance': 'DiglettsCave_EntranceNorth',
    'DiglettsCave_SouthEntrance': 'DiglettsCave_EntranceSouth',
    'RockTunnel_1F': 'RockTunnel_1F', 'RockTunnel_B1F': 'RockTunnel_B1F',
}
# Cartes déjà reprises de Heart & Soul par un travail antérieur (Mont Argenté) : elles servent seulement de cible.
DEJA = {'Route28': 'Route28', 'Route28_House': 'Route28_House'}
# Étages de Rouge Feu sans équivalent : leurs dresseurs et leurs objets rejoignent l'étage indiqué.
FUSIONS = {}
