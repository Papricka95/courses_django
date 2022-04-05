from django.template.defaulttags import url
from django.urls import path

from . import views

'''
фишка такой структуры:
при первом исполнении будут скомпилированы эти RegEx
что сделает эту часть выполнения быстрой
'''
urlpatterns = [

    path('', views.home),
    path('items', views.items, name='items'), #http://localhost:8000/items
    path('item/2003/', views.special_case_2003, name='special_case_2003'),
    # path('item/([0-9]{4})/', views.year_archive, name='special_case_2003'),
    # path('item/(?P<year>[\d]{4})/(?P<month>[0-9]{2})/(?P<day>[\d]{2})', views.day_archive, name="day_archive"),
    path('book/', views.page, name="page"),
    # path('book/page(?P<num>[0-9]+)/', views.page, name='page'),


    # url(r'^item/2003/$', views.special_case_2003, name='special_case_2003')
]

