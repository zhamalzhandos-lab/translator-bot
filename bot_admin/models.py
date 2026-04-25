from django.db import models

class UserQuery(models.Model):
    telegram_id = models.BigIntegerField()
    username = models.CharField(max_length=100, blank=True, null=True)
    word = models.CharField(max_length=200)
    translation = models.CharField(max_length=200, blank=True)
    found = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username or self.telegram_id}: {self.word} → {self.translation}"

    class Meta:
        verbose_name = "Запрос пользователя"
        verbose_name_plural = "Запросы пользователей"
        ordering = ["-created_at"]
