from django.db import models

class SensorData(models.Model):
    user = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    soil_moisture = models.IntegerField()
    temprature = models.FloatField()
    rain = models.FloatField()
    irrigation_needed = models.BooleanField(default=False)
    humidity = models.FloatField()

    def __str__(self):
        return f"{self.timestamp} - Moisture: {self.soil_moisture}"