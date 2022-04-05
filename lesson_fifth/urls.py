from django.template.defaulttags import url
from django.urls import path

from . import views

urlpatterns = [
    # url(r'^$', views.form),
    path('', views.ContactFormView.as_view()),
    path('test-view/', views.test_view),
    path('search-form/', views.search_form),
    path('file-input/', views.file_input),
    path('search/', views.search),
    path('add-article/', views.add_article),
    path('add-author/', views.author_add),
]