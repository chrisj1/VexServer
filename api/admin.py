# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import IndivualTeamMatchPerformance,Match,Team

# Register your models here.
admin.site.register(IndivualTeamMatchPerformance)
admin.site.register(Match)
admin.site.register(Team)