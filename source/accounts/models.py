from django.contrib.auth import get_user_model
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        related_name="profile",
        verbose_name="Профиль",
        on_delete=models.CASCADE,
    )

    avatar = models.ImageField(
        verbose_name="Аватар",
        upload_to="avatars/",
        null=True,
        blank=True
    )

    git_url = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Ссылка"
    )

    about_user = models.TextField(
        max_length=2000,
        null=True,
        blank=True,
        verbose_name="О себе",
    )

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self) -> str:
        return f"Профиль: {self.user.username}. {self.id}"
