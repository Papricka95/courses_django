# Generated by Django 3.2.4 on 2021-09-02 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_fifth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(max_length=5000, verbose_name='Текст статьи'),
        ),
    ]
