from django.template.defaulttags import url
from django.urls import path

from . import views
from .views import List

urlpatterns = [
    path('', List.as_view(), name='list-view'),

]