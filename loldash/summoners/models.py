from django.db import models

class Summoner(models.Model):
    ###############
    # SummonerDto #
    ###############

    # Status Codes
    # 400    Bad Request
    # 401    Unauthorized
    # 404    No summoner data found for and specified inputs
    # 429    Rate limit exceeded
    # 500    Internal server error
    # 503    Service Unavailable

    # summonerid    long    Summoner ID.
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # name    string    Summoner Name.
    name = models.CharField(max_length=100)

    # profileIconId    int    ID of the summoner icon assoc. with the summoner
    profile_icon_id = models.IntegerField()

    # summmonerLevel    long    Summoner Level associated with the summoner
    summoner_level = models.IntegerField()

    # revisionDate    long    Date summoner was last modified specified as epoch milliseconds
    revision_date = models.IntegerField()

    class Meta:
        db_table = 'summoners'



class StatSummaryType(object):
    ARAM_UNRANKED_5x5 = ('ARAM Unranked 5x5', 'ARAM_UNRANKED_5x5')
    COOP_VS_AI = ('Co-op Vs AI', 'COOP_VS_AI')
    COOP_VS_AI_3x3 = ('Co-op Vs AI 3x3', 'COOP_VS_AI_3x3')
    ODIN_UNRANKED = ('Odin Unranked', 'ODIN_UNRANKED')
    RANKED_PREMADE_3x3 = ('Ranked Premade 3x3', 'RANKED_PREMADE_3x3')
    RANKED_PREMADE_5x5 = ('Ranked Premade 5x5', 'RANKED_PREMADE_5x5')
    RANKED_SOLO_5x5 = ('Ranked Solo 5x5', 'RANKED_SOLO_5x5')
    RANKED_TEAM_3x3 = ('Ranked Team 3x3', 'RANKED_TEAM_3x3')
    RANKED_TEAM_5x5 = ('Ranked Team 5x5', 'RANKED_TEAM_5x5')
    UNRANKED = ('Unranked', 'UNRANKED')
    UNRANKED_3x3 = ('Unranked 3x3', 'UNRANKED_3x3')
    ONE_FOR_ALL_5x5 = ('One For All 5x5', 'ONEFORALL_5x5')
    FIRST_BLOOD_1x1 = ('First Blood 1x1', 'FIRSTBLOOD_1x1')
    FIRST_BLOOD_2x2 = ('First Blood 2x2', 'FIRSTBLOOD_2x2')
    SR_6x6 = ('SR 6x6', 'SR_6x6')
    CAP_5x5 = ('Cap 5x5', 'CAP_5x5')
    URF = ('URF', 'URF')
    URF_BOT = ('URF Bot', 'URF_BOT')
    NIGHTMARE_BOT = ('Nightmare Bot', 'NIGHTMARE_BOT')

    choices = (ARAM_UNRANKED_5x5, COOP_VS_AI, COOP_VS_AI_3x3, ODIN_UNRANKED, RANKED_PREMADE_3x3, 
        RANKED_PREMADE_5x5, RANKED_SOLO_5x5, RANKED_TEAM_3x3, RANKED_TEAM_5x5, UNRANKED, UNRANKED_3x3,
        ONE_FOR_ALL_5x5, FIRST_BLOOD_1x1, FIRST_BLOOD_2x2, SR_6x6, CAP_5x5, URF, URF_BOT, NIGHTMARE_BOT)



class SummonerStats(models.Model):

    # Status Codes
    # 400    Bad Request
    # 401    Unauthorized
    # 404    Stats data not found
    # 429    Rate limit exceeded
    # 500    Internal server error
    # 503    Service Unavailable

    id = models.AutoField(primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    #############################
    # PlayerStatsSummaryListDto #
    #############################
    
    # summonerId    long    Summoner ID.
    summoner = models.ForeignKey(Summoner, related_name='summoner_stats')

    #a new row will need to be created for each in list playerStatSummaries
    #stats are based on game modes and has a list entry for each
    
    #########################
    # PlayerStatsSummaryDto #
    #########################

    # losses    int    Number of loses for this queue type
    # Return for rankded queue types only
    losses = models.IntegerField(null=True)

    #modifyDate    long    Date stats were last modified specified as epoch milliseconds
    modify_date = models.IntegerField()

    # playerStatSummaryType   string    Payer stats summary type.
    # (legal values: ARAM_UNRANKED_5x5, COOP_VS_AI, COOP_VS_AI_3x3, ODIN_UNRANKED, RANKED_PREMADE_3x3, 
    #   RANKED_PREMADE_5x5, RANKED_SOLO_5x5, RANKED_TEAM_3x3, RANKED_TEAM_5x5, UNRANKED, UNRANKED_3x3,
    #   ONE_FOR_ALL_5x5, FIRST_BLOOD_1x1, FIRST_BLOOD_2x2, SR_6x6, CAP_5x5, URF, URF_BOT, NIGHTMARE_BOT
    player_stat_summary_type = models.CharField(max_length=50, choices=StatSummaryType.choices)
    
    # wins    int    Number of wins for this queue type.
    wins = models.IntegerField(null=True)

    ######################
    # AggregatedStatsDto #
    ######################


    ### Dominion Only Stat Fields ###
    # averageAssists    int    Dominion only.
    avg_assists = models.IntegerField(null=True)

    # averageChampionsKilled    int    Dominion only.
    avg_champions_killed = models.IntegerField(null=True)

    # averageCombatPlayerScore    int    Dominion only.
    avg_combat_player_score = models.IntegerField(null=True)

    # averageNodeCaptures    int    Dominion only.
    avg_node_capture = models.IntegerField(null=True)

    # averageNodeCaptureAssist    int    Dominion only.
    avg_node_capture_assist = models.IntegerField(null=True)

    # averageNodeNeutralize    int    Dominion only.
    avg_node_neutralize = models.IntegerField(null=True)

    # averageNodeNeutralizeAssist    int    Dominion only.
    avg_node_neutralize_assist = models.IntegerField(null=True)

    # averageNumDeaths    int    Dominion only.
    avg_num_deaths = models.IntegerField(null=True)

    # averageObjectivePlayerScore    int    Dominion only.
    avg_objective_player_score = models.IntegerField(null=True)

    # averageTeamObjective    int    Dominion only.
    avg_team_objective = models.IntegerField(null=True)

    # averageTotalPlayerScore    int    Dominion only.
    avg_total_player_score = models.IntegerField(null=True)

    # maxAssists    int    Dominion only.
    max_assists = models.IntegerField(null=True)

    # maxCombatPlayerScore    int    Dominion only.
    max_combat_player_score = models.IntegerField(null=True)

    # maxNodeCaptureScore    int    Dominion only.
    max_node_capture = models.IntegerField(null=True)

    # maxNodeCaptureAssist    int    Dominion only.
    max_node_capture_assist = models.IntegerField(null=True)
    
    # maxNodeNeutralize    int    Dominion only.
    max_node_neutralize = models.IntegerField(null=True)

    # maxNodeNeutralizeAssist    int    Dominion only.
    max_node_neutralize_assist = models.IntegerField(null=True)

    # maxObjectivePlayerScore    int    Dominion only.
    max_objective_player_score = models.IntegerField(null=True)

    # maxTeamObjective    int    Dominion only.
    max_team_objective = models.IntegerField(null=True)

    # maxTotalPlayerScore    int    Dominion only.
    max_total_player_score = models.IntegerField(null=True)

    # totalNodeCapture    int    Dominion only.
    total_node_capture = models.IntegerField(null=True)

    # totalNodeNeutralize    int    Dominion only.
    total_node_neutralize = models.IntegerField(null=True)


    ### Ranked Only Stat Fields ###
    # maxNumDeaths    int    Only returned for ranked statistics
    max_num_deaths = models.IntegerField(null=True)

    # totalDeathsPerSession    int    Only returned for ranked statistics
    total_deaths_per_session = models.IntegerField(null=True)


    ### General Stat Fields ###
    # botGamesPlayed    int
    bot_games_played = models.IntegerField(null=True)

    # killingSpree    int
    killing_spree = models.IntegerField(null=True)

    # maxChampionsKilled    int
    max_champion_kills = models.IntegerField(null=True)

    # maxLargestCriticalStrike    int
    max_largest_critical_strike = models.IntegerField(null=True)

    # maxLargestKillingSpree    int
    max_largest_killing_spree = models.IntegerField(null=True)

    # maxTimePlayed    int
    max_time_played = models.IntegerField(null=True)

    # maxTimeSpentLiving    int
    max_time_spent_living = models.IntegerField(null=True)

    # mostChampionKillsPerSession    int
    most_champion_kills_per_session = models.IntegerField(null=True)

    # mostSpellsCast   int
    most_spells_cast = models.IntegerField(null=True)

    # normalGamesPlayed    int
    normal_games_played = models.IntegerField(null=True)

    # rankedPremageGamesPlayed    int
    ranked_premade_games_played = models.IntegerField(null=True)

    # rankedSoloGamesPlayed   int
    ranked_solo_games_played = models.IntegerField(null=True)

    # totalAssists    int
    total_assists = models.IntegerField(null=True)

    # totalChampionKills    int
    total_champion_kills = models.IntegerField(null=True)

    # totalDamageDealt    int
    total_damage_dealt = models.IntegerField(null=True)

    # totalDamageTaken    int
    total_damage_taken = models.IntegerField(null=True)

    # totalDoubleKIlls    int
    total_double_kills = models.IntegerField(null=True)

    # totalFirstBlood    int
    total_first_blood = models.IntegerField(null=True)

    # totalGoldEarned    int
    total_gold_earned = models.IntegerField(null=True)

    # totalHeal    int
    total_heal = models.IntegerField(null=True)

    # totalMagicDamageDealt    int
    total_magic_damage_dealt = models.IntegerField(null=True)

    # totalMinionKills    int
    total_minion_kills = models.IntegerField(null=True)

    # totalNeutralMinionsKilled    int
    total_neutral_minions_killed = models.IntegerField(null=True)

    # totalPentaKills    int
    total_penta_kills = models.IntegerField(null=True)

    # totalPhysicalDamageDealt    int
    total_physical_damage_dealt = models.IntegerField(null=True)

    # totalQuadraKills    int
    total_quadra_kills = models.IntegerField(null=True)

    # totalSessionsLost    int
    total_sessions_lost = models.IntegerField(null=True)

    # totalSessionsPlayed    int
    total_sessions_played = models.IntegerField(null=True)

    # totalSessionsWon    int
    total_sessions_won = models.IntegerField(null=True)

    # totalTripleKills    int
    total_triple_kills = models.IntegerField(null=True)

    # totalTurretsKilled    int
    total_turrets_killed = models.IntegerField(null=True)

    # totalUnrealKills    int
    total_unreal_kills = models.IntegerField(null=True)



    class Meta:
        db_table = 'summoner_stats'