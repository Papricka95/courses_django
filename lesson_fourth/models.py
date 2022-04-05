from django.db import models

'''
Значение атрибута on_delete в ForeignKey: 

CASCADE 
Каскадное удаление. Django эмулирует поведение SQL правила ON DELETE CASCADE и также удаляет объекты, связанные через ForeignKey

PROTECT
Препятствует удалению связанного объекта, вызывая исключение django.db.models.ProtectedError

SET_NULL
Устанавливает ForeignKey в NULL

SET_DEFAULT
Устанавливает ForeignKey в значение по умолчанию.
'''

'''
РЕАЛИЗАЦИЯ СВЯЗИ FOREIGNKEY (ОДИН КО МНОГИМ)
'''


# Create your models here.
class Example(models.Model):
    integer_field = models.IntegerField()
    positive_field = models.PositiveIntegerField()
    positive_small_field = models.PositiveSmallIntegerField()
    big_integer_field = models.BigIntegerField()
    float_field = models.FloatField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=5)
    text_field = models.TextField(max_length=50)
    date_field = models.DateField(auto_now=False)  # сохраняем дату нашего ПОСЛЕДНЕГО ИЗМЕНЕНИЯ
    date_time_field = models.DateTimeField(auto_now_add=False)  # сохраняем в этом поле текущую дату СОЗДАНИЯ объекта
    decimal_field = models.DecimalField(max_digits=8,
                                        decimal_places=2)  # 222222.22 (всего цифр в числе = 8: 6, до запятой, 2 после)
    email = models.EmailField()
    file_field = models.FileField(upload_to='file')
    image_field = models.ImageField(upload_to='images')


class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    date_birth = models.DateField(auto_now=False, verbose_name="Дата рождения")  # Сами будем выставлять ДР автора :)

    def __str__(self):  # Этот метод отвечает за отображение авторов в базе
        return "Имя: %s Фамилия: %s" % (self.name, self.surname)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    '''
    Привязали автора к определенной книжке ForeignKey
    Когда будем добавлять книгу на наш сайт, то будет предлагаться список авторов, которые
    сначала надо будет зарегистрировать.
    '''
    # кортеж создан для выбора в админке жанра нашей книги
    CHOISE_GENRE = (
        ('comedy', 'Comedy'),  # Первое слово будет находится в нашей базе данных
        ('tragedy', 'Tragedy'),  # Второе слово это то, что будет отображено в пользовательском виджете админки
        ('drama', 'Drama')
    )

    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE)  # атрибут on_delete говорит о том, что нужно делать при удалении записей из БД
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    genre = models.CharField(max_length=50, choices=CHOISE_GENRE)

    def __str__(self):  # Этот метод отвечает за отображение авторов в базе
        return self.title


'''
РЕАЛИЗАЦИЯ СВЯЗИ ONE_TO_ONE
'''


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name


class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name  # Ссылка на place, и у объекта класса Place будет выводится имя этого места


class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)


'''
РЕАЛИЗАЦИЯ СВЯЗИ MANY_TO_MANY
'''


class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline', )