from django.shortcuts import render

from django.http import HttpResponse
from aiproject.models import Member
from .models import *

def home(request):
    members = Member.objects.all()
    articles = Article.objects.all()
    return render(request, 'index.html', locals())
# Create your views here.
