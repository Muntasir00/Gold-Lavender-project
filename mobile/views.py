from django.shortcuts import render, redirect
from .models import Mobile
from .forms import MobileForm
from django.http import JsonResponse
from django.shortcuts import HttpResponse

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

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


def search_results(request):
    if request.is_ajax():
        res = None
        mobile = request.POST.get('mobile')
        qs = Mobile.objects.filter(name__icontains=mobile)
        if len(qs) > 0 and len(mobile) > 0:
            data = []
            for pos in qs:
                item = {
                    'pk':pos.pk,
                    'brand_name':pos.brand_name,
                    'model_name':pos.model_name,
                    'color':pos.color,
                    'jan_code':pos.jan_code,
                    'image':str(pos.image.url)
                    
                    
                }
                data.append(item)
            res = data
        else:
            res = 'No mobiles found...'
        return JsonResponse({'data':res})
        
            
    return JsonResponse({})
