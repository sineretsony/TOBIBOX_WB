# Generated by Django 5.0 on 2024-01-02 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TOBIBOX', '0010_carouselimg_carousel_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrawTemplates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draw_name', models.CharField(max_length=30, verbose_name='Назва креслення')),
                ('max_width', models.IntegerField(max_length=5, verbose_name='Максимальна ширина')),
                ('min_width', models.IntegerField(max_length=5, verbose_name='Мінімальна ширина')),
                ('max_height', models.IntegerField(max_length=5, verbose_name='Максимальна висота')),
                ('min_height', models.IntegerField(max_length=5, verbose_name='Мінімальна висота')),
                ('max_depth', models.IntegerField(max_length=5, verbose_name='Максимальна глубина')),
                ('min_depth', models.IntegerField(max_length=5, verbose_name='Мінімальна глубина')),
                ('templates_upload', models.FileField(upload_to='drawing_templates/', verbose_name='Завантаження файлу')),
                ('templates_prev', models.ImageField(blank=True, upload_to='drawing_templates/', verbose_name="Прев'ю")),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TOBIBOX.boxcategory', verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Шаблон креслення',
                'verbose_name_plural': 'Шаблони креслення',
            },
        ),
    ]
