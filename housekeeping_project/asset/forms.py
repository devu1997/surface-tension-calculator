from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.db.models import Q
from asset.models import *


class SurfaceTensionForm(forms.ModelForm):
	class Meta:
		model = SurfaceTension
		fields = ['angle','liquid','solid']

	def __init__(self, *args, **kwargs):
		super(SurfaceTensionForm, self).__init__(*args, **kwargs)
				
		self.fields['angle'].label = 'Contact Angle'
		self.fields['angle'].widget.attrs.update({
				'placeholder': 'Contact Angle',
				'class': 'form-control',
			})

		self.fields['liquid'].label = 'Choose Liquid'
		self.fields['liquid'].widget.attrs.update({
				'class': 'single-select-input',
			})

		self.fields['solid'].label = 'Choose Solid'
		self.fields['solid'].widget.attrs.update({
				'class': 'single-select-input',
			})


class SolidEnergyForm(forms.ModelForm):
	class Meta:
		model = SolidEnergy
		fields = ['name','energy']

	def __init__(self, *args, **kwargs):
		super(SolidEnergyForm, self).__init__(*args, **kwargs)
				
		self.fields['name'].label = 'Solid Name'
		self.fields['name'].widget.attrs.update({
				'placeholder': 'Solid Name',
				'class': 'form-control',
			})

		self.fields['energy'].label = 'Surface Energy'
		self.fields['energy'].widget.attrs.update({
				'placeholder': 'Surface Energy',
				'class': 'form-control',
			})


class LiquidEnergyForm(forms.ModelForm):
	class Meta:
		model = LiquidEnergy
		fields = ['name','energy']

	def __init__(self, *args, **kwargs):
		super(LiquidEnergyForm, self).__init__(*args, **kwargs)
				
		self.fields['name'].label = 'Liquid Name'
		self.fields['name'].widget.attrs.update({
				'placeholder': 'Liquid Name',
				'class': 'form-control',
			})

		self.fields['energy'].label = 'Surface Energy'
		self.fields['energy'].widget.attrs.update({
				'placeholder': 'Surface Energy',
				'class': 'form-control',
			})
