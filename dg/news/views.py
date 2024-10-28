from django.shortcuts import render
from django.contrib.auth.models import User

from .models import News_post
#from .forms import NewsForm

def home(request):
	news = News_post.objects.all()
	return render(request, 'news/news.html', {'news': news})

def user_list(request):
    users = User.objects.all()  # Извлекаем всех пользователей
    return render(request, 'user_list.html', {'users': users})  # Передаем пользователей в шаблон
# def create_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             form.save(user=request.user)  # Передаем текущего пользователя
#             return redirect('news_list')  # Перенаправляем на список новостей
#     else:
#         form = NewsForm()
#     return render(request, 'create_news.html', {'form': form})

