from .models import Projects,SiteInfo
from django.conf import settings
from django.shortcuts import render
from .forms import SearchForm
def contexts(request):
	try:
		projects = Projects.objects.filter(is_apprival=True)
	except Exception, e:
		projects = []
	try:
		siteinfo = SiteInfo.objects.get()
	except Exception, e:
		siteinfo = []
	form = SearchForm	
	#siteinfo = SiteInfo.objects.get()
	return {"projects":projects,"siteinfo":siteinfo,"form":form}
