from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def dashbord(request):
  return render(request, 'dashbord.html')
@login_required
def home(request):
  return render(request, 'home.html')

@login_required
def order(request):
  return render(request, 'home.html')