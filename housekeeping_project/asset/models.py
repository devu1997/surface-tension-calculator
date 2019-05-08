# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from decimal import Decimal

# Create your models here.

class LiquidEnergy(models.Model):
	energy = models.DecimalField(default=0,decimal_places=2,max_digits=4)
	name = models.CharField(max_length=100)

	def __str__(self):
		return '%s' % (self.name)

class SolidEnergy(models.Model):
	energy = models.DecimalField(default=0,decimal_places=2,max_digits=4)
	name = models.CharField(max_length=100)

	def __str__(self):
		return '%s' % (self.name)

class SurfaceTension(models.Model):
	angle = models.IntegerField()
	liquid = models.ForeignKey(LiquidEnergy, on_delete=models.CASCADE)
	solid = models.ForeignKey(SolidEnergy, on_delete=models.CASCADE)

	def __str__(self):
		return '%s' % (self.name)
