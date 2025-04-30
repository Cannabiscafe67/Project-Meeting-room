from django.contrib import admin
from room.models import Rooming # นำเข้าโมเดลที่สร้างไว้

# Register your models here.
admin.site.register(Rooming)  # ลงทะเบียนโมเดลให้แสดงใน admin