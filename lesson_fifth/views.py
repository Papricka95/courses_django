from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . import forms



# Create your views here.


def search_form(request):
    return render(request, 'search_form.html', {})


def search(request):
    if request.method == "GET":
        if 'q' in request.GET:  # ключ 'q' есть в запросе request.GET
            if request.GET['q'] == '':
                return HttpResponse("Вы отправили пустую форму")
            return HttpResponse("Вы хотели найти %s" % request.GET['q'])  # с массива GET по ключу 'q'
        else:
            return HttpResponse("Вы отправили пустую форму или поменяйте ключ")


def test_view(request):
    # return HttpResponse('welcome to %s ' % request.path)  # вывод пути, по которому мы перешли
    # return HttpResponse('host is %s%s' %(request.get_host(), request.path))  # Полный путь
    # return HttpResponse('host is %s' % request.get_host())  # вывод пути, по которому мы перешли
    # return HttpResponse('Полный путь %s ' % request.get_full_path())  # вывод пути, по которому мы перешли
    return HttpResponse('Защищено %s ' % request.is_secure())  # вывод пути, по которому мы перешли


def file_input(request):
    name = request.POST['name']
    surname = request.POST['surname']
    birth = request.POST['birth']
    gender = request.POST['gender']
    some_file = open("some.txt", "w", encoding='utf-8')
    some_file.write("Имя: " + name + "\n")
    some_file.write("Фамилия: " + surname + "\n")
    some_file.write("Дата рождения: " + birth + "\n")
    some_file.write("Пол: " + gender + "\n")
    some_file.close()
    # return HttpResponse("Данные успешно были записаны в файл!")
    return render(request, "example.html", {})


def form(request):
    form_for_author1 = forms.AuthorOneForm
    form_for_article = forms.ArticleForm
    form_contact = forms.ContactForm
    context = {
        'form_for_author1': form_for_author1,
        'form_for_article': form_for_article,
        'form_contact': form_contact
    }
    return render(request, 'form.html', context)


def add_article(request):
    form_art = forms.ArticleForm(data=request.POST)
    if request.method == "POST":
        if form_art.is_valid():
            data = form_art.cleaned_data  # объект cleaned_data содержит все значения, которые нам пришли с формы в виде словаря
            form_art.save()  # сохраняем данные в БД
            # print(data['name'])
            return HttpResponse("Статья добавлена! %s" % request.path)


def author_add(request):
    form_auth = forms.AuthorOneForm(data=request.POST)  # принимает объект формы
    # print(request.POST)
    # print(form_auth)
    result = "Автор успешно добавлен %s" % request.path
    if request.method == "POST":
        if form_auth.is_valid():
            print(form_auth.is_valid())
            data = form_auth.cleaned_data  # объект cleaned_data содержит все значения, которые нам пришли с формы в виде
            # словаря
            form_auth.save()  # сохраняем данные в БД
            print(data['name'])
            return HttpResponse("Автор добавлен! %s" % request.path)


class ContactFormView(generic.TemplateView):
    form_for_author1 = forms.AuthorOneForm
    form_for_article = forms.ArticleForm
    form_contact = forms.ContactForm

    def post(self, request):
        form = forms.ContactForm(data=request.POST)
        context = {
            'form_for_author1': self.form_for_author1,
            'form_for_article': self.form_for_article,
            'form_contact': form
        }
        if form.is_valid():
            data = form.cleaned_data
            return HttpResponse(data.items())
        else:
            return render(request, 'form.html', context)

    def get(self, request):
        context = {
            'form_for_author1': self.form_for_author1,
            'form_for_article': self.form_for_article,
            'form_contact': self.form_contact
        }
        return render(request, 'form.html', context)