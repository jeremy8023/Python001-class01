# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MoviesInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    grade = models.IntegerField()
    short = models.CharField(max_length=400)
    score = models.FloatField()

    class Meta:
        managed = False
        db_table = 'movies_info'


class T1(models.Model):
    id = models.BigAutoField(primary_key=True)
    n_star = models.IntegerField()
    short = models.CharField(max_length=400)
    sentiment = models.FloatField()

    class Meta:
        managed = False
        db_table = 't1'
