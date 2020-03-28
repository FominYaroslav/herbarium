from django.shortcuts import render

# Create your views here.
def picker(request):
    return render(request, 'color picker.html')
