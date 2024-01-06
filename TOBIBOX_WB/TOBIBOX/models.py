import os

from django.contrib.auth.models import User
from django.db import models



# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class BoxCategory(models.Model):
    name_box_category = models.CharField(max_length=40,
                                         verbose_name='Категорія')

    def __str__(self):
        return self.name_box_category

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class DrawTemplates(models.Model):
    draw_name = models.CharField(
        max_length=30,
        verbose_name='Назва креслення')
    draw_content = models.TextField(
        verbose_name='Опис креслення')
    category = models.ForeignKey(
        BoxCategory,
        on_delete=models.CASCADE,
        verbose_name='Категорія')
    max_width = models.IntegerField(
        max_length=5,
        verbose_name='Макс. ширина')
    min_width = models.IntegerField(
        max_length=5,
        verbose_name='Мін. ширина')
    max_height = models.IntegerField(
        max_length=5,
        verbose_name='Макс. висота')
    min_height = models.IntegerField(
        max_length=5,
        verbose_name='Мін. висота')
    max_depth = models.IntegerField(
        max_length=5,
        verbose_name='Макс. глибина')
    min_depth = models.IntegerField(
        max_length=5,
        verbose_name='Мін. глибина')
    templates_upload = models.FileField(
        null=False,
        upload_to='drawing_templates/',
        verbose_name='Креслення')
    templates_prev = models.ImageField(
        default='static/TOBIBOX/svg/favicon.svg',
        upload_to='drawing_templates/',
        verbose_name='Прев\'ю')
    max_material = models.IntegerField(
        null=True,
        default=500,
        max_length=5,
        verbose_name='Макс. тов. матерiалу')
    min_material = models.IntegerField(
        null=True,
        default=360,
        max_length=5,
        verbose_name='Мін. тов. матерiалу')

    file_name = models.CharField(
        max_length=30,
        verbose_name='Назва файлу',
        null=True,
        default='',
        help_text='Назва файлу без розширення')

    def save(self, *args, **kwargs):
        if self.templates_upload:
            filename_and_path = os.path.basename(self.templates_upload.name)
            name_file_no_py, _ = os.path.splitext(filename_and_path)
            self.file_name = name_file_no_py
        super().save(*args, **kwargs)

    def __str__(self):
        return self.draw_name

    class Meta:
        verbose_name = 'Шаблон креслення'
        verbose_name_plural = 'Шаблони креслення'


class IndexPost(models.Model):
    post_title = models.CharField(
        max_length=30,
        verbose_name='Зміст посту')
    post_content = models.TextField(
        verbose_name='Опис новини')
    published_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата та час')
    post_img = models.ImageField(
        blank=True,
        upload_to='posters/',
        verbose_name='Постер')

    def __str__(self):
        return self.post_title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'


class ContactsInfo(models.Model):
    contacts_title = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        default='Контакти',
        verbose_name='Контакти (title)')

    contacts_info_text = models.TextField(
        blank=True,
        null=True,
        default='TOBIBOX',
        verbose_name='Інформація про контакти')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакти'

    def __str__(self):
        return self.contacts_title


class AboutInfo(models.Model):
    about_title = models.CharField(
        max_length=30,
        default='Наша команда',
        verbose_name='Про нас (title)',
        help_text='Заголовок раздела "Про нас"'
    )
    about_info_text = models.TextField(
        default='TOBIBOX',
        verbose_name='Інформація про нас',
        help_text='Текст з інформацією про вашу команду'
    )
    post_img = models.ImageField(
        blank=True,
        upload_to='other_img/',
        verbose_name='Значок/пiдпис')

    class Meta:
        verbose_name = 'Про нас'
        verbose_name_plural = 'Про нас'

    def __str__(self):
        return self.about_title


class CarouselImg(models.Model):
    carousel_title = models.CharField(
        max_length=30,
        default='Карусель',
        verbose_name='Карусель',
        help_text='Карусель')

    img_one = models.ImageField(
        blank=True,
        upload_to='carousel/',
        verbose_name='Зображення 1')

    img_two = models.ImageField(
        blank=True,
        upload_to='carousel/',
        verbose_name='Зображення 2')

    img_three = models.ImageField(
        blank=True,
        upload_to='carousel/',
        verbose_name='Зображення 3')

    class Meta:
        verbose_name = 'Карусель'
        verbose_name_plural = 'Каруселi'

    def __str__(self):
        return self.carousel_title


class SocialMedia(models.Model):
    telegram_link = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Посилання телеграм')
    instagram_link = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Посилання iнастаграм')
    facebook_link = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Посилання фейсбук')
    email_txt = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Пошта')

    class Meta:
        verbose_name = 'Соц налаштування'
        verbose_name_plural = 'Соц налаштування'

    def __str__(self):
        return 'Насройки блоку соціальних мереж'

