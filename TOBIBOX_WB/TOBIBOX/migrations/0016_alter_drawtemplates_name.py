# Generated by Django 5.0 on 2024-01-02 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TOBIBOX', '0015_alter_drawtemplates_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawtemplates',
            name='name',
            field=models.CharField(default='', help_text='Назва файлу без розширення', max_length=30, null=True, verbose_name='Назва файлу'),
        ),
    ]
