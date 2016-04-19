from django import forms
from django.forms import ModelForm
from .models import Projects

class ProjectsForm(forms.ModelForm):
	name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Project Name'}))
	description = forms.CharField(max_length=100,widget=forms.Textarea)
	image= forms.ImageField()
	class Meta:
		model = Projects
		fields = ['name', 'description','image']

class SearchForm(forms.Form):
	name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Project Name'}))
