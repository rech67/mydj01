from django.shortcuts import render
from django.http import HttpResponse

<<<<<<< HEAD
def hello(request):
=======
def hello():
>>>>>>> a6c177ceb4ba45778ef5e743224e01a30f41430a
    return HttpResponse('<h2>哈摟!!</h2>')