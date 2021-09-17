from django.http.response import HttpResponse
from django.shortcuts import render
from django.http.request import HttpRequest

# Create your views here.

def near_hundred(request: HttpRequest, n) -> HttpResponse:
    if (n >= 90 and n <= 100) or (n >= 190 and n <= 200):
        return HttpResponse(True)
    if (n >= 100 and n <= 110) or (n >= 200 and n <= 210):
        return HttpResponse(True)
    else:
        return HttpResponse(False)

def string_splosion(request: HttpRequest, str)-> HttpResponse:
    result = ""
    for i in range(len(str)):
        result = result + str[:i+1]
    return HttpResponse(result)

def cat_dog(request: HttpRequest, word)-> HttpResponse:
    return HttpResponse(word.count("cat") == word.count("dog"))



def lone_sum(request: HttpRequest, a, b, c):
    if a == b == c:
        return HttpResponse(0)
    elif a == b:
        return HttpResponse(c)
    elif a == c:
        return HttpResponse(b)
    elif b == c:
        return HttpResponse(a)
    else:
        return HttpResponse(a + b + c)
