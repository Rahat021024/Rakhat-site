from django.db import models

class Danatube(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class User(models.Model):
    userName = models.CharField(max_length=40)
    ava = models.ImageField(upload_to='ava/%Y/%m/%d')
    biographi = models.TextField(blank=True)
    birthday = models.DateField()

    def __str__(self):
        return self.userName

    class Meta:
        ordering = ['userName']
        verbose_name = 'Имя пользователь'
        verbose_name_plural = 'Имя пользователи'




