from django.db import models
from django.contrib.auth.models import User


class Res_Input(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(null=False)
    second_name = models.TextField(null=False)
    data = models.CharField(max_length=140)

    class Meta:
        db_table = "Resume"
        get_latest_by = 'Res'
    def create(self, user, *args, **kwargs):
        # Додаємо користувача до форми перед збереженням
        obj = super().create(user= user, *args, **kwargs)
        return obj