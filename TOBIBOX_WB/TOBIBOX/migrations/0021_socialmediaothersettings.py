# Generated by Django 5.0 on 2024-01-06 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TOBIBOX', '0020_alter_drawtemplates_max_depth_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaOtherSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_link', models.URLField(blank=True, null=True, verbose_name='Посилання телеграм')),
                ('instagram_link', models.URLField(blank=True, null=True, verbose_name='Посилання iнастаграм')),
                ('facebook_link', models.URLField(blank=True, null=True, verbose_name='Посилання фейсбук')),
                ('email_txt', models.CharField(blank=True, max_length=50, null=True, verbose_name='Пошта')),
            ],
        ),
    ]
