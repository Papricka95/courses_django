from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from lesson_sixth.models import Human


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=True)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class HumanForm(forms.ModelForm):
    class Meta:
        model = Human # модель, которая будет взята за основу это модель Human из lesson_sixth
        fields = {field.name for field in Human._meta.fields} # и поля, которые мы отобразим