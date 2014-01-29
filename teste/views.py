from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from teste.models import Jogador, Estrategia


# Create your views here.
def pagina_inicial(request):
    c = {}
    c.update(csrf(request))
    template = "inicial.html"
    estrategias = []
    if request.method == 'GET':
        estrategias = Estrategia.objects.all()

    elif request.method == 'POST':
        autor = request.POST["autor"]
        codigo = request.POST["codigo"]
        nome = request.POST["nome"]
        estrategia = Estrategia(codigo=codigo, nome=nome, autor=Jogador.objects.get(id=autor))
        estrategia.save()
    return render_to_response(template, {"estrategias": estrategias})


class EstrategiaCreate(CreateView):
    model = Estrategia
    fields = ['codigo', 'autor', 'nome']



class EstrategiaUpdate(UpdateView):
    model = Estrategia
    fields = ['codigo', 'autor', 'nome']


class EstrategiaDelete(DeleteView):
    model = Estrategia
    success_url = reverse_lazy('autor-list')