from django.http import HttpResponse
from django.shortcuts import render
from team.models import team
def homepage(request):
    teams = team.objects.all()
    return render (request,'home.html',{"teams": teams})