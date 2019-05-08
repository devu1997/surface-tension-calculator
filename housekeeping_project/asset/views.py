# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render,redirect
from django.db import transaction
from django.utils import timezone
from asset.forms import *
from asset.models import *
import math

def getSurfaceTension(request):
    context = {}

    if request.method == 'POST':
        form = SurfaceTensionForm(request.POST)
        if form.is_valid():
            angle = form.instance.angle
            solid = form.instance.solid
            liquid = form.instance.liquid
            context['surfaceTension'] = float(solid.energy) - (float(liquid.energy) * math.cos(angle))
    else:
        form = SurfaceTensionForm()

    context['form'] = form
    return render(request, 'surfaceTension.html', context)

def addSolid(request):
	if request.method == 'POST':
		form = SolidEnergyForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('addSolid')
	else:
		form = SolidEnergyForm()

	context = {
		'form':form,
	}

	return render(request, 'addSolid.html', context)


def addLiquid(request):
	if request.method == 'POST':
		form = LiquidEnergyForm(request.POST)
		if form.is_valid():
			form.save()			
			return redirect('addLiquid')
	else:
		form = LiquidEnergyForm()

	context = {
		'form':form,
	}

	return render(request, 'addLiquid.html', context)


def solidAll(request):
	solids = SolidEnergy.objects.all()

	context = {
		'solids':solids,
	}
	
	return render(request, 'solidsAll.html',context)


def liquidAll(request):
	liquids = LiquidEnergy.objects.all()

	context = {
		'liquids':liquids,
	}
	
	return render(request, 'liquidsAll.html',context)


