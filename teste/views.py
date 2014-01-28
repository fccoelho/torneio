from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.
def pagina_inicial(request):
    template = "inicial.html"
    return render_to_response(template)