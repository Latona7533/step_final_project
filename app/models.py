from django.db import models

"""
2 организация бд:
	Профиль 
		фото
		описание
	
	Портфолио
		картинка
		описание
		ссылка
		сложность(1-5)
	
	Комментарии
		текст

	Блог
		название
		текст

"""


class Profile(models.Model):
    photo = models.ImageField(upload_to='photos/')
    descr = models.TextField(max_length=50)

    def __str__(self):
        return self.descr

class Portfolio(models.Model):
    DIFFICULT = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),

    ]

    image = models.ImageField(upload_to='photos/')
    descr = models.TextField(max_length=50)
    link = models.CharField(max_length=50)
    difficult = models.CharField(max_length=1, choices=DIFFICULT,default='1',)


    def __str__(self):
        return self.descr

class Comment(models.Model):
    project = models.ForeignKey(Portfolio, on_delete=models.CASCADE, default=None, related_name='comments')
    text = models.TextField(max_length=50)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.text


class Blog(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=5000)

    def __str__(self):
        return self.name
