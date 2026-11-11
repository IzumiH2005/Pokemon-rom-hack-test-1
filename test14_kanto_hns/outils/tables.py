"""Tables écrites à la main pour la bascule des extérieurs."""

# Portes : case Rouge Feu -> case HnS. None = bâtiment absent du Kanto de HnS.
PORTES = {
 'PewterCity': {(17,6):(19,8), (25,4):(27,6), (15,16):(16,18), (28,18):(30,22), (33,11):(35,15),
                (17,25):(19,29), (9,30):(11,34)},
 'CeruleanCity': {(10,11):(18,11), (30,11):(38,11), (15,17):(23,17), (22,19):(30,19), (31,21):(39,21),
                  (13,28):(21,28), (29,28):(37,28), (1,12):(9,12), (10,8):None, (31,8):None, (31,9):None,
                  (14,28):(22,28), (23,28):(31,28), (17,11):(25,11)},
 'LavenderTown': {(18,6):(22,6), (6,5):(10,5), (10,11):(12,11), (5,16):(5,16), (10,16):(12,16), (20,15):(4,6)},
 'VermilionCity': {(22,34):None, (23,34):None, (24,34):None, (9,6):(15,4), (15,6):(22,4), (12,17):(18,16),
                   (19,17):(25,16), (29,17):(38,16), (28,24):(38,22), (14,25):(21,23)},
 'CeladonCity': {(34,21):(35,21), (11,14):(11,14), (15,14):(15,14), (30,11):(30,11), (48,11):(48,11),
                 (39,20):(26,18), (11,30):(12,30), (37,29):(37,29), (41,29):(41,29), (49,29):(49,29),
                 (29,5):(30,4), (30,4):(30,4), (31,5):(30,4)},
 'FuchsiaCity': {(24,5):(26,5), (33,31):(33,31), (11,15):(11,15), (28,16):None, (9,32):(9,32), (14,31):(14,31),
                 (25,31):(25,31), (38,31):(38,31), (39,28):(39,28), (39,29):(39,28), (19,31):(19,31)},
 'CinnabarIsland': {(8,3):(34,15), (20,4):(30,24), (8,9):(33,25), (14,11):(45,29), (19,11):(48,30)},
 'SaffronCity': {(33,30):(25,30), (22,14):(19,21), (40,12):(32,12), (46,12):(38,12), (27,21):(39,21),
                 (40,21):(32,21), (24,38):(16,38), (43,38):(35,38), (8,27):(0,27), (34,5):(26,5),
                 (58,27):(50,27), (34,46):(26,46), (35,46):(27,46), (35,5):(27,5), (47,21):(13,14)},
 'Route2': {(5,13):(5,13), (6,13):(6,13), (5,51):(5,51), (17,11):(17,11), (17,22):(17,22), (18,46):(18,46),
            (18,41):(18,40), (19,41):(19,40), (19,46):(19,46), (6,51):(6,51)},
 'Route4': {(19,5):(18,9), (32,5):(32,5), (12,5):(12,5)},
 'Route5': {(31,31):(31,31), (23,25):(23,25), (24,32):(24,32), (25,32):(25,32)},
 'Route6': {(19,13):(49,13), (12,5):(42,5), (13,5):(43,5)},
 'Route7': {(7,14):(7,34), (15,10):(15,30)},
 'Route8': {(13,4):(9,4), (7,10):(3,9)},
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
# Entrées creusées dans un décor Heart & Soul : dossier du layout -> [(x, y, bloc)]. 0x30A9 = entrée de grotte.
# Cramois'Île est celle d'après l'éruption : Manoir, Arène, Labo et Boutique s'ouvrent dans la falaise.
# Collisions oubliées par Heart & Soul (case marchable sur un rocher, un toit, un mur, une plante) : décor -> cases à bloquer.
_GALERIE = [(x, 6) for x in range(27)]        # mur des lampes au fond des entrées du Souterrain
COLLISIONS = {
    'Hns_Route2': [(x, 5) for x in range(14, 20)],                         # rebord du rocher sous la barrière
    'Hns_Route23': [(19, 17)],                                             # coin du rocher (le garde Cascade monte en tête du couloir)
    'Hns_Route21': [(21, 38), (22, 38), (21, 39), (22, 39)],               # rocher dans l'eau
    'Hns_TohjoFalls_Cavern': [(14, 22), (15, 22), (14, 23), (15, 23)],     # rocher dans l'eau
    'Hns_VermilionCity_PortOutside': [(41, 0), (42, 0), (41, 1), (42, 1)],  # rocher dans l'eau
    'Hns_PalletTownHouseRedsHouse2': [(x, 0) for x in range(20)],          # mur du fond de la chambre
    'Hns_Route5_TunnelEntrance': _GALERIE, 'Hns_Route6_TunnelEntrance': _GALERIE,
    'Hns_Route7_TunnelEntrance': _GALERIE, 'Hns_Route8_TunnelEntrance': _GALERIE,
    # Plante en pot à l'entrée des postes de garde.
    'Hns_FuchsiaCity_Route15_Gate': [(1, 7)], 'Hns_Gate_CeladonCity_Route16': [(1, 7)],
    'Hns_Gate_FuchsiaCity_Route18': [(1, 7)], 'Hns_Gate_SaffronCity_Route7': [(1, 7)], 'Hns_Gate_SaffronCity_Route8': [(1, 7)],
    # Buissons isolés.
    'Hns_CeladonCity': [(53, 33)], 'Hns_Route3': [(75, 14)], 'Hns_Route4': [(48, 3)],
    # Rang du haut du toit des cabanes du Souterrain : le joueur passait derrière.
    'Hns_Route5': [(30, 28), (31, 28), (32, 28)], 'Hns_Route6': [(48, 10), (49, 10), (50, 10), (51, 10)],
    'Hns_Route7': [(6, 31), (7, 31), (8, 31), (9, 31), (16, 27), (17, 27), (18, 27)],
}

RETOUCHES = {'Hns_CinnabarIsland': [(34, 15, 0x30A9), (30, 24, 0x30A9), (33, 25, 0x30A9), (48, 30, 0x30A9)],
             # Mont Sélénite : un passage dans les éboulis rouvre la salle des fossiles, murée dans Heart & Soul.
             'Hns_MtMoon_Cave': [(6, 9, 0x3281), (6, 8, 0x3281), (6, 7, 0x3284), (6, 6, 0x3281), (6, 5, 0x3281),
                                 (7, 5, 0x3281), (8, 5, 0x3281)],
             # Maisons de Rouge Feu sans porte dans Heart & Soul : la porte du modèle voisin est posée sur une façade libre.
             # Parmanie : maison du Gardien (33,31) et maison du frère du Maître Pêcheur (19,31).
             'Hns_FuchsiaCity': [(x + dx, 30 + dy, b) for x in (19, 33)
                                 for dx, dy, b in ((0, 0, 0x06B1), (1, 0, 0x06B2), (0, 1, 0x06BF), (1, 1, 0x06B9))],
             # Safran : maison aux Roucool (39,21) ; le Fan Club prend la porte de la gare (13,14).
             'Hns_SaffronCity': [(38, 20, 0x06BE), (39, 20, 0x06BF), (40, 20, 0x06AF),
                                 (38, 21, 0x06AE), (39, 21, 0x075C), (40, 21, 0x068C)],
             # Azuria : maisons 5 (25,11) et 4 (31,28).
             'Hns_CeruleanCity': [(x + dx, y + dy, b) for x, y in ((24, 10), (30, 27))
                                  for dx, dy, b in ((0, 0, 0x06C3), (1, 0, 0x0690), (2, 0, 0x06C4),
                                                    (0, 1, 0x06C1), (1, 1, 0x0698), (2, 1, 0x06C2))],
             # Céladopole : maison (41,29) et hôtel (49,29) ; la salle des lots prend le bâtiment bleu (26,18).
             'Hns_CeladonCity': [(x + dx, 28 + dy, b) for x in (40, 48)
                                 for dx, dy, b in ((0, 0, 0x0714), (1, 0, 0x0715), (2, 0, 0x0716),
                                                   (0, 1, 0x06E5), (1, 1, 0x043D), (2, 1, 0x06E7))]
                                # Clôture ouverte à l'ouest : l'enclos de la salle des lots ne s'atteignait qu'en Surf.
                                + [(23, 20, 0x3008)]}
# Panneaux reposés à la main : carte -> {script: case}.
PANNEAUX = {'CinnabarIsland': {'CinnabarIsland_EventScript_GymSign': (31, 25),
                               'CinnabarIsland_EventScript_IslandSign': (41, 33)}}
# La Cave Taupiqueur sort à Carmin dans HnS, plus sur la Route 11.
PORTE_DEPLACEE = ('Route11', (6, 7), 'VermilionCity', (61, 10), 'DiglettsCave_SouthEntrance')

# Intérieurs : places fixées à la main (local_id -> case), pour les scènes dont le décor a changé de forme.
D = 'MOVEMENT_TYPE_FACE_RIGHT'
PLACES = {
    'PalletTown_ProfessorOaksLab': {
        'LOCALID_OAKS_LAB_PROF_OAK': (13, 11), 'LOCALID_OAKS_LAB_RIVAL': (12, 12),
        'LOCALID_BULBASAUR_BALL': (15, 12), 'LOCALID_SQUIRTLE_BALL': (16, 12), 'LOCALID_CHARMANDER_BALL': (17, 12),
        'LOCALID_POKEDEX_1': (9, 10), 'LOCALID_POKEDEX_2': (10, 10),
    },
    # Clé : local_id, script, ou rang du PNJ dans la carte.
    'FuchsiaCity_SafariZone_Entrance': {0: (2, 5), 'FuchsiaCity_SafariZone_Entrance_EventScript_InfoAttendant': (2, 10)},
    'SafariZone_West': {'SafariZone_SecretHouse_EventScript_Attendant': (9, 8),
                        # Occupants de la maison de repos, absente de Heart & Soul : près du gardien, sur le chemin.
                        'SafariZone_West_RestHouse_EventScript_Scientist': (8, 10, D),
                        'SafariZone_West_RestHouse_EventScript_Man': (8, 9, D),
                        'SafariZone_West_RestHouse_EventScript_CooltrainerF': (38, 22)},      # donne la CS Surf
    'SSAnne_Exterior': {'LOCALID_SS_ANNE': (6, 12)},
    'CinnabarIsland_Gym': {'CinnabarIsland_Gym_EventScript_Blaine': (18, 10), 'LOCALID_QUINN': (25, 13),
                           'CinnabarIsland_Gym_EventScript_Erik': (23, 9), 'LOCALID_AVERY': (16, 12),
                           'LOCALID_DEREK': (25, 11), 'CinnabarIsland_Gym_EventScript_GymGuy': (20, 23),
                           'LOCALID_DUSTY': (12, 14), 'LOCALID_ZAC': (13, 17), 'LOCALID_RAMON': (21, 16)},
    # Occupants de l'étage disparu du poste : hors du passage et des déclencheurs.
    'Route16_NorthEntrance_1F': {'Route16_NorthEntrance_2F_EventScript_LittleBoy': (3, 4),
                                 'Route16_NorthEntrance_2F_EventScript_LittleGirl': (8, 6),
                                 'Route16_NorthEntrance_2F_EventScript_Aide': (9, 4)},
    'MtMoon_1F': {'MtMoon_1F_EventScript_Josh': (17, 9), 'MtMoon_1F_EventScript_Robby': (20, 15), 'MtMoon_1F_EventScript_Jovan': (40, 27)},
    'SaffronCity_Dojo': {'LOCALID_KARATE_MASTER': (14, 6)},
    'CinnabarIsland': {'LOCALID_CINNABAR_BILL': (30, 27)},
    'IndigoPlateau_PokemonCenter_1F': {'LOCALID_LEAGUE_DOOR_GUARD': (33, 4)},
    # Gardes des badges : au Portail, le garde tient le bord gauche du couloir ; sur la Route 23, réduite à sa sortie
    # de la Route Victoire, les sept gardes s'alignent le long du dernier couloir, un contrôle par rangée.
    'Route22_NorthEntrance': {'Route22_NorthEntrance_EventScript_BoulderBadgeGuard': (9, 6, D)},
    'Route23': {'LOCALID_CASCADE_BADGE_GUARD': (19, 10, D), 'LOCALID_THUNDER_BADGE_GUARD': (19, 16, D),
                'LOCALID_RAINBOW_BADGE_GUARD': (19, 15, D), 'LOCALID_SOUL_BADGE_GUARD': (19, 14, D),
                'LOCALID_MARSH_BADGE_GUARD': (19, 13, D), 'LOCALID_VOLCANO_BADGE_GUARD': (19, 12, D),
                'LOCALID_EARTH_BADGE_GUARD': (19, 11, D)},
    # Extérieurs.
    'Route22': {'LOCALID_ROUTE22_RIVAL': (29, 8)},
    # Crissy : le plateau fleuri de Heart & Soul est fermé, elle attend sur le chemin du dessous.
    'Route4': {'Route4_EventScript_Crissy': (80, 6, D)},
    # Sbires de Safrania : chacun devant la porte qu'il garde (maison de Copieuse, arène, maison aux Roucool).
    'SaffronCity': {'SaffronCity_EventScript_RocketGrunt1': (19, 22), 'SaffronCity_EventScript_RocketGrunt3': (38, 13),
                    'SaffronCity_EventScript_RocketGrunt4': (39, 22)},
    # Maître d'E-Coque : dans l'enclos derrière la salle des lots, rouvert côté ouest.
    'CeladonCity': {'CeladonCity_EventScript_SoftboiledTutor': (28, 20)},
    'CeladonCity_DepartmentStore_2F': {'CeladonCity_DepartmentStore_2F_EventScript_Woman': (6, 3)},
    'PewterCity_Museum_1F': {'PewterCity_Museum_1F_EventScript_OldAmberScientist': (23, 3)},
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
    'CeruleanCave_1F': 'CeruleanCave_1F', 'CeruleanCave_2F': 'CeruleanCave_B1F', 'CeruleanCave_B1F': 'CeruleanCave_B2F',
    'SeafoamIslands_1F': 'SeafoamIslands_1F', 'SeafoamIslands_B1F': 'SeafoamIslands_B1F',
    'SeafoamIslands_B4F': 'SeafoamIslands_SecretCave',      # salle d'Artikodin
    'CinnabarIsland_Gym': 'SeafoamIslands_Gym',             # comme dans Or et Argent : l'Arène d'Auguste est aux Îles Écume
    'PowerPlant': 'Route10_PowerPlantEntrance',
    'UndergroundPath_NorthEntrance': 'Route5_TunnelEntrance', 'UndergroundPath_SouthEntrance': 'Route6_TunnelEntrance',
    'UndergroundPath_WestEntrance': 'Route7_TunnelEntrance', 'UndergroundPath_EastEntrance': 'Route8_TunnelEntrance',
    'UndergroundPath_NorthSouthTunnel': 'SaffronCity_Tunnel_NS', 'UndergroundPath_EastWestTunnel': 'SaffronCity_Tunnel_SW',
    # Parc Safari : quatre zones reliées par des connexions, plus une grotte.
    'FuchsiaCity_SafariZone_Entrance': 'FuchsiaCity_SafariZoneEntrance', 'SafariZone_Center': 'FuchsiaCity_SafariZoneBeach',
    'SafariZone_West': 'FuchsiaCity_SafariZoneBrush', 'SafariZone_North': 'FuchsiaCity_SafariZoneMountain',
    'SafariZone_East': 'FuchsiaCity_SafariZoneCave',
    'SSAnne_Exterior': 'VermilionCity_PortInside',          # le quai de l'Océane
}
# Cartes déjà reprises de Heart & Soul par un travail antérieur (Mont Argenté) : elles servent seulement de cible.
DEJA = {'Route28': 'Route28', 'Route28_House': 'Route28_House'}
# Étages de Rouge Feu sans équivalent : leurs dresseurs et leurs objets rejoignent l'étage indiqué.
FUSIONS = {'SeafoamIslands_B1F': ['SeafoamIslands_B2F', 'SeafoamIslands_B3F'],
           'MtMoon_1F': ['MtMoon_B1F', 'MtMoon_B2F']}
# Cartes de Heart & Soul sans équivalent dans Rouge Feu, créées vides : nom -> (musique, zone de la carte).
NOUVELLES = {
    'MtMoon_Outside': ('MUS_RG_ROUTE3', 'MAPSEC_MT_MOON'), 'MtMoon_Shop': ('MUS_RG_ROUTE3', 'MAPSEC_MT_MOON'),
    'Route10_PowerPlantBackRoom': ('MUS_RG_POKE_MANSION', 'MAPSEC_POWER_PLANT'),
    'Route26North': ('MUS_RG_ROUTE24', 'MAPSEC_ROUTE_26'), 'Route26': ('MUS_RG_ROUTE24', 'MAPSEC_ROUTE_26'),
    'Route26_House1': ('MUS_RG_ROUTE24', 'MAPSEC_ROUTE_26'), 'Route26_House2': ('MUS_RG_ROUTE24', 'MAPSEC_ROUTE_26'),
    'Route27': ('MUS_RG_ROUTE24', 'MAPSEC_ROUTE_27'),
    'TohjoFalls_Cavern': ('MUS_RG_MT_MOON', 'MAPSEC_TOHJO_FALLS'),
    'TohjoFalls_GiovanniRoom': ('MUS_RG_MT_MOON', 'MAPSEC_TOHJO_FALLS'),
    'Route19_Cave': ('MUS_RG_MT_MOON', 'MAPSEC_ROUTE_19'),
    'SaffronCity_FightingDojoVIP': ('MUS_RG_GYM', 'MAPSEC_SAFFRON_CITY'),
    'VermilionCity_PortOutside': ('MUS_RG_VERMILLION', 'MAPSEC_VERMILION_CITY'),
}
ZONES = {'MAPSEC_ROUTE_26': ('ROUTE 26', 1, 10), 'MAPSEC_ROUTE_27': ('ROUTE 27', 0, 12),
         'MAPSEC_TOHJO_FALLS': ('CHUTES TOHJO', 0, 12)}
# Scripts de carte de Rouge Feu liés à l'ancien décor (courants, portes) : types retirés de la table de la carte.
SCRIPTS_RETIRES = {'SeafoamIslands_B4F': ('MAP_SCRIPT_ON_LOAD', 'MAP_SCRIPT_ON_WARP_INTO_MAP_TABLE', 'MAP_SCRIPT_ON_FRAME_TABLE')}

# Bâtiments de Rouge Feu absents de Heart & Soul : leurs occupants se tiennent dehors, dans la carte indiquée.
HABITANTS = {'SafariZone_Center': ['SafariZone_Center_RestHouse'],
             'SafariZone_West': ['SafariZone_SecretHouse', 'SafariZone_West_RestHouse'],
             'SafariZone_North': ['SafariZone_North_RestHouse'], 'SafariZone_East': ['SafariZone_East_RestHouse'],
             # Postes de Heart & Soul sans étage : l'aide du Prof. Chen et les autres occupants descendent au rez-de-chaussée.
             'Route15_WestEntrance_1F': ['Route15_WestEntrance_2F'], 'Route16_NorthEntrance_1F': ['Route16_NorthEntrance_2F'],
             'Route18_EastEntrance_1F': ['Route18_EastEntrance_2F']}
# Déclencheurs gardés : carte -> script -> case dans le décor Heart & Soul.
P = 'FuchsiaCity_SafariZone_Entrance_EventScript_EntryTrigger'
# Une case, ou une liste de cases : la i-ème case reçoit le i-ème déclencheur d'origine du script.


def _trio(prefixe, noms, cases): return {prefixe + n: c for n, c in zip(noms, cases)}


def _poste_ns(c): return _trio(c + '_EventScript_GuardTrigger', ('Left', 'Mid', 'Right'), [(5, 6), (6, 6), [(7, 6), (8, 6), (9, 6)]])


def _poste_eo(c): return _trio(c + '_EventScript_GuardTrigger', ('Top', 'Mid', 'Bottom'), [(6, 4), (6, 5), (6, 6)])


def _poste_velo(c):
    d = _trio(c + '_EventScript_NeedBikeTrigger', ('Top', 'MidTop', 'Mid'), [(6, 4), (6, 5), (6, 6)])
    d['EventScript_SetEnteringCyclingRoad'] = [(2, 5), (1, 4), (1, 6)]
    d['EventScript_SetExitingCyclingRoad'] = [(10, 5), (11, 4), (11, 6)]
    return d


L = 'PalletTown_ProfessorOaksLab_EventScript_'
G = 'Route23_EventScript_%sBadgeGuardTrigger'
DECLENCHEURS = {
    'CinnabarIsland': {'CinnabarIsland_EventScript_GymDoorLocked': (30, 25)},
    'FuchsiaCity_SafariZone_Entrance': {P + 'Mid': (5, 5), P + 'Right': (6, 5), P + 'Left': (4, 5)},
    # Labo de Chen : la cloison du décor laisse trois cases de passage vers la sortie.
    'PalletTown_ProfessorOaksLab': {
        L + 'LeaveStarterSceneTrigger': [(12, 16), (13, 16), (14, 16)],
        L + 'RivalBattleTriggerLeft': (12, 16), L + 'RivalBattleTriggerMid': (13, 16), L + 'RivalBattleTriggerRight': (14, 16)},
    'PewterCity_Museum_1F': _trio('PewterCity_Museum_1F_EventScript_EntranceTrigger', ('Left', 'Mid', 'Right'),
                                  [(12, 5), (13, 5), (14, 5)]),
    'SaffronCity_Dojo': {'SaffronCity_Dojo_EventScript_TriggerMasterBattleLeft': (13, 6),
                         'SaffronCity_Dojo_EventScript_TriggerMasterBattleRight': (15, 6)},
    'Route5_SouthEntrance': _poste_ns('Route5_SouthEntrance'), 'Route6_NorthEntrance': _poste_ns('Route6_NorthEntrance'),
    'Route7_EastEntrance': _poste_eo('Route7_EastEntrance'), 'Route8_WestEntrance': _poste_eo('Route8_WestEntrance'),
    'Route16_NorthEntrance_1F': _poste_velo('Route16_NorthEntrance_1F'),
    'Route18_EastEntrance_1F': _poste_velo('Route18_EastEntrance_1F'),
    'Route22_NorthEntrance': {'Route22_NorthEntrance_EventScript_BoulderBadgeGuardTrigger': [(10, 6), (11, 6), (12, 6)]},
    'Route23': {G % b: [(20, y), (21, y)] for b, y in zip(('Cascade', 'Thunder', 'Rainbow', 'Soul', 'Marsh', 'Volcano', 'Earth'),
                                                          (10, 16, 15, 14, 13, 12, 11))},
    # Extérieurs : mêmes scènes, décalées avec la ville.
    'PewterCity': dict(_trio('PewterCity_EventScript_GymGuideTrigger', ('Top', 'Mid', 'Bottom', 'Right'),
                             [(44, 25), (44, 26), (44, 27), (45, 27)]),
                       **_trio('PewterCity_EventScript_RunningShoesAideTrigger', ('Top', 'Mid', 'Bottom'),
                               [(48, 25), (48, 26), (48, 27)])),
    'Route22': dict(_trio('Route22_EventScript_EarlyRivalTrigger', ('Top', 'Mid', 'Bottom'), [(37, 8), (37, 9), (37, 10)]),
                    **_trio('Route22_EventScript_LateRivalTrigger', ('Top', 'Mid', 'Bottom'), [(37, 8), (37, 9), (37, 10)])),
}
# Portes dont l'arrivée est imposée : carte -> {numéro : (carte d'arrivée, porte d'arrivée)}.
# L'Arène d'Auguste garde le décor de la grotte de Heart & Soul mais s'ouvre sur Cramois'Île, où Rouge Feu
# place le verrou de la Clé Secrète et la scène de Léo ; l'échelle des Îles Écume mène alors chez Artikodin.
PORTES_FORCEES = {'CinnabarIsland_Gym': {0: ('MAP_CINNABAR_ISLAND', '1'), 1: ('MAP_CINNABAR_ISLAND', '1')},
                  'SeafoamIslands_1F': {1: ('MAP_SEAFOAM_ISLANDS_B4F', '0')},
                  'SeafoamIslands_B4F': {0: ('MAP_SEAFOAM_ISLANDS_1F', '1')}}
# Portes ajoutées à un décor Heart & Soul : (x, y, carte, numéro de porte d'arrivée).
PORTES_AJOUTEES = {'SSAnne_Exterior': [(8, 10, 'MAP_SSANNE_1F_CORRIDOR', '2')]}
# PNJ (local_id ou script) et déclencheurs (script) d'un extérieur déplacés dans une autre carte : (source, clé, cible, x, y).
TRANSFERTS = [
    ('VermilionCity', 'LOCALID_VERMILION_FERRY_SAILOR', 'SSAnne_Exterior', 9, 9),
    ('VermilionCity', 'VermilionCity_EventScript_CheckTicketLeft', 'SSAnne_Exterior', 8, 9),
    ('VermilionCity', 'VermilionCity_EventScript_ExitedTicketCheck', 'SSAnne_Exterior', 8, 8),
    # Scène du fossile : même salle que dans Rouge Feu, aux mêmes cases.
    ('MtMoon_B2F', 'LOCALID_MIGUEL', 'MtMoon_1F', 13, 11),
    ('MtMoon_B2F', 'LOCALID_DOME_FOSSIL', 'MtMoon_1F', 13, 7),
    ('MtMoon_B2F', 'LOCALID_HELIX_FOSSIL', 'MtMoon_1F', 14, 7),
    ('MtMoon_B2F', 'MtMoon_B2F_EventScript_MiguelTrigger', 'MtMoon_1F', 14, 11),
    # Postes des Routes 11 et 12 absents de Heart & Soul : leurs occupants attendent sur la route.
    ('Route11_EastEntrance_2F', 'Route11_EastEntrance_2F_EventScript_Aide', 'Route11', 56, 9),
    ('Route11_EastEntrance_2F', 'Route11_EastEntrance_2F_EventScript_Turner', 'Route11', 55, 12),
    ('Route12_NorthEntrance_2F', 'Route12_NorthEntrance_2F_EventScript_Lass', 'Route12', 13, 8),
]
# Scripts ajoutés à la fin du fichier d'une carte.
SCRIPTS_AJOUTES = {'SSAnne_Exterior': """
@ Bout de la passerelle : le décor Heart & Soul n'a pas de case de porte, un déclencheur fait monter à bord.
SSAnne_Exterior_EventScript_Embarquer::
	lockall
	warp MAP_SSANNE_1F_CORRIDOR, 2
	waitstate
	releaseall
	end
"""}
DECLENCHEURS_AJOUTES = {'SSAnne_Exterior': [(8, 10, 'VAR_TEMP_1', 'SSAnne_Exterior_EventScript_Embarquer')]}
# Scripts qui visent une case précise de l'ancien décor : fichier -> [(texte de Rouge Feu, texte adapté)].
E = 'FuchsiaCity_SafariZone_Entrance_'
REMPLACEMENTS = {
    # Ferry des îles Sevii : il accoste au quai du port, là où se tient désormais le marin.
    'src/seagallop.c': [
        ('MAP_GROUP(MAP_VERMILION_CITY), MAP_NUM(MAP_VERMILION_CITY),      0x17, 0x20',
         'MAP_GROUP(MAP_SSANNE_EXTERIOR), MAP_NUM(MAP_SSANNE_EXTERIOR),      8, 8'),
        ('mapGroup == MAP_GROUP(MAP_VERMILION_CITY)', 'mapGroup == MAP_GROUP(MAP_SSANNE_EXTERIOR)'),
        ('mapNum == MAP_NUM(MAP_VERMILION_CITY)', 'mapNum == MAP_NUM(MAP_SSANNE_EXTERIOR)'),
        ('pos.x < 24', 'pos.x < 9'),
    ],
    # Positions fixées par script (setobjectxyperm) : reportées sur le nouveau décor.
    'data/maps/PalletTown_ProfessorOaksLab_Frlg/scripts.inc': [
        ('LOCALID_OAKS_LAB_PROF_OAK, 6, 11', 'LOCALID_OAKS_LAB_PROF_OAK, 13, 19'),
        ('LOCALID_OAKS_LAB_PROF_OAK, 6, 3', 'LOCALID_OAKS_LAB_PROF_OAK, 13, 11'),
        ('LOCALID_OAKS_LAB_RIVAL, 5, 10', 'LOCALID_OAKS_LAB_RIVAL, 12, 18'),
        ('LOCALID_OAKS_LAB_RIVAL, 6, 10', 'LOCALID_OAKS_LAB_RIVAL, 13, 18')],
    # Chen ramène le joueur au labo : il arrive sur le tapis de la porte Heart & Soul, plus dans le vide.
    'data/maps/PalletTown_Frlg/scripts.inc': [('warp MAP_PALLET_TOWN_PROFESSOR_OAKS_LAB, 6, 12', 'warp MAP_PALLET_TOWN_PROFESSOR_OAKS_LAB, 13, 20')],
    # Le courant d'Écume mène à la grotte d'Artikodin : arrivée devant la sortie au lieu d'un mur.
    'data/maps/SeafoamIslands_B3F_Frlg/scripts.inc': [('warp MAP_SEAFOAM_ISLANDS_B4F, 27, 21', 'warp MAP_SEAFOAM_ISLANDS_B4F, 16, 16')],
    'data/maps/Route22_Frlg/scripts.inc': [('LOCALID_ROUTE22_RIVAL, 25, 5', 'LOCALID_ROUTE22_RIVAL, 29, 9')],
    'data/maps/CeruleanCity_Frlg/scripts.inc': [
        ('LOCALID_CERULEAN_POLICEMAN, 30, 12', 'LOCALID_CERULEAN_POLICEMAN, 38, 12'),
        # Le sud de la ville est ouvert dans Heart & Soul : Flagadoss et la fille ne barrent plus rien, ils restent en place.
        ('\tsetobjectxyperm LOCALID_CERULEAN_SLOWBRO, 26, 31\n', ''), ('\tsetobjectxyperm LOCALID_CERULEAN_LASS, 27, 31\n', ''),
        ('LOCALID_CERULEAN_RIVAL, 23, 0', 'LOCALID_CERULEAN_RIVAL, 31, 0'),
        ('LOCALID_CERULEAN_RIVAL, 24, 0', 'LOCALID_CERULEAN_RIVAL, 32, 0')],
    'data/maps/SaffronCity_Frlg/scripts.inc': [('LOCALID_SAFFRON_DOOR_GUARD_GRUNT, 33, 31', 'LOCALID_SAFFRON_DOOR_GUARD_GRUNT, 25, 31')],
    'data/maps/IndigoPlateau_PokemonCenter_1F_Frlg/scripts.inc': [('LOCALID_LEAGUE_DOOR_GUARD, 4, 2', 'LOCALID_LEAGUE_DOOR_GUARD, 32, 3')],
    # Cramois'Île : l'Arène est loin du rivage, le ferry de Léo part après un fondu au lieu d'accoster.
    'data/maps/CinnabarIsland_Frlg/scripts.inc': [
        ('LOCALID_CINNABAR_BILL, 15, 12', 'LOCALID_CINNABAR_BILL, 46, 30'),
        ('goto_if_ge VAR_0x8004, 18,', 'goto_if_lt VAR_0x8004, 40,'),
        ('LOCALID_CINNABAR_BILL, 18, 12\n\tsetobjectmovementtype LOCALID_CINNABAR_BILL, MOVEMENT_TYPE_FACE_UP',
         'LOCALID_CINNABAR_BILL, 41, 30\n\tsetobjectmovementtype LOCALID_CINNABAR_BILL, MOVEMENT_TYPE_FACE_RIGHT'),
        ('LOCALID_CINNABAR_BILL, 21, 8', 'LOCALID_CINNABAR_BILL, 39, 34'),
        ('BillFacePlayer2::\n\tapplymovement LOCALID_CINNABAR_BILL, Common_Movement_WalkInPlaceFasterLeft',
         'BillFacePlayer2::\n\tapplymovement LOCALID_CINNABAR_BILL, Common_Movement_WalkInPlaceFasterRight'),
        ('\tapplymovement LOCALID_PLAYER, Common_Movement_WalkInPlaceFasterRight\n\twaitmovement 0\n\treturn',
         '\tapplymovement LOCALID_PLAYER, Common_Movement_WalkInPlaceFasterLeft\n\twaitmovement 0\n\treturn'),
        ('BillApproachPlayer2::\n\twalk_left\n\twalk_left\n\twalk_left', 'BillApproachPlayer2::\n\twalk_right\n\twalk_right\n\twalk_right'),
        ('BillExit::\n' + '\twalk_down\n' * 6, 'BillExit::\n' + '\twalk_right\n' * 3),
        ('BillExitToPokeCenter::\n\twalk_right\n' + '\twalk_down\n' * 6, 'BillExitToPokeCenter::\n\twalk_down\n' + '\twalk_left\n' * 4),
        ('PlayerWatchBillExit::\n\twalk_left\n\twalk_in_place_faster_right', 'PlayerWatchBillExit::\n\twalk_right\n\twalk_in_place_faster_left'),
        ('BillApproachDoor::\n\tdelay_16\n\twalk_left', 'BillApproachDoor::\n\tdelay_16\n\twalk_right'),
        ('opendoor 14, 11', 'opendoor 45, 29'), ('closedoor 14, 11', 'closedoor 45, 29'),
        ('\tcall_if_set FLAG_TEMP_2, CinnabarIsland_EventScript_ApproachShore\n\taddobject LOCALID_CINNABAR_SEAGALLOP\n'
         '\tcall_if_unset FLAG_TEMP_2, CinnabarIsland_EventScript_BoatArrive\n'
         '\tcall_if_set FLAG_TEMP_2, CinnabarIsland_EventScript_BoatArriveExitedPokeCenter\n', ''),
        ('\tcall_if_unset FLAG_TEMP_2, CinnabarIsland_EventScript_BoardBoat\n'
         '\tcall_if_set FLAG_TEMP_2, CinnabarIsland_EventScript_BoardBoatExitedPokeCenter\n', '\tfadescreen FADE_TO_BLACK\n')],
    # Retour des Îles Sevii : le ferry dépose sur la plage sud.
    'src/seagallop.c': [('MAP_NUM(MAP_CINNABAR_ISLAND),     0x15, 0x07}', 'MAP_NUM(MAP_CINNABAR_ISLAND),     39, 33}')],
    # Gardes des badges : ils se tiennent à gauche du passage et regardent vers la droite.
    'data/scripts/route23.inc': [('applymovement VAR_0x8009, Common_Movement_WalkInPlaceFasterLeft',
                                  'applymovement VAR_0x8009, Common_Movement_WalkInPlaceFasterRight'),
                                 ('applymovement VAR_0x8009, Common_Movement_WalkInPlaceFasterDown',
                                  'applymovement VAR_0x8009, Common_Movement_WalkInPlaceFasterRight')],
    'data/scripts/safari_zone.inc': [('MAP_FUCHSIA_CITY_SAFARI_ZONE_ENTRANCE, 4, 1', 'MAP_FUCHSIA_CITY_SAFARI_ZONE_ENTRANCE, 5, 2')],
    'data/maps/FuchsiaCity_SafariZone_Entrance_Frlg/scripts.inc': [
        ('MAP_SAFARI_ZONE_CENTER, 26, 30', 'MAP_SAFARI_ZONE_CENTER, 20, 39'),
        ('MAP_SAFARI_ZONE_CENTER, 255, 26, 30', 'MAP_SAFARI_ZONE_CENTER, 255, 20, 39'),
        # L'employé du guichet est à gauche du couloir, et la porte du parc une case plus loin.
        ('Common_Movement_WalkInPlaceFasterRight\n\twaitmovement 0\n\tshowmoneybox',
         'Common_Movement_WalkInPlaceFasterLeft\n\twaitmovement 0\n\tshowmoneybox'),
        (E + 'Movement_Exit::\n', E + 'Movement_Exit::\n\twalk_down\n'),
        (E + 'Movement_EnterSafariZoneMid::\n', E + 'Movement_EnterSafariZoneMid::\n\twalk_up\n'),
        (E + 'Movement_EnterSafariZoneRight::\n', E + 'Movement_EnterSafariZoneRight::\n\twalk_up\n'),
        (E + 'Movement_EnterSafariZoneLeft::\n', E + 'Movement_EnterSafariZoneLeft::\n\twalk_up\n'),
    ],
    'data/maps/SSAnne_Exterior_Frlg/scripts.inc': [
        ('SSAnne_Exterior_Movement_Exit::\n\twalk_up\n', 'SSAnne_Exterior_Movement_Exit::\n'),      # 8 pas jusqu'à la porte
        # Entrée par la porte du hall : 8 pas jusqu'au bout de la passerelle, pas un de plus (sinon le joueur marche sur l'eau).
        ('SSAnne_Exterior_Movement_WalkDown::\n\twalk_down\n', 'SSAnne_Exterior_Movement_WalkDown::\n'),
        ('setvar VAR_MAP_SCENE_VERMILION_CITY, 2', 'setvar VAR_MAP_SCENE_VERMILION_CITY, 3'),
        ('warp MAP_VERMILION_CITY, 23, 34', 'warp MAP_VERMILION_CITY_PORT_OUTSIDE, 15, 9'),
    ],
}
