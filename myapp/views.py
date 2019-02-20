from django.shortcuts import render

# Create your views here.

def mhome(request):
    return render(request, 'mhome.html')