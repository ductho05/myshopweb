from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    subject_name = models.CharField(max_length=30)
    contents = models.CharField(max_length=1000)
    status = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.contents

    def __recode__(self):
        return self.name