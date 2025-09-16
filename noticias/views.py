from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Noticia

class NoticiaListaView(ListView):
    model = Noticia
    template_name = "noticias/lista.html"
    context_object_name = "noticias"
    paginate_by = 5

    def get_queryset(self):
        return Noticia.objects.filter(publicado=True)

class NoticiaDetalleView(DetailView):
    model = Noticia
    template_name = "noticias/detalle.html"
    context_object_name = "noticia"

