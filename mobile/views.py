from django.shortcuts import render, redirect
from .models import Mobile
from .forms import MobileForm



def home(request):
    mobiles = Mobile.objects.all()
    return render(request,'home.html',{'mobiles':mobiles})

def add_mobile(request):
    if request.method == 'POST':
        form = MobileForm(request.POST, request.FILES)
        if form.is_valid():
            mobile = form.save(commit=False)
            mobile.save()

            return redirect('home')

    else:
        form = MobileForm()

    return render(request, 'add_mobile.html', {'form':form})

