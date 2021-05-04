from django.shortcuts import render
from django.http import HttpResponse

def hello():
    return HttpResponse('<h2>哈摟!!</h2>')