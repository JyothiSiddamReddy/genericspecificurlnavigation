from django.shortcuts import render

# Create your views here.
def VJ(request):
    return render(request,'VJ.html')

def JV(request):
    return render(request,'JV.html')
