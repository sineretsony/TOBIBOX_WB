# Generated by Django 5.0 on 2024-01-06 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TOBIBOX', '0018_drawtemplates_max_material_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawtemplates',
            name='max_material',
            field=models.IntegerField(default=500, max_length=5, null=True, verbose_name='Максимальна товщина матерiалу'),
        ),
        migrations.AlterField(
            model_name='drawtemplates',
            name='min_material',
            field=models.IntegerField(default=360, max_length=5, null=True, verbose_name='Мінімальна товщина матерiалу'),
        ),
    ]