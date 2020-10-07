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
            return redirect ('inventoryLoads:inventory-provider')
    context = {
        'form':form,
    }
    return render(request, 'inventoryLoads/provider_form.html', context)