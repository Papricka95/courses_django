# Generated by Django 3.2.4 on 2021-07-21 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_fourth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('date_birth', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='example',
            name='date_field',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='example',
            name='date_time_field',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='example',
            name='text_field',
            field=models.TextField(max_length=50),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=1000)),
                ('genre', models.CharField(choices=[('comedy', 'Comedy'), ('tragedy', 'Tragedy'), ('drama', 'Drama')], max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson_fourth.author')),
            ],
        ),
    ]
