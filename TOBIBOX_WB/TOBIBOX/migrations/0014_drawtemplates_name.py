# Generated by Django 5.0 on 2024-01-02 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TOBIBOX', '0013_drawtemplates_draw_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='drawtemplates',
            name='name',
            field=models.CharField(blank=True, default='', help_text='Назва файлу без розширення', max_length=30, null=True, verbose_name='Назва файлу'),
        ),
    ]
