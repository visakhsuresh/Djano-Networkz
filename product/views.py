from django.shortcuts import render
from django.http import HttpResponse
from.models import list
def review(request):
    X= list.objects.all()
    return render(request,'index.html',{'X':X})

    #return HttpResponse("<h1>WELCOME TO NIKE</h1>")
    # Create your views here.
