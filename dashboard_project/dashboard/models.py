from django.db import models

class DataPoint(models.Model):
    intensity = models.FloatField()
    likelihood = models.FloatField()
    relevance = models.FloatField()
    year = models.IntegerField()
    country = models.CharField(max_length=255)
    topics = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

class DashboardData(models.Model):

    def __str__(self):
        return f"{self.year} - {self.country}"
