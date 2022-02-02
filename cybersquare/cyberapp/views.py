from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cyber(request):

    return render(request,'cybersquare.html')
