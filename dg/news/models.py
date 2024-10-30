from django.db import models
from django.contrib.auth.models import User

class News_post(models.Model):
	title = models.CharField('Название новости', max_length=50)
	short_description = models.CharField('Краткое описание новости', max_length=200)
	#author = models.CharField('Название новости', max_length=50)
	text = models.TextField('Новость')
	pub_date = models.DateTimeField('Дата публикации')
	#author = models.CharField(User, max_length=50, default='0')  # Связь с моделью User
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Добавлено поле автора, может быть пустым
	# Новые поля
	#id_author2 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='author2', blank=True)
	#author2_name = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'