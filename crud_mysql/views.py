from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm
# Create your views here.

def admin(request):
    return render(request, 'admin')

def inicio(request):
    return render(request, 'formularios/inicio.html')

def nosotros(request):
    return render(request, 'formularios/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def crear(request):
    formulario = LibroForm(request.POST or None,  request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        print("Formulario si cumplió")
        return redirect('libros')
    else:
        print("Formulario no cumplió")
    return render(request, 'libros/crear.html', {'formulario': formulario})

def editar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario': formulario})

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')
