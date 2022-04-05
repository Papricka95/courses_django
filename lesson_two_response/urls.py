from django.template.defaulttags import url
from django.urls import path

from . import views




urlpatterns = [
    path('', views.hello_response), #http://localhost:8000/lesson-two-response/
    path('redirect/', views.http_redirect),
    path('fun1/', views.fun1),
    path('render-html/', views.render_html), #is very bad
    path('render-template/', views.render_template),
    path('render-template/form-hendler/', views.form_hendler)

]