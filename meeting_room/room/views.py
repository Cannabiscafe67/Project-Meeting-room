from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Rooming
from .forms import RoomForm

#Home หรือ ข้อมูลการจอง
@login_required
def home(request):
    rooms = Rooming.objects.all()
    return render(request, 'room/home.html', {'rooms': rooms})

#เพิ่มการจองห้อง
def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RoomForm()
    return render(request, 'room/add_room.html', {'form': form})

#แก้ไขการจองห้อง
def edit_room(request, room_id):
    room = get_object_or_404(Rooming, id=room_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RoomForm(instance=room)
    return render(request, 'room/edit_room.html', {'form': form})

#ลบการจองห้อง
def delete_room(request, room_id):
    rooming = get_object_or_404(Rooming, id=room_id)
    rooming.delete()
    return redirect('home')

#ค้นหาการจองห้อง
def search_room(request):
    query = request.GET.get('query')
    results = []
    if query:
        results = Rooming.objects.filter(name__icontains=query)  # ค้นหาจากชื่อผู้จอง
    return render(request, 'room/search_room.html', {'results': results})

#หน้า About
def about(request):
    return render(request, 'room/about.html')

#หน้าlogin
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง')
    return render(request, 'room/login.html')

# ฟังก์ชัน logut
def logout_view(request):
    logout(request)
    return redirect('login')

# หน้าสมัคร
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'มีผู้ใช้นี้แล้วในระบบ')
            return redirect('register')

        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)  # ล็อกอินอัตโนมัติหลังสมัคร
        return redirect('home')
    
    return render(request, 'room/register.html')

from .models import Rooming

from datetime import datetime
from django.core.exceptions import ValidationError

def add_room(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        room = request.POST.get('room')
        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        try:
            # พยายามแปลงให้เป็นเวลาจริง
            start_time = datetime.strptime(start_time, '%H:%M').time()
            end_time = datetime.strptime(end_time, '%H:%M').time()

            Rooming.objects.create(
                name=name,
                room=room,
                date=date,
                start_time=start_time,
                end_time=end_time
            )
            return redirect('home')
        
        except ValueError:
            raise ValidationError("กรุณากรอกเวลาในรูปแบบ HH:MM เท่านั้น")
    
    return render(request, 'room/add_room.html')

# ค้นหาการจองห้อง
def search_room(request):
    query = request.GET.get('query')
    results = []

    if query:
        results = Rooming.objects.filter(name__icontains=query)  # ใช้ Rooming ไม่ใช่ Room

    return render(request, 'room/search_room.html', {  # ไฟล์ต้องชื่อ search_room.html
        'results': results,
        'query': query,
    })
