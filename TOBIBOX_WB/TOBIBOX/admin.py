from django.contrib import admin
from .models import ContactsInfo, AboutInfo, IndexPost, CarouselImg


# Register your models here.
@admin.register(IndexPost)
class IndexPostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'published_date')
    search_fields = ('post_title', 'published_date')


@admin.register(ContactsInfo)
class ContactsInfoAdmin(admin.ModelAdmin):
    list_display = ('contacts_title',)
    search_fields = ('contacts_title', 'contacts_info_text')


@admin.register(AboutInfo)
class AboutInfoAdmin(admin.ModelAdmin):
    list_display = ('about_title',)
    search_fields = ('about_title', 'about_info_text')


@admin.register(CarouselImg)
class CarouselImgAdmin(admin.ModelAdmin):
    list_display = ('carousel_title', 'img_one', 'img_two', 'img_three')
    search_fields = ('carousel_title', 'img_one', 'img_two', 'img_three')

