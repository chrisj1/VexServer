# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests


from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Team, Match, IndivualTeamMatchPerformance


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def teams(request):
    return Team.objects.all()


def events(request):
    r = requests.get('https://api.vexdb.io/v1/get_teams?team=2915A')

    print(r.json())

    return HttpResponse(r.text)

