from django.db import models


class GeneratorModel(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return self.title
