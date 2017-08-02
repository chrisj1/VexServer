# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Team(models.Model):
    team_id = models.CharField(max_length=7)


class Match(models.Model):
    red1 = models.ForeignKey(Team, related_name='red1', on_delete=models.CASCADE)
    red2 = models.ForeignKey(Team, related_name='red2', on_delete=models.CASCADE)
    blue1 = models.ForeignKey(Team, related_name='blue1', on_delete=models.CASCADE)
    blue2 = models.ForeignKey(Team, related_name='blue2', on_delete=models.CASCADE)

    red_score = models.IntegerField()
    blue_score = models.IntegerField()

    time = models.DateTimeField()


class IndivualTeamMatchPerformance(models.Model):
    team = models.ForeignKey(Team)
    cones_on_goal = models.IntegerField()
    mobile_goals_scored_in_5 = models.IntegerField()
    mobile_goals_scored_in_10 = models.IntegerField()
    mobile_goals_scored_in_20 = models.IntegerField()
    robot_parks = models.BooleanField()
    autonomous_points=models.IntegerField()

    autonomous_description=models.CharField(max_length=700)
    teleop_description=models.CharField(max_length=700)
    penalties = models.IntegerField()
    penalties_point_deductions = models.IntegerField()
