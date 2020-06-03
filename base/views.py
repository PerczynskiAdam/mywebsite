from django.shortcuts import render

# Create your views here.
def home(request):
   return render(request, 'base/home.html')

def dash(request):
   return render(request, 'base/dash.html')

def datascience(request):
   return render(request, 'base/datascience.html')