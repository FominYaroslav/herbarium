from django.shortcuts import render

# Create your views here.
def meassurement(request):
    return render(request, 'meassurement.html')