#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response

# Create your views here.
def home(request):
    return render_to_response("talk.html",{

    })