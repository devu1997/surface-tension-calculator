# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Asset(models.Model):
	assetId = models.CharField(max_length=100,primary_key=True)
	name = models.CharField(max_length=100)

	def __str__(self):
		return '%s' % (self.name)


class Task(models.Model):
	taskId = models.CharField(max_length=100,primary_key=True)
	name = models.CharField(max_length=100)

	def __str__(self):
		return '%s' % (self.name)


class Worker(models.Model):
	workerId =  models.CharField(max_length=100,primary_key=True)
	name = models.CharField(max_length=100)

	def __str__(self):
		return '%s' % (self.name)


class Allocate(models.Model):
	asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
	timeOfAllocation = models.DateTimeField()
	taskToBePerformedBy = models.DateTimeField()

	def __str__(self):
		return '%s' % (self.name)