from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':1436,'b':341,}
    return render(request,'operations.html',d)
