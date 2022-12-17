from django.shortcuts import render, redirect
from entregas.models import EntregaCliente, EntregaExterna
from entregas.forms import EntregaClienteForm, EntregaExternaForm

# Create your views here.

#inicioadmin ?

def entregaExterna(request):
    titulo= "Entrega Cliente Externo"
    context={
    'titulo':titulo
    }
    return render(request,'entregas/entregas.html',context)


def entregaExterna_crear(request):
    titulo = "Entrega -  Externa - Crear "
    if request.method == "POST":
        form= EntregaExterna(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entregaExternas')  #
        else:
            print ("Error al Guardar ")
    else:
        form= EntregaExternaForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return (request,'partials/crear.html',context)


def entregaCliente(request):
    titulo= "Entrega - Cliente"
    entregaCliente = EntregaCliente.objects.all()
    context={
    'titulo':titulo
    }
    return render(request,'entregas/recepcion.html.html',context)


def entregaCliente_crear(request):
    titulo = "Entrega - Cliente - Crear "
    if request.method == "POST":
        form= EntregaCliente(request.POST)  #form
        if form.is_valid():
            form.save()
            return redirect('entregaClientes')  #
        else:
            print("Error al Guardar")
    else:
        form= EntregaClienteForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'partials/crear.html',context)  #crear


def entregaCliente_editar(request, pk):
    titulo ="Entrega - Cliente - Editar"
    entregaCliente= EntregaCliente.objects.get(id=pk)
    if request.method == "POST":
        form= EntregaCliente(request.POST, instance=entregaCliente)
        if form.is_valid():
            form.save()
            return redirect('entregaCliente')
        else:
            print("Error al guardar la edición")
    else:
        form= EntregaCliente(instance= EntregaCliente)
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'partials/crear.html',context)


def entregaCliente_eliminar(request, pk):
    titulo = "entregaCliente - Eliminar"
    entregaCliente = EntregaCliente.objects.all()

    EntregaCliente.objects.filter(id=pk).update(
        estado='0'
    )
    return redirect('entregaCliente')

    context = {
        'entregaCliente': entregaCliente,
        'titulo': titulo,

    }
    return render(request, '', context)  #entregaCliente/entregaCliente.html


#####
######






