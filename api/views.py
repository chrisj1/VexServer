# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Team, Match, IndivualTeamMatchPerformance


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def teams(request):
    return Team.objects.all()

