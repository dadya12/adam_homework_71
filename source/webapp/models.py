from django.contrib.auth import get_user_model
from django.db import models


class Publication(models.Model):
    picture = models.ImageField(upload_to='publication/picture/', verbose_name='Аватар')
    description = models.TextField(verbose_name='Описание')
    comments_count = models.PositiveIntegerField(default=0, verbose_name='Счетчик комментариев')
    author = models.ForeignKey(get_user_model(), related_name='publications', on_delete=models.CASCADE, verbose_name='Автор')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    users_likes = models.ManyToManyField(get_user_model(), related_name='users_likes')

    def __str__(self):
        return f'{self.description} {self.created}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.author.publication_counter += 1
            self.author.save()
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.author.publication_counter -= 1
        self.author.save()
        return super().delete(*args, **kwargs)

class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), default=1, related_name='comments', on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField(verbose_name='Комментарий', max_length=400)
    post = models.ForeignKey('webapp.Publication', related_name='comments', on_delete=models.CASCADE, verbose_name='Публикация')
    likes = models.ManyToManyField(get_user_model(), related_name='loved_comments')
