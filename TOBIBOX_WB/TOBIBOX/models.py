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