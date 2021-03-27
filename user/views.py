from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request,'user/home.html',{'home': home})

def start(request):
    
    return render(request,'user/start.html',{'start': home})

def go_to(request):
    
    return render(request,'user/go_to.html',{'go_to': go_to})
