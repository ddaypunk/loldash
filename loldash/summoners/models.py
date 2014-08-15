from django.db import models

#Summoner model for pulls from the api
class Summoner(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    profile_icon_id = models.IntegerField()
    summoner_level = models.IntegerField()
    revision_date = models.DateField()

    class Meta:
        db_table = 'summoners'

#Stats model for pulls from the api
class Stats(models.Model):
	id = models.IntegerField(primary_key=True)
	summoner_id = models.ForeignKey(Summoner, related_name='stats') 
	losses = models.IntegerField()
	modify_date = models.DateField()
	player_stat_summary_type = models.CharField(max_length=25)
	avg_assists = models.IntegerField() #dominion only
	avg_champions_killed = models.IntegerField() #dominion only
	avg_combat_player_score = models.IntegerField() #dominion only
	avg_node_capture = models.IntegerField() #dominion only
	avg_node_capture_assist = models.IntegerField() #dominion only
	avg_node_neutralize = models.IntegerField() #dominion only
	avg_node_neutralize_assist = models.IntegerField() #dominion only
	avg_num_deaths = models.IntegerField() #dominion only
	avg_objective_player_score = models.IntegerField() #dominion only
	avg_team_objective = models.IntegerField() #dominion only
	avg_total_player_score = models.IntegerField() #dominion only
	bot_games_played = models.IntegerField()
	killing_spree = models.IntegerField()
	max_assists = models.IntegerField() #dominion only
	max_champion_kills = models.IntegerField()
	max_combat_player_score = models.IntegerField() #dominion only
	max_largest_critical_strike = models.IntegerField()
	max_largest_killing_spree = models.IntegerField()
	max_node_capture = models.IntegerField() #dominion only
	max_node_capture_assist = models.IntegerField() #dominion only
	max_node_neutralize = models.IntegerField() #dominion only
	max_node_neutralize_assist = models.IntegerField() #dominion only
	max_num_deaths = models.IntegerField() #ranked only
	max_objective_player_score = models.IntegerField() #dominion only
	max_team_objective = models.IntegerField() #dominion only
	max_time_played = models.IntegerField()
	max_time_spent_living = models.IntegerField()
	max_total_player_score = models.IntegerField() #dominion only
	most_champion_kills_per_session = models.IntegerField()
	most_spells_cast = models.IntegerField()
	normal_games_played = models.IntegerField()
	ranked_premade_games_played = models.IntegerField()
	ranked_solo_games_played = models.IntegerField()
	total_assists = models.IntegerField()
	total_champion_kills = models.IntegerField()
	total_damage_dealt = models.IntegerField()
	total_damage_taken = models.IntegerField()
	total_deaths_per_session = models.IntegerField() #ranked only
	total_double_kills = models.IntegerField()
	total_first_blood = models.IntegerField()
	total_goald_earned = models.IntegerField()
	total_heal = models.IntegerField()
	total_magic_damage_dealt = models.IntegerField()
	total_minion_kills = models.IntegerField()
	total_neutral_minions_killed = models.IntegerField()
	total_node_capture = models.IntegerField() #dominion only
	total_node_neutralize = models.IntegerField() #dominion only
	total_penta_kills = models.IntegerField()
	total_physical_damage_dealt = models.IntegerField()
	total_quadra_kills = models.IntegerField()
	total_sessions_lost = models.IntegerField()
	total_sessions_played = models.IntegerField()
	total_sessions_won = models.IntegerField()
	total_triple_kills = models.IntegerField()
	total_turrets_killed = models.IntegerField()
	total_unreal_kills = models.IntegerField()

	class Meta:
		db_table = 'stats'