from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def demo(request):
#     return HttpResponse("hello Welcome user")

def about(request):

    return render(request,'index.html')
def operation(request):


    x=int(request.GET["num1"])
    y=int(request.GET["num2"])
    res=x+y
    res1=x-y
    res2=x*y
    res3=x/y
    return render(request,'operation.html',{'result':res,'result1':res1,'result2':res2,'result3':res3})

def contact(request):
    return HttpResponse("contact number:+0987654345678")

def detail(request):
    return render(request,'detail.html')

def thanks(request):
    return HttpResponse('THANKS TO ALL')

