from django.conf.urls import include
from django.template.defaulttags import url
from django.urls import path

from . import views

'''
фишка такой структуры:
при первом исполнении будут скомпилированы эти RegEx
что сделает эту часть выполнения быстрой

UPD20210612: запись вида "?:" передается только один именованный аргумент! 
'''
# extra_patterns = [
#     url(r'^report/$', views.report),
#     url(r'^report/(?P<id>[0-9]+)/$', views.report),
# ]
#
#
# urlpatterns = [
#     url(r'blog/(page-(\d+)/)?$', views.blog_articles, name='blog_articles'), #bad
#     url(r'comments/(?:page-(?P<page_number>\d+)/)', views.comments, name='blog_articles'), #good
#     url(r'optional_args/(?P<year>[0-9]{4})/$', views.optional_args, {'foo': 'bar'}),
#     url(r'extra/', include(extra_patterns)),
#     # url(r'^item/2003/$', views.special_case_2003, name='special_case_2003')
# ]

# urlpatterns = {
#     url(r'^(?P<page_slug>[\w]+)-(?P<page_id>[\w]+)/history/$', views.history),
#     url(r'^(?P<page_slug>[\w]+)-(?P<page_id>[\w]+)/edit/$', views.edit),
#     url(r'^(?P<page_slug>[\w]+)-(?P<page_id>[\w]+)/discuss/$', views.discuss),
#     url(r'^(?P<page_slug>[\w]+)-(?P<page_id>[\w]+)/permissions/$', views.permissions),
#     # url(r'^item/2003/$', views.special_case_2003, name='special_case_2003')
# }


urlpatterns = [
    # path('(?P<page_slug>[\w]+)-(?P<page_id>[\w]+)/', include([
    path('history/', views.history),
    path('edit/', views.edit),
    path('discuss/', views.discuss),
    path('permissions/', views.permissions),

]