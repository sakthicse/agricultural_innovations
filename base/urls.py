"""urlconf for the base application"""

from django.conf.urls import url, patterns
from .views import ProjectAddView,ProjectView,ProjectSearchView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('base.views',
    url(r'^$', 'home', name='home'),
    url(r'^project-add/', login_required(ProjectAddView.as_view()),name='project_add'),
    url(r'^projects/(?P<project_id>[0-9]+)/$', ProjectView.as_view(),name='project_view'),
    url(r'^project-search/', ProjectSearchView.as_view(),name='project_search'),
    # url(regex=r'^project/(?P<project_id>[\w.@+-]+)/$',ProjectView.as_view(),name='project_view')
)
# if settings.DEBUG:
#     from django.views.static import serve
#     _media_url = settings.MEDIA_URL
#     if _media_url.startswith('/'):
#         _media_url = _media_url[1:]
#         urlpatterns += patterns('',
#                                 (r'^%s(?P<path>.*)$' % _media_url,
#                                 serve,
#                                 {'document_root': settings.MEDIA_ROOT}))
#     del(_media_url, serve)
