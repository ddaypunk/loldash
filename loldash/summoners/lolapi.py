__author__ = 'andydelso'

from helpers.lolapi import make_request

from summoners.models import Summoner, SummonerStats


def get_summoner_by_name(summoner_name, region, version='v1.4'):

    """
    :param summoner_name: summoner name - not sure where from yet
    :param region: region of player
    :param version: version of the api, default 1.4
    :return: summoner object
    """

    endpoint = 'summoner/by-name/' + str(summoner_name)

    api_request_json = make_request(endpoint, version, region)

    # parse json into new Summoner object
    summoner = Summoner(
        id=api_request_json['id'],
        name=api_request_json['name'],
        profile_icon_id=api_request_json['profileIconId'],
        revision_date=api_request_json['revisionDate'],
        summoner_level=api_request_json['summonerLevel']
    )

    return summoner

def get_stats_summary_by_id(summoner_id, region='na', version='v1.3'):

    """
    :param summoner_id: summoner id from summoners table
    :param region: region of player
    :param version: version of the api, default 1.3
    :return: list of summoner stats object
    """

    endpoint = 'stats/by-summoner/' + str(summoner_id) + '/summary'
    summoner_stat_list = []

    api_request_json = make_request(endpoint, version, region)

    # parse json into new SummonerStats object

    for json_stat_header in api_request_json['playerStatSummaries']:
        aggregated_stats = json_stat_header['aggregatedStats']

        summoner_stat = SummonerStats(
            # .get will return None if key does not exist, should put NULL in DB
            id=summoner_id,
            player_stat_summary_type=json_stat_header.get('playerStatSummaryType'),
            wins=json_stat_header.get('wins'),
            losses=json_stat_header.get('losses'),
            modify_date=json_stat_header.get('modifyDate'),
            avg_assists=aggregated_stats.get('averageAssists'),
            avg_champions_kille=aggregated_stats.get('averageChampionsKilled'),
            avg_assist=aggregated_stats.get('averageAssists'),
            avg_combat_player_score=aggregated_stats.get('averageCombatPlayerScore'),
            avg_node_capture=aggregated_stats.get('averageNodeCapture'),
            avg_node_capture_assist=aggregated_stats.get('averageNodeCaptureAssist'),
            avg_node_neutralize=aggregated_stats.get('averageNodeNeutralize'),
            avg_node_neutralize_assist=aggregated_stats.get('averageNodeNeutralizeAssist'),
            avg_num_deaths=aggregated_stats.get('averageNumDeaths'),
            avg_objective_player_score=aggregated_stats.get('averageObjectivePlayerScore'),
            avg_team_objective=aggregated_stats.get('averageTeamObjective'),
            avg_total_player_score=aggregated_stats.get('averageTotalPlayerScore'),
            max_assists=aggregated_stats.get('maxAssists'),
            max_combat_player_score=aggregated_stats.get('maxCombatPlayerScore'),
            max_node_capture=aggregated_stats.get('maxNodeCapture'),
            max_node_capture_assist=aggregated_stats.get('maxNodeCaptureAssist'),
            max_node_neutralize=aggregated_stats.get('maxNodeNeutralize'),
            max_node_neutralize_assist=aggregated_stats.get('maxNodeNeutralizeAssist'),
            max_objective_player_score=aggregated_stats.get('maxObjectivePlayerScore'),
            max_team_objective=aggregated_stats.get('maxTeamObjective'),
            max_total_player_score=aggregated_stats.get('maxTotalPlayerScore'),
            total_node_capture=aggregated_stats.get('maxTotalNodeCapture'),
            total_node_neutralize=aggregated_stats.get('maxTotalNodeNeutralize'),
            max_num_deaths=aggregated_stats.get('maxNumDeaths'),
            total_deaths_per_session=aggregated_stats.get('totalDeathsPerSession'),
            bot_games_played=aggregated_stats.get('botGamesPlayed'),
            killing_spree=aggregated_stats.get('killingSpree'),
            max_champion_kills=aggregated_stats.get('maxChampionsKilled'),
            max_largest_critical_strike=aggregated_stats.get('maxLargestCriticalStrike'),
            max_largest_killing_spree=aggregated_stats.get('maxLargestKillingSpree'),
            max_time_played=aggregated_stats.get('maxTimePlayed'),
            max_time_spent_living=aggregated_stats.get('maxTimeSpentLiving'),
            most_champion_kills_per_session=aggregated_stats.get('mostChampionKillsPerSession'),
            most_spells_cast=aggregated_stats.get('mostSpellsCast'),
            normal_games_played=aggregated_stats.get('normalGamesPlayed'),
            ranked_premade_games_played=aggregated_stats.get('rankedPremadeGamesPlayed'),
            ranked_solo_games_played=aggregated_stats.get('rankedSoloGamesPlayed'),
            total_assists=aggregated_stats.get('totalAssists'),
            total_champion_kills=aggregated_stats.get('totalChampionKills'),
            total_damage_dealt=aggregated_stats.get('totalDamageDealt'),
            total_damage_taken=aggregated_stats.get('totalDamageTaken'),
            total_double_kills=aggregated_stats.get('totalDoubleKills'),
            total_first_blood=aggregated_stats.get('totalFirstBlood'),
            total_gold_earned=aggregated_stats.get('totalGoldEarned'),
            total_heal=aggregated_stats.get('totalHeal'),
            total_magic_damage_dealt=aggregated_stats.get('totalMagicDamageDealt'),
            total_minion_kills=aggregated_stats.get('totalMinionKills'),
            total_neutral_minions_killed=aggregated_stats.get('totalNeutralMinionKills'),
            total_penta_kills=aggregated_stats.get('totalPentaKills'),
            total_physical_damage_dealt=aggregated_stats.get('totalPhysicalDamageDealt'),
            total_quadra_kills=aggregated_stats.get('totalQuadraKills'),
            total_sessions_lost=aggregated_stats.get('totalSessionsLost'),
            total_sessions_played=aggregated_stats.get('totalSessionsPlayed'),
            total_sessions_won=aggregated_stats.get('totalSessionsWon'),
            total_triple_kills=aggregated_stats.get('totalTripleKills'),
            total_turrets_killed=aggregated_stats.get('totalTurretsKilled'),
            total_unreal_kills=aggregated_stats.get('totalUnrealKills')
        )

    summoner_stat_list.append(summoner_stat)

    return summoner_stat_list