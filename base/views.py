""" Views for the base application """

from django.shortcuts import render
from .forms import ProjectsForm
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .models import Projects

def home(request):
    """ Default view for the root """
    return render(request, 'base/home.html')

class ProjectView(TemplateView):
	template_name = 'base/view-project.html'    
	def get(self,request,project_id):
		try:
			projects = Projects.objects.filter(pk=project_id)
		except Exception, e:
			projects = []
		
		return render(request, self.template_name, {"projects": projects})

	

class ProjectAddView(TemplateView):
	template_name = 'base/add-project.html'    
	def get(self,request):
		form = ProjectsForm
		return render(request, self.template_name, {"form": form})

	def post(self,request):

		#template_name = 'add-project.html'
		data = request.POST
		form = ProjectsForm(request.POST,request.FILES)
		if form.is_valid():
			project=form.save(commit=False)
			project.created_by=request.user
			project.save()
			#return HttpResponseRedirect('/')
			return render(request, 'base/home.html', {"success_message": "success"})
		return render(request, self.template_name, {"form": form})
	
class QueryView(TemplateView):
	pass
class QueryAddView(TemplateView):
	template_name = 'base/add-query.html'    
	def get(self,request):
		form = ProjectsForm
		return render(request, self.template_name, {"form": form})

class ProjectSearchView(TemplateView):
	# template_name = 'base/add-project.html'    
	# def get(self,request):
	# 	form = ProjectsForm
	# 	return render(request, self.template_name, {"form": form})

	def post(self,request):

		template_name = 'base/home.html'
		data = request.POST
		name=data['name']
		projects = Projects.objects.filter(name=name,is_apprival=True)
		#form = SearchForm(request.POST)
		# if form.is_valid():
		# 	project=form.save(commit=False)
		# 	project.save()
		# 	success_message
		# 	#return HttpResponseRedirect('/')
		# 	return render(request, '/base/home.html', {"success_message": success})
		return render(request, template_name, {"projects": projects})
		

