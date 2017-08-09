# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from api.jsonHelpers import get_json_from_URL


# Create your models here.
class Team(models.Model):
    team_number = models.CharField(max_length=10)
    organisation = models.CharField(max_length=70)
    team_name = models.CharField(max_length=70)
    robot_name = models.CharField(max_length=100)
    grade = models.BooleanField()

    def update(self):
        json = get_json_from_URL('https://api.vexdb.io/v1/get_teams?team=9228A')
        if json['size'] != 1:
            print('invalid team number')
            return
        print(json['size'])
        result = json['result'][0]
        self.organisation = result['organisation']
        self.team_name = result['team_name']
        self.robot_name = result['robot_name']
        self.grade = result['grade'] == 'High School'
        self.save()


    def __str__(self):
        return "team_number: %s, organisation: %s, team_name: %s, robot_name %s, grade %s".format(
            self.team_number, self.organisation, self.team_name, self.robot_name, self.grade)


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
    match = models.ForeignKey(Match)

    teleop_description = models.CharField(max_length=700)
    cones_on_goal = models.IntegerField()
    mobile_goals_scored_in_5 = models.IntegerField()
    mobile_goals_scored_in_10 = models.IntegerField()
    mobile_goals_scored_in_20 = models.IntegerField()
    robot_parks = models.BooleanField()

    penalties = models.IntegerField()
    penalties_point_deductions = models.IntegerField()

    autonomous_description=models.CharField(max_length=700)
    autonomous_points=models.IntegerField()
    autonomous_cones_stacked=models.IntegerField()
    autonomous_mobile_goals_scored_in_5 = models.IntegerField()
    autonomous_mobile_goals_scored_in_10 = models.IntegerField()
    autonomous_mobile_goals_scored_in_20 = models.IntegerField()
    higest_stack_in_5 = models.IntegerField()
    higest_stack_in_10 = models.IntegerField()
    higest_stack_in_20 = models.IntegerField()
