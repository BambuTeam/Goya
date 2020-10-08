from django.shortcuts import render, redirect
from inventoryLoads.models import *
from inventoryLoads.forms import *
from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.


def provider_feed(request):
    providers = Provider.objects.all()
    paginator = Paginator(providers, 20)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {
        'providers':providers,
        'page_object':page_object
    }
    return render(request, 'inventoryLoads/provider_feed.html', context)


def provider_new(request):
    form = ProviderForm()
    if request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('inventoryLoads:inventory_provider')
    context = {
        'form':form,
    }
    return render(request, 'inventoryLoads/provider_form.html', context)


def provider_edit(request, pk):
    provider = Provider.objects.get(id = pk)
    form = ProviderForm(instance=provider)
    if request.method=='POST':
        form = ProviderForm(request.POST, instance=provider)
        if form.is_valid():
            form.save()
            return redirect('inventoryLoads:inventory_provider')
    context = {
        'form':form
    }
    return render(request, 'inventoryLoads/provider_form.html', context)


def inventoryload_feed(request):
    inventory = InventoryLoad.objects.all()
    paginator = Paginator(inventory, 20)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {
        'providers': inventory,
        'page_object': page_object
    }
    return render(request, 'inventoryLoads/inventori_feed.html', context)