from django.contrib.auth import get_user_model
from django.db import models


class Comments(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        related_name='user_comment',
        null=False,
        blank=False,
        verbose_name='Автор',
        on_delete=models.CASCADE
    )
    description = models.TextField(
        max_length=1000,
        null=False,
        blank=False,
        verbose_name="Комментарий"
    )
    post = models.ForeignKey(
        to='instagram.Posts',
        related_name='post',
        null=False,
        blank=False,
        verbose_name='Пост',
        on_delete=models.CASCADE
    )
    likes = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Количество лайков в посте",
        default=0
    )

    def __str__(self):
        return f'{self.user} - {self.likes}'
