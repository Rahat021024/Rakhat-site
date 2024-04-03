from django.db import models

class allPosts(models.Model):
  user = models.CharField(max_length=100)
  avatar = models.ImageField(upload_to=('photo%/Y%/m%/d'))
  title = models.CharField(max_length=255)
  description = models.TextField()
  dete_create = models.DateField(auto_now=True)
  is_published = models.BooleanField(default=True)

  class Meta:
    verbose_name = ("Пост")
    verbose_name_plural = ("Посты")

  def __str__(self):
    return self.user


