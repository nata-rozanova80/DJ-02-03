# = urls.py news
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import user_list


urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', include('myapp.urls')),
    #path('', views.home, name='news_home'),
    #path('news/', include('news.urls')),
    path('', views.home, name='news_home'),
    path('users/', user_list, name='user_list'),  # URL для отображения списка пользователей
]
# Добавляем статические файлы, если DEBUG=True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)