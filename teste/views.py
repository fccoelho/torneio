from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from teste.models import Jogador, Estrategia


# Create your views here.
def pagina_inicial(request):
    template = "inicial.html"
    if "autor" in request.GET:
        autor = request.GET["autor"]
    return render_to_response(template, {"autor":autor})

class EstrategiaCreate(CreateView):
    model = Estrategia
    fields = ['codigo', 'autor']

class EstrategiaUpdate(UpdateView):
    model = Estrategia
    fields = ['codigo', 'autor']

class EstrategiaDelete(DeleteView):
    model = Estrategia
    success_url = reverse_lazy('autor-list')