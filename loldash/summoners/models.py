from django.db import models


class Summoner(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    profile_icon_id = models.IntegerField()
    summoner_level = models.IntegerField()
    revision_date = models.DateField()

    class Meta:
        db_table = 'summoners'
