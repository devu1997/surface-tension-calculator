# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render,redirect
from django.db import transaction
from django.utils import timezone
from asset.forms import *

def addTask(request):
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('assetAll')
	else:
		form = TaskForm()

	context = {
		'taskForm':form,
	}

	return render(request, 'addTask.html', context)


def addAsset(request):
	if request.method == 'POST':
		form = AssetForm(request.POST)
		if form.is_valid():
			form.save()			
			return redirect('assetAll')
	else:
		form = AssetForm()

	context = {
		'assetForm':form,
	}

	return render(request, 'addAsset.html', context)


def addWorker(request):
	if request.method == 'POST':
		form = WorkerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('assetAll')
	else:
		form = WorkerForm()

	context = {
		'workerForm':form,
	}

	return render(request, 'addWorker.html', context)


def assetAll(request):
	assets = Asset.objects.all()

	context = {
		'assets':assets,
	}
	
	return render(request, 'assetAll.html',context)


def allocateTask(request):
	if request.method == 'POST':
		form = AllocateForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('assetAll')
	else:
		form = AllocateForm()

	context = {
		'allocateForm':form,
	}

	return render(request, 'allocateTask.html', context)


def getTasksForWorker(request,workerId=None):
	context = {
		'search':False,
	}

	if request.GET.get('workerId') or workerId is not None:
		if workerId is None:
			workerId = request.GET['workerId']
		alloctedTasks = Allocate.objects.filter(worker__workerId=workerId)
		context.update({
			'search': True,
			'alloctedTasks': alloctedTasks,
			})

	return render(request, 'getTasksForWorker.html',context)