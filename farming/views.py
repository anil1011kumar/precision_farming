from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SensorData
from .forms import SensorDataForm
from .utils import get_weather_data, get_fertilizer_recommendation
from .irrigation import should_irrigate
import random
from .forms import UserRegisterForm
from django.contrib import messages






def dashboard(request):
    soil_moisture = random.randint(300, 800)
    weather = get_weather_data()
    irrigation = should_irrigate(soil_moisture , weather['rain'])
    data = SensorData.objects.create(soil_moisture = soil_moisture, temprature = weather['temprature'], humidity = weather['humidity'], rain = weather['rain'], irrigation_needed = irrigation)
    

    return render(request,'dashboard.html',{'data': data})
def register_view(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created Successfully! Please Login.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'register.html',{'form':form})
@login_required
def farmer_input(request):
    result = None
    if request.method == 'POST':
        form = SensorDataForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.irrigation_needed = data.humidity < 50
            data.save()
            result = "Yes" if data.irrigation_needed else "No"
    else:
        form = SensorDataForm()
    recent_data = SensorData.objects.filter(user=request.user).order_by('-id')[:5]

    return render(request, 'farmer_input.html',{'form':form, 'result': result, 'recent_data': recent_data}) 

def fertiliser_view(request):
    recommendation = None
    if request.method == "POST":
        crop_type = request.POST.get("crop_type")
        soil_type = request.POST.get("soil_type")
        season = request.POST.get("season")
        recommendation = get_fertilizer_recommendation(crop_type, soil_type,season)
    return render (request, "fertiliser.html", {"recommendation": recommendation})

           

