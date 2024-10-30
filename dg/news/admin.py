from django.contrib import admin
from .models import News_post

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'pub_date', 'author')  # Добавьте поле автора в список
    readonly_fields = ('author',)  # поле автора только для чтения

    def save_model(self, request, obj, form, change):
        if not obj.author:  # Установите автора только при создании
            obj.author = request.user  # Установите текущего пользователя как автора
        obj.save()


admin.site.register(News_post, NewsAdmin)
