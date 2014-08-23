from django.db import models

from summoners.models import Summoner


class GameMode(object):
    CLASSIC = ('Classic', 'CLASSIC')
    ODIN = ('Odin', 'ODIN')
    ARAM = ('ARAM', 'ARAM')
    TUTORIAL = ('Tutorial', 'TUTORIAL')
    ONE_FOR_ALL = ('One For All', 'ONEFORALL')
    FIRST_BLOOD = ('First Blood', 'FIRSTBLOOD')

    choices = (CLASSIC, ODIN, ARAM, TUTORIAL, ONE_FOR_ALL, FIRST_BLOOD,)


class GameType(object):
    CUSTOM_GAME = ('Custom Game', 'CUSTOM_GAME')
    MATCHED_GAME = ('Matched Game', 'MATCHED_GAME')
    TUTORIAL_GAME = ('Tutorial Game', 'TUTORIAL_GAME')

    choices = (CUSTOM_GAME, MATCHED_GAME, TUTORIAL_GAME,)


class GameSubType(object):
    NORMAL = ('Normal', 'NORMAL')
    BOT = ('Bot', 'BOT')
    RANKED_SOLO_5x5 = ('Ranked Solo 5x5', 'RANKED_SOLO_5x5')
    RANKED_PREMADE_3x3 = ('Ranked Premade 3x3', 'RANKED_PREMADE_3x3')
    RANKED_PREMADE_5x5 = ('Ranked Premade 5x5', 'RANKED_PREMADE_5x5')
    ODIN_UNRANKED = ('Odin Unranked', 'ODIN_UNRANKED')
    RANKED_TEAM_3x3 = ('Ranked Team 3x3', 'RANKED_TEAM_3x3')
    RANKED_TEAM_5x5 = ('Ranked Team 5x5', 'RANKED_TEAM_5x5')
    NORMAL_3x3 = ('Normal 3x3', 'NORMAL_3x3')
    BOT_3x3 = ('Bot 3x3', 'BOT_3x3')
    CAP_5x5 = ('Cap 5x5', 'CAP_5x5')
    ARAM_UNRANKED_5x5 = ('ARAM Unranked 5x5', 'ARAM_UNRANKED_5x5')
    ONE_FOR_ALL_5x5 = ('One For All 5x5', 'ONEFORALL_5x5')
    FIRST_BLOOD_1x1 = ('First Blood 1x1', 'FIRSTBLOOD_1x1')
    FIRST_BLOOD_2x2 = ('First Blood 2x2', 'FIRSTBLOOD_2x2')
    SR_6x6 = ('SR 6x6', 'SR_6x6')
    URF = ('URF', 'URF')
    URF_BOT = ('URF Bot', 'URF_BOT')
    NIGHTMARE_BOT = ('Nightmare Bot', 'NIGHTMARE_BOT')

    choices = (NORMAL, BOT, RANKED_SOLO_5x5, RANKED_PREMADE_3x3, RANKED_PREMADE_5x5, ODIN_UNRANKED, RANKED_TEAM_3x3,
               RANKED_TEAM_5x5, NORMAL_3x3, BOT_3x3, CAP_5x5, ARAM_UNRANKED_5x5, ONE_FOR_ALL_5x5, FIRST_BLOOD_1x1,
               FIRST_BLOOD_2x2, SR_6x6, URF, URF_BOT, NIGHTMARE_BOT,)


class Team(object):
    BLUE_TEAM = 'Blue Team'
    PURPLE_TEAM = 'Purple Team'

    choices = (
        (BLUE_TEAM, 100),
        (PURPLE_TEAM, 200),
    )


class Game(models.Model):
    ###########
    # GameDto #
    ###########

    # gameId    long    Game ID.
    id = models.IntegerField(primary_key=True)

    # createDate    long    Date that end game data was recorded, specified as epoch milliseconds.
    create_date = models.IntegerField()

    # gameMode  string  Game mode.
    # (legal values: CLASSIC, ODIN, ARAM, TUTORIAL, ONEFORALL, FIRSTBLOOD)
    game_mode = models.CharField(max_length=50, choices=GameMode.choices)

    # gameType  string  Game type.
    # (legal values: CUSTOM_GAME, MATCHED_GAME, TUTORIAL_GAME)
    game_type = models.CharField(max_length=50, choices=GameType.choices)

    # subType   string  Game sub-type.
    # (legal values: NONE, NORMAL, BOT, RANKED_SOLO_5x5, RANKED_PREMADE_3x3, RANKED_PREMADE_5x5, ODIN_UNRANKED,
    #  RANKED_TEAM_3x3, RANKED_TEAM_5x5, NORMAL_3x3, BOT_3x3, CAP_5x5, ARAM_UNRANKED_5x5, ONEFORALL_5x5, FIRSTBLOOD_1x1,
    #  FIRSTBLOOD_2x2, SR_6x6, URF, URF_BOT, NIGHTMARE_BOT)
    sub_type = models.CharField(max_length=50, choices=GameSubType.choices)

    # mapId     int     Map ID.
    map_id = models.IntegerField()

    # invalid   boolean Invalid flag.
    invalid = models.BooleanField()

    class Meta:
        db_table = 'games'


class GamePlayer(models.Model):
    id = models.AutoField(primary_key=True)

    # gameId    long    Game ID.
    game = models.ForeignKey(Game, related_name='players')

    #############
    # PlayerDto #
    #############

    # summonerId    long    Summoner ID.
    summoner = models.ForeignKey(Summoner, related_name='games')

    # championId    int Champion ID associated with game.
    champion_id = models.IntegerField()

    # teamId    int     Team ID associated with game.
    # Team ID 100 is blue team. Team ID 200 is purple team.
    team_id = models.IntegerField()

    class Meta:
        db_table = 'game_players'


class GameStat(models.Model):
    id = models.AutoField(primary_key=True)

    player = models.ForeignKey(GamePlayer, related_name='game_stat')

    ###########
    # GameDto #
    ###########

    # level int Level.
    level = models.IntegerField()

    # spell1    int ID of first summoner spell.
    spell_1_id = models.IntegerField()

    # spell2    int ID of second summoner spell.
    spell_2_id = models.IntegerField()

    # ipEarned  int IP Earned.
    ip_earned = models.IntegerField()

    ###############
    # RawStatsDto #
    ###############

    # assists   int
    assists = models.IntegerField()

    # barracksKilled    int Number of enemy inhibitors killed.
    barracks_killed = models.IntegerField()

    # championsKilled   int
    champions_killed = models.IntegerField()

    # combatPlayerScore int
    combat_player_score = models.IntegerField()

    # consumablesPurchased  int
    consumables_purchased = models.IntegerField()

    # damageDealtPlayer int
    damage_dealt_player = models.IntegerField()

    # doubleKills   int
    double_kills = models.IntegerField()

    # firstBlood    int
    first_blood = models.IntegerField()

    # gold  int
    gold = models.IntegerField()

    # goldEarned    int
    gold_earned = models.IntegerField()

    # goldSpent int
    gold_spent = models.IntegerField()

    # item0 int
    item_0  = models.IntegerField()

    # item1 int
    item_1 = models.IntegerField()

    # item2 int
    item_2 = models.IntegerField()

    # item3 int
    item_3 = models.IntegerField()

    # item4 int
    item_4 = models.IntegerField()

    # item5 int
    item_5 = models.IntegerField()

    # item6 int
    item_6 = models.IntegerField()

    # itemsPurchased    int
    items_purchased = models.IntegerField()

    # killingSprees int
    killing_sprees = models.IntegerField()

    # largestCriticalStrike int
    largest_critical_strike = models.IntegerField()

    # largestKillingSpree   int
    largest_killing_spree = models.IntegerField()

    # largestMultiKill  int
    largest_multi_kill = models.IntegerField()

    # legendaryItemsCreated int Number of tier 3 items built.
    legendary_items_created = models.IntegerField()

    # level int
    level = models.IntegerField()

    # magicDamageDealtPlayer    int
    magic_damage_dealt_player = models.IntegerField()

    # magicDamageDealtToChampions   int
    magic_damage_dealt_to_champions = models.IntegerField()

    # magicDamageTaken  int
    magic_damage_taken = models.IntegerField()

    # minionsDenied int
    minions_denied = models.IntegerField()

    # minionsKilled int
    minions_killed = models.IntegerField()

    # neutralMinionsKilled  int
    neutral_minions_killed = models.IntegerField()

    # neutralMinionsKilledEnemyJungle   int
    netural_minions_killed_enemy_jungle = models.IntegerField()

    # neutralMinionsKilledYourJungle    int
    neutral_minions_killed_your_jungle = models.IntegerField()

    # nexusKilled   boolean Flag specifying if the summoner got the killing blow on the nexus.
    nexus_killed = models.BooleanField()

    # nodeCapture   int
    node_capture = models.IntegerField()

    # nodeCaptureAssist int
    node_capture_assist = models.IntegerField()

    # nodeNeutralize    int
    node_neutralize = models.IntegerField()

    # nodeNeutralizeAssist  int
    node_neutralize_assist = models.IntegerField()

    # numDeaths int
    num_deaths = models.IntegerField()

    # numItemsBought    int
    num_items_bought = models.IntegerField()

    # objectivePlayerScore  int
    objective_player_score = models.IntegerField()

    # pentaKills    int
    penta_kills = models.IntegerField()

    # physicalDamageDealtPlayer int
    physical_damage_dealt_player = models.IntegerField()

    # physicalDamageDealtToChampions    int
    physical_damage_dealt_to_champions = models.IntegerField()

    # physicalDamageTaken   int
    physical_damage_taken = models.IntegerField()

    # quadraKills   int
    quadra_kills = models.IntegerField()

    # sightWardsBought  int
    sight_wards_bought = models.IntegerField()

    # spell1Cast    int Number of times first champion spell was cast.
    spell_1_cast = models.IntegerField()

    # spell2Cast    int Number of times second champion spell was cast.
    spell_2_cast = models.IntegerField()

    # spell3Cast    int Number of times third champion spell was cast.
    spell_3_cast = models.IntegerField()

    # spell4Cast    int Number of times fourth champion spell was cast.
    spell_4_cast = models.IntegerField()

    # summonSpell1Cast  int
    summon_spell_1_cast = models.IntegerField()

    # summonSpell2Cast  int
    summon_spell_2_cast = models.IntegerField()

    # superMonsterKilled    int
    super_monster_killed = models.IntegerField()

    # team  int
    team = models.IntegerField()

    # teamObjective int
    team_objective = models.IntegerField()

    # timePlayed    int
    time_played = models.IntegerField()

    # totalDamageDealt  int
    total_damage_dealt = models.IntegerField()

    # totalDamageDealtToChampions   int
    total_damage_dealt_to_champions = models.IntegerField()

    # totalDamageTaken  int
    total_damage_taken = models.IntegerField()

    # totalHeal int
    total_heal = models.IntegerField()

    # totalPlayerScore  int
    total_player_score = models.IntegerField()

    # totalScoreRank    int
    total_score_rank = models.IntegerField()

    # totalTimeCrowdControlDealt    int
    total_time_crowd_control_dealt = models.IntegerField()

    # totalUnitsHealed  int
    total_units_healed = models.IntegerField()

    # tripleKills   int
    triple_kills = models.IntegerField()

    # trueDamageDealtPlayer int
    true_damage_dealt_player = models.IntegerField()

    # trueDamageDealtToChampions    int
    true_damage_dealt_to_champions = models.IntegerField()

    # trueDamageTaken   int
    true_damage_taken = models.IntegerField()

    # turretsKilled int
    turrets_killed = models.IntegerField()

    # unrealKills   int
    unreal_kills = models.IntegerField()

    # victoryPointTotal int
    victory_point_total = models.IntegerField()

    # visionWardsBought int
    vision_wards_bought = models.IntegerField()

    # wardKilled    int
    ward_killed = models.IntegerField()

    # wardPlaced    int
    ward_placed = models.IntegerField()

    # win   boolean Flag specifying whether or not this game was won.
    win = models.BooleanField()

    class Meta:
        db_table = 'game_stats'
