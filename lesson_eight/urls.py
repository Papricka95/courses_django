from django.template.defaulttags import url
from django.urls import path

from . import views


urlpatterns = [
    path('register/', views.RegisterFormView.as_view()),
    path('login/', views.LoginFormView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('', views.MainView.as_view()),
    path('validate_email/', views.validate_email),
    path('show_three/', views.show_three),
    path('show_four/', views.show_four),
    path('add_human/', views.add_human)

]