from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Habitacion, Pais, TipoHab
from django.views import generic
from . forms import ClienteForm, PaisForm, HabitacionForm

# Create your views here.

def index(request):
    num_clientes = Cliente.objects.all().count()
    num_habitaciones = Habitacion.objects.all().count()
    
    return render(
        request,
        'index.html',
        context = {'numero de clientes: ': num_clientes, 'numero de habitaciones: ': num_habitaciones},
    )
    
def habitacion(request):
    num_clientes = Cliente.objects.all().count()
    num_habitaciones = Habitacion.objects.all().count()
    
    return render(
        request,
        'habitacion.html',
        context = {'numero de clientes: ': num_clientes, 'numero de habitaciones: ': num_habitaciones},
    )
    
def registrarse(request):
    n_clientes = Cliente.objects.all().count()
    
    return render(
        request,
        'registrarse.html',
        context = {'numero de clientes: ': n_clientes},
    )
    
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect

#CLIENTE

class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('index')
    template_name = 'CRUD/cliente_confirm_delete.html'
    
class ClienteDetailView(generic.DetailView):
    model = Cliente
    template_name = 'CRUD/cliente_detail.html'

class ClienteListView(generic.ListView):
    model = Cliente
    template_name = 'CRUD/cliente_list.html'
    queryset = Cliente.objects.all()

    paginate_by = 10

def cliente_nuevo(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = ClienteForm()
        return render(request, 'CRUD/cliente_form.html', {'form': form})

def cliente_editar(request, pk):
    post = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('cliente-detail', pk=post.pk)
    else:
        form = ClienteForm(instance=post)
    return render(request, 'CRUD/cliente_form.html', {'form': form})

#HABITACION

class HabitacionDeleteView(DeleteView):
    model = Habitacion
    success_url = reverse_lazy('index')
    template_name = 'CRUD/habitacion_confirm_delete.html'
    
class HabitacionDetailView(generic.DetailView):
    model = Habitacion
    template_name = 'CRUD/habitacion_detail.html'

class HabitacionListView(generic.ListView):
    model = Habitacion
    template_name = 'CRUD/habitacion_list.html'
    queryset = Habitacion.objects.all()

    paginate_by = 10

def habitacion_nuevo(request):
    if request.method == "POST":
        form = HabitacionForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = HabitacionForm()
        return render(request, 'CRUD/habitacion_form.html', {'form': form})

def habitacion_editar(request, pk):
    post = get_object_or_404(Habitacion, pk=pk)
    if request.method == "POST":
        form = HabitacionForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('habitacion-detail', pk=post.pk)
    else:
        form = HabitacionForm(instance=post)
    return render(request, 'CRUD/habitacion_form.html', {'form': form})