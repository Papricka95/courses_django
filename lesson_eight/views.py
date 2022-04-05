from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
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
from .forms import HumanForm

from lesson_sixth.models import Human

from django.views.decorators.csrf import csrf_exempt # нужен для того, чтоб ajax запрос выполнялся корректно, чтоб не было перехватов наших данных


class MainView(TemplateView):
    template_name = 'ajax.html' # то, что будем рендерить
    human_form = HumanForm

    def get(self, request):
        ctx = {}
        if request.user.is_authenticated: # авторизован ли юзер
            all_humans = Human.objects.all()
            ctx['humans'] = all_humans
            ctx['human_form'] = self.human_form
            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, {})


class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = "/lesson_eight/login" # этот урл будет срабатывать в случае успешной регистрации
    template_name = "register_8.html" # что отобразить пользователю с нашей формой

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form) # возвращаем контекст ошибок


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "login.html"

    success_url = "/lesson_eight/"

    def form_valid(self, form):
        # получаем объект пользователя на основе введенных в форму данных.
        self.user = form.get_user()

        # выполняем аутентификацию пользователя
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginFormView, self).form_invalid(form)


def validate_email(request):
    if request.GET:
        email = request.GET.get('email') # забираем по ключу email
        is_taken = User.objects.filter(email=email).exists() # проверка того, если есть в БД такой email, то записываем True
        if is_taken:
            data = {
                "is_taken": "На этот почтовый ящик уже зарегистрирован пользователь!"
            }
            return JsonResponse(data) # отправляем Json на наш клиент
        else:
            return JsonResponse(data={"ok": "На этот почтовый адрес не было регистраций"})  # отправляем Json на наш клиент


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/lesson_eight/")



def show_three(request): # показать 3 записи
    first_three = Human.objects.all()[:3].values()  # сделает ключ-значение

    context = {
        'elements': list(first_three) # приводим к типу JSON (список списков)
    }
    return JsonResponse(context)


def show_four(request): # показать 4 записи
    first_four = Human.objects.all()[:4].values()

    context = {
        'elements': list(first_four)
    }
    return JsonResponse(context)


@csrf_exempt
def add_human(request):
    if request.POST:
        if request.is_ajax():
            name = request.POST['name']
            surname = request.POST['surname']
            birth = request.POST['birth']
            company = request.POST['company']
            position = request.POST['position']
            language = request.POST['language']
            salary = request.POST['salary']
            human_loc = Human.objects.create(
                                         name=name,
                                         surname=surname,
                                         birth=birth,
                                         company=company,
                                         position=position,
                                         language=language,
                                         salary=salary
                                         ) # создаем новый объект. слева - поля, справа - значение с пост запроса
    return JsonResponse(human_loc.dict())



