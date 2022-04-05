from django.template.defaulttags import url
from django.urls import path, re_path

from . import views

'''
фишка такой структуры:
при первом исполнении будут скомпилированы RegEx
что сделает эту часть выполнения быстрой
'''
urlpatterns = [
    path('filters/', views.filter_func),
    re_path(r'^view/$', views.view),
    path('tags-if/', views.tags_if),
    path('tags-for/', views.tags_for),
    path('check/', views.check),
    path('in/', views.tag_in),
#    url(r'^regroup/$', views.tag_regroup),
   #  url(r'^items$', views.items, name='items'), #http://localhost:8000/items
   #  url(r'^item/2003/$', views.special_case_2003, name='special_case_2003'),
   #  url(r'^item/([0-9]{4})/$', views.year_archive, name='special_case_2003'),
   #  url(r'^item/(?P<year>[\d]{4})/(?P<month>[0-9]{2})/(?P<day>[\d]{2})', views.day_archive, name="day_archive"),
   #
   # url(r'^book/$', views.page, name="page"),
   # url(r'^book/page(?P<num>[0-9]+)/$', views.page, name='page')


    # url(r'^item/2003/$', views.special_case_2003, name='special_case_2003')
]

