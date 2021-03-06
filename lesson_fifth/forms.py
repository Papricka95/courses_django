from django.forms import ModelForm

from django import forms
from .models import Author1
from .models import Article

'''
Ниже определены формы, которые основаны на моделях из models.py
'''


class AuthorOneForm(ModelForm):
    class Meta:
        model = Author1  # то, какую модель будем отображать
        fields = ['name', 'surname', 'city']  # какие поля будут видны


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['author', 'title', 'text']


class ContactForm(forms.Form):
    boolean_field = forms.BooleanField()
    float_field = forms.FloatField()
    name_sender = forms.CharField(max_length=100, label="Введите ваше имя")
    message = forms.CharField(widget=forms.Textarea, label="Сообщение")
    sender = forms.EmailField(label="Введите ваш емейл")
