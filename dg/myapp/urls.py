from django.urls import path

from . import views  # Импортируйте ваши представления


urlpatterns = [

    path('', views.home_view, name='home'),  # Новый маршрут для главной страницы
    path('data/', views.data_view, name='data'),  # URL для страницы data
    path('test/', views.test_view, name='test'),  # URL для страницы test
    path('new/', views.new, name='new'),  # URL для страницы new
    path('privacy policy/', views.privacy_policy, name='pp'),  # URL для страницы pp
    path('contacts/', views.contacts, name='contacts'),  # URL для страницы contacts

]
