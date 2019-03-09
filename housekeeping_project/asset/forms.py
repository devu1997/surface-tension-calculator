from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.db.models import Q
from asset.models import *


class AssetForm(forms.ModelForm):
	class Meta:
		model = Asset
		fields = ['assetId','name']

	def __init__(self, *args, **kwargs):
		super(AssetForm, self).__init__(*args, **kwargs)
				
		self.fields['assetId'].label = 'Asset ID'
		self.fields['assetId'].widget.attrs.update({
				'placeholder': 'Asset ID',
				'class': 'form-control',
			})

		self.fields['name'].label = 'Name'
		self.fields['name'].widget.attrs.update({
				'placeholder': 'Name',
				'class': 'form-control',
			})

class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['taskId','name']

	def __init__(self, *args, **kwargs):
		super(TaskForm, self).__init__(*args, **kwargs)
				
		self.fields['taskId'].label = 'Task ID'
		self.fields['taskId'].widget.attrs.update({
				'placeholder': 'Task ID',
				'class': 'form-control',
			})

		self.fields['name'].label = 'Name'
		self.fields['name'].widget.attrs.update({
				'placeholder': 'Name',
				'class': 'form-control',
			})


class WorkerForm(forms.ModelForm):
	class Meta:
		model = Worker
		fields = ['workerId','name']

	def __init__(self, *args, **kwargs):
		super(WorkerForm, self).__init__(*args, **kwargs)
				
		self.fields['workerId'].label = 'Worker ID'
		self.fields['workerId'].widget.attrs.update({
				'placeholder': 'Worker ID',
				'class': 'form-control',
			})

		self.fields['name'].label = 'Name'
		self.fields['name'].widget.attrs.update({
				'placeholder': 'Name',
				'class': 'form-control',
			})


class AllocateForm(forms.ModelForm):
	class Meta:
		model = Allocate
		fields = ['asset','task','worker','timeOfAllocation','taskToBePerformedBy']

	def __init__(self, *args, **kwargs):
		super(AllocateForm, self).__init__(*args, **kwargs)
				
		self.fields['asset'].label = 'Asset'
		self.fields['asset'].widget.attrs.update({
				'placeholder': 'Asset',
				'class': 'single-select-input',
			})

		self.fields['task'].label = 'Task'
		self.fields['task'].widget.attrs.update({
				'placeholder': 'task',
				'class': 'single-select-input',
			})

		self.fields['worker'].label = 'Worker'
		self.fields['worker'].widget.attrs.update({
				'placeholder': 'Worker',
				'class': 'single-select-input',
			})

		self.fields['timeOfAllocation'].label = 'Time Of Allocation'
		self.fields['timeOfAllocation'].widget.attrs.update({
				'placeholder': 'YYYY-mm-dd HH:MM:SS',
				'class': 'form-control',
			})

		self.fields['taskToBePerformedBy'].label = 'Task To Be Performed By'
		self.fields['taskToBePerformedBy'].widget.attrs.update({
				'placeholder': 'YYYY-mm-dd HH:MM:SS',
				'class': 'form-control',
			})