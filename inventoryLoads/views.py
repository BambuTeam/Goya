from django.shortcuts import render, redirect
from inventoryLoads.models import *
from inventoryLoads.forms import *
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
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
    return render(request, 'inventoryLoads/inventory_feed.html', context)


def inventoryLoad_detail (request, pk):
    Inventoryload = InventoryLoad.objects.get(id = pk )
    detail_list = Inventoryload.inventoryloaddetail_set.all()

    paginator = Paginator(detail_list, 20)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {
        'inventoryload': Inventoryload,
        'page_object': page_object
    }
    return render(request, 'inventoryLoads/inventory_description.html', context)


def inventoryLoad_new(request):
    form = InventoriLoadForm()
    if request.method == 'POST':
        form = InventoriLoadForm(request.POST)
        if form.is_valid():
            form.save()
            redirect ('inventoryLoads:inventory_lodad_feed')
    context = {
        'form':form

    }
    return render(request, 'inventoryLoads/inventoryload_form.html', context)


class InventoryCreateview(CreateView):
    model = InventoryLoad
    fields = '__all__'

    def get_context_data(self, **kwargs):
        # we need to overwrite get_context_data
        # to make sure that our formset is rendered
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["children"] = ChildFormset(self.request.POST)
        else:
            data["children"] = ChildFormset()
        return data
    def form_valid(self, form):
        context = self.get_context_data()
        children = context["children"]
        self.object = form.save()
        if children.is_valid():
            children.instance = self.object
            children.save()
        return super().form_valid(form)
    def get_success_url(self):
        return reverse("parents:list")



