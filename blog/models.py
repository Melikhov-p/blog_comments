from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-id']

class Comment(models.Model):
    content = models.TextField(verbose_name='Комментарий')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')
    parent_com = models.IntegerField(default=0, verbose_name='Род. комментарий')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['id']