from django.shortcuts import render
from  .models import Place
from .models import Teammembers
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=Teammembers.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})