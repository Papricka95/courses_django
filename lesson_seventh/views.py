from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout

from .forms import UserCreateForm
from lesson_sixth.models import Human


class MainView(TemplateView):
    template_name = 'main_seventh.html'

    def get(self, request):
        if request.user.is_authenticated:
            humans = Human.objects.all()
            ctx = {}
            ctx['humans'] = humans
            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, {})


class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = "/lesson_seventh/login/" # этот урл будет срабатывать в случае успешной регистрации

    template_name = "register.html" # что отобразить пользователю с нашей формой

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "login.html"

    success_url = "/lesson_seventh/"

    def form_valid(self, form):
        # получаем объект пользователя на основе введенных в форму данных.
        self.user = form.get_user()

        # выполняем аутентификацию пользователя
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/lesson_seventh/")