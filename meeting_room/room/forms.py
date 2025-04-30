from django import forms
from .models import Rooming

# ตัวเลือกห้อง (Room choices)
ROOM_CHOICES = [
    ('C01', 'C01'),
    ('C02', 'C02'),
    ('C03', 'C03'),
    ('C04', 'C04'),
    ('C05', 'C05'),
    ('C06', 'C06'),
    ('C07', 'C07'),
    ('C08', 'C08'),
    ('C09', 'C09'),
    ('C10', 'C10'),
]

class RoomForm(forms.ModelForm):
    class Meta:
        model = Rooming
        fields = ['name', 'room', 'date', 'start_time', 'end_time']  # ✅ เพิ่ม 'room' เข้าไปแล้ว
