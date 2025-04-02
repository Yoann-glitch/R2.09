from django.shortcuts import render

# Create your views here.
def index(request):
2 return render(request, 'mysecondapp/formulaire1.html')