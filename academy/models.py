from django.db import models


class PersonalTrainer(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.TextField(null=True, blank=True)
    registration_number = models.IntegerField()

    def __str__(self):
        return self.name
