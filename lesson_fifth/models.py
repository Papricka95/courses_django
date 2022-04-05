from django.db import models


# Create your models here.


class Author1(models.Model):
    CHOICES_FOR_CITY = (
        ('kyiv', "Киев"),  # формат такой: первое значение - представление в БД, второе - отображение данного поля юзеру
        ('chernigov', "Чернигов"),
        ('odessa', "Одесса"),
        ('Lvov', "Львов"),
    )
    name = models.CharField(max_length=200, verbose_name='Имя автора')
    surname = models.CharField(max_length=200, verbose_name='Фамилия автора')
    city = models.CharField(choices=CHOICES_FOR_CITY, max_length=200, blank=False, verbose_name='Город', help_text="Выберите город "
                                                                                                      "из списка")

    def __str__(self):
        return "Имя %s" % self.name


class Article(models.Model):
    author = models.ForeignKey(Author1, verbose_name="Автор статьи", on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    text = models.TextField(max_length=5000, verbose_name="Текст статьи")

    def __str__(self):
        return self.title
