from django.shortcuts import render, HttpResponse

# Create your views here.
def Hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello, {nome}! Bom saber que voce tem {idade} anos de idade.</h1>')

def Soma(request, n1, n2):
    res = n1 + n2
    return HttpResponse(f'<h1>O resultado é: {res}</h1>')