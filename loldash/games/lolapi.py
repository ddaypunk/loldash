__author__ = 'andydelso'


from helpers.lolapi import make_request
from games.models import Game, GamePlayer, GameStat


def get_games_by_summoner_id(summoner_id, region='na', version='v1.3'):

    """
    :param summoner_id: summoner id from summoners table
    :param region: region of player
    :param version: version of the api, default 1.3
    :return: list containing game data for push to DB
    """

    endpoint = 'game/by-summoner/' + str(summoner_id) + '/recent'

    api_request_json = make_request(endpoint, version, region)

    # create a list for the games in the json
    games_list = []

    for json_game in api_request_json['games']:

        game_elements = []

        # parse game json into Game object and save to list
        new_game = Game(
            id=json_game.get('gameId'),
            create_date=json_game.get('createDate'),
            game_mode=json_game.get('gameMode'),
            game_type=json_game.get('gameType'),
            sub_type=json_game.get('subType'),
            map_id=json_game.get('mapId'),
            invalid=json_game.get('invalid')
        )

        game_elements.append(new_game)

        # parse game json into stats object and save to list
        stat_block = json_game.get('stats')

        new_game_stats = GameStat(
            game=json_game.get('gameId'),
            summoner=api_request_json.get('summonerId'),
            game_level=json_game.get('level'),
            spell_1_id=json_game.get('spell1'),
            spell_2_id=json_game.get('spell2'),
            ip_earned=json_game.get('ipEarned'),
            assists=stat_block.get('assists'),
            barracks_killed=stat_block.get('barracksKilled'),
            champions_killed=stat_block.get('championsKilled'),
            combat_player_score=stat_block.get('combatPlayerScore'),
            consumables_purchased=stat_block.get('consumablesPurchased'),
            damage_dealt_player=stat_block.get('damageDealtPlayer'),
            double_kills=stat_block.get('doubleKills'),
            first_blood=stat_block.get('firstBlood'),
            gold=stat_block.get('gold'),
            gold_earned=stat_block.get('goldEarned'),
            gold_spent=stat_block.get('goldSpent'),
            item_0=stat_block.get('item0'),
            item_1=stat_block.get('item1'),
            item_2=stat_block.get('item2'),
            item_3=stat_block.get('item3'),
            item_4=stat_block.get('item4'),
            item_5=stat_block.get('item5'),
            item_6=stat_block.get('item6'),
            items_purchased=stat_block.get('itemsPurchased'),
            killing_sprees=stat_block.get('killingSprees'),
            largest_critical_strike=stat_block.get('largestCriticalStrike'),
            largest_killing_spree=stat_block.get('largestKillingSpree'),
            largest_multi_kill=stat_block.get('largestMultiKill'),
            legendary_items_created=stat_block.get('legendaryItemsCreated'),
            stat_level=stat_block.get('level'),
            magic_damage_dealt_player=stat_block.get('magicDamageDealtPlayer'),
            magic_damage_dealt_to_champions=stat_block.get('magicDamageDealtToChampions'),
            magic_damage_taken=stat_block.get('magicDamageTaken'),
            minions_denied=stat_block.get('minionsDenied'),
            minions_killed=stat_block.get('minionsKilled'),
            neutral_minions_killed=stat_block.get('neutralMinionsKilled'),
            netural_minions_killed_enemy_jungle=stat_block.get('neutralMinionsKilledEnemyJungle'),
            neutral_minions_killed_your_jungle=stat_block.get('neutralMinionsKilledYourJungle'),
            nexus_killed=stat_block.get('nexusKilled'),
            node_capture=stat_block.get('nodeCapture'),
            node_capture_assist=stat_block.get('nodeCaptureAssist'),
            node_neutralize=stat_block.get('nodeNeutralize'),
            node_neutralize_assist=stat_block.get('nodeNeutralizeAssist'),
            num_deaths=stat_block.get('numDeaths'),
            num_items_bought=stat_block.get('numItemsBought'),
            objective_player_score=stat_block.get('objectivePlayerScore'),
            penta_kills=stat_block.get('pentaKills'),
            physical_damage_dealt_player=stat_block.get('physicalDamageDealtPlayer'),
            physical_damage_dealt_to_champions=stat_block.get('physicalDamageDealtToChampions'),
            physical_damage_taken=stat_block.get('physicalDamageTaken'),
            quadra_kills=stat_block.get('quadraKills'),
            sight_wards_bought=stat_block.get('sightWardsBought'),
            spell_1_cast=stat_block.get('spell1Cast'),
            spell_2_cast=stat_block.get('spell2Cast'),
            spell_3_cast=stat_block.get('spell3Cast'),
            spell_4_cast=stat_block.get('spell4Cast'),
            summon_spell_1_cast=stat_block.get('summonSpell1Cast'),
            summon_spell_2_cast=stat_block.get('summonSpell2Cast'),
            super_monster_killed=stat_block.get('superMonsterKilled'),
            team=stat_block.get('team'),
            team_objective=stat_block.get('teamObjective'),
            time_played=stat_block.get('timePlayed'),
            total_damage_dealt=stat_block.get('totalDamageDealt'),
            total_damage_dealt_to_champions=stat_block.get('totalDamageDealtToChampions'),
            total_damage_taken=stat_block.get('totalDamageTaken'),
            total_heal=stat_block.get('totalHeal'),
            total_player_score=stat_block.get('totalPlayerScore'),
            total_score_rank=stat_block.get('totalScoreRank'),
            total_time_crowd_control_dealt=stat_block.get('totalTimeCrowdControlDealt'),
            total_units_healed=stat_block.get('totalUnitsHealed'),
            triple_kills=stat_block.get('tripleKills'),
            true_damage_dealt_player=stat_block.get('trueDamageDealtPlayer'),
            true_damage_dealt_to_champions=stat_block.get('trueDamageDealtToChampions'),
            true_damage_taken=stat_block.get('trueDamageTaken'),
            turrets_killed=stat_block.get('turretsKilled'),
            unreal_kills=stat_block.get('unrealKills'),
            victory_point_total=stat_block.get('victoryPointTotal'),
            vision_wards_bought=stat_block.get('visionWardsBought'),
            ward_killed=stat_block.get('wardKilled'),
            ward_placed=stat_block.get('wardPlaced'),
            win=stat_block.get('win')
        )

        game_elements.append(new_game_stats)

        # parse game json into GamePlayer object and save to list
        game_players = []

        # don't forget the summoner is a player
        summoner_player = GamePlayer(
            game=new_game.id,
            summoner=api_request_json.get('summonerId'),
            champion_id=json_game.get('championId'),
            team_id=json_game.get('teamId')
        )

        game_players.append(summoner_player)

        for each_player in json_game.get('fellowPlayers'):
            new_fellow_player = GamePlayer(
                game=new_game.id,
                summoner=each_player.get('summonerId'),
                champion_id=each_player.get('championId'),
                team_id=each_player.get('teamId')
            )
            game_players.append(new_fellow_player)

        game_elements.append(game_players)

        # save objects list into the list of up to 10 games
        games_list.append(game_elements)

    return games_list