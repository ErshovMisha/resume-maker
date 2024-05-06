from django.db import models

class Res_Input(models.Model):
    name = models.TextField()
    second_name = models.TextField()
    data = models.TextField()

    class Meta:
        db_table = "Resume"
        get_latest_by = 'Res'
