from django.db import models
from django.contrib.auth.models import User

class News_post(models.Model):
	title = models.CharField('Название новости', max_length=50)
	short_description = models.CharField('Краткое описание новости', max_length=200)
	#author = models.CharField('Название новости', max_length=50)
	text = models.TextField('Новость')
	pub_date = models.DateTimeField('Дата публикации')
	#author = models.CharField(User, max_length=50, default='0')  # Связь с моделью User

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'