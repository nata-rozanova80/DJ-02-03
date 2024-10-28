# DJ-02
Перезалив после ошибки с папками

Нейрокот, [27.10.2024 1:44]
Чтобы задать фон страницам в проекте Django, вы можете использовать CSS. Вот пошаговое руководство, как это сделать:

### 1. Создание CSS файла

Сначала создайте CSS файл, если у вас его еще нет. Обычно CSS файлы хранятся в папке `static` вашего приложения. Например, создайте файл `styles.css` в директории `myapp/static/myapp/`.

```plaintext
myapp/
│
├── static/
│   └── myapp/
│       └── styles.css
└── templates/
    └── myapp/
        └── index.html
```

### 2. Добавление стилей в CSS файл

В вашем CSS файле (`styles.css`) добавьте стиль для фона. Например:

```css
body {
    background-color: #f0f0f0; /* Цвет фона */
    background-image: url('/static/myapp/background.jpg'); /* Фоновое изображение */
    background-size: cover; /* Покрытие всего экрана */
    background-repeat: no-repeat; /* Не повторять изображение */
}
```

### 3. Подключение CSS файла в HTML шаблоне

В вашем HTML шаблоне (например, `index.html`) подключите CSS файл. Используйте тег `{% load static %}` для корректной работы с статическими файлами Django.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Моя страница</title>
    {% load static %}
    <link rel="stylesheet" type="text/css" href="{% static 'myapp/styles.css' %}">
</head>
<body>
    <h1>Добро пожаловать на мою страницу!</h1>
    <!-- Остальная часть вашего контента -->
</body>
</html>
```

### 4. Убедитесь, что статические файлы настроены правильно

Убедитесь, что ваш проект настроен для работы со статическими файлами. В вашем `settings.py` должны быть следующие настройки:

```python
STATIC_URL = '/static/'

# Если у вас есть локальная папка для статических файлов, добавьте:
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

### 5. Запустите сервер

Теперь запустите сервер разработки Django с помощью команды:

```bash
python manage.py runserver
```

Перейдите на страницу, и вы должны увидеть фон, который вы задали в `styles.css`.

USERS NAMES

Чтобы вывести имена зарегистрированных пользователей на сайте, сделанном на Django, вам необходимо выполнить несколько шагов. Предполагается, что у вас уже есть настроенная модель пользователя и вы используете стандартную модель User от Django. Вот как это сделать:

### Шаг 1: Импортируйте модель пользователя

Если вы используете стандартную модель пользователя Django, вам нужно импортировать её в вашем представлении (views.py):

from django.contrib.auth.models import User


### Шаг 2: Создайте представление

Создайте представление, которое будет извлекать всех зарегистрированных пользователей из базы данных и передавать их в шаблон. Пример:

from django.shortcuts import render
from django.contrib.auth.models import User

def user_list(request):
    users = User.objects.all()  # Извлекаем всех пользователей
    return render(request, 'user_list.html', {'users': users})  # Передаем пользователей в шаблон


### Шаг 3: Настройте URL

Добавьте маршрут для вашего нового представления в файл urls.py вашего приложения:

from django.urls import path
from .views import user_list

urlpatterns = [
    path('users/', user_list, name='user_list'),  # URL для отображения списка пользователей
]


### Шаг 4: Создайте шаблон

Создайте шаблон user_list.html в папке templates вашего приложения (если папка не существует, создайте её). Внутри этого файла вы можете использовать следующий код для отображения имен пользователей:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Список пользователей</title>
</head>
<body>
    <h1>Список зарегистрированных пользователей</h1>
    <ul>
        {% for user in users %}
            <li>{{ user.username }}</li>  <!-- Выводим имя пользователя -->
        {% empty %}
            <li>Нет зарегистрированных пользователей.</li>
        {% endfor %}
    </ul>
</body>
</html>


### Шаг 5: Проверьте функциональность

Теперь вы можете запустить сервер Django:

python manage.py runserver


Перейдите по адресу http://127.0.0.1:8000/users/, чтобы увидеть список зарегистрированных пользователей.

### Дополнительные настройки

- Если вы хотите выводить дополнительные поля (например, email), вы можете изменить строку {{ user.username }} на {{ user.email }} или другие поля, доступные в модели User.
- Убедитесь, что у вас есть зарегистрированные пользователи в базе данных, иначе список будет пустым.


