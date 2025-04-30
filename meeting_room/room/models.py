from django.db import models

ROOM_CHOICES = [
    ('C01', 'C01'),
    ('C02', 'C02'),
    ('C03', 'C03'),
]

class Rooming(models.Model):
    name = models.CharField(max_length=100)
    room = models.CharField(max_length=50, choices=ROOM_CHOICES, default='C01')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.name} ห้องที่จอง {self.room} วันที่ {self.date}"
