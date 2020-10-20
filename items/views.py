from django.shortcuts import render, redirect
from items.models import Item, Category, Tag
from items.forms import *
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.o


class ItemsListView(ListView):
    template_name = 'items/feed.html'
    model = Item
    paginate_by = 10
    context_object_name = 'items'


def item_new(request):
    item_form = ItemForm()
    if request.method == 'POST':
        item_form = ItemForm(request.POST)
        if item_form.is_valid():
            item_form.save()
            return redirect('')
    context = {
        'form': item_form,
    }
    return render(request, 'items/new_item.html', context)


def item_update(request, pk):
    item = Item.objects.get(id=pk)
    item_form = ItemForm(instance=item)
    if request.method == 'POST':
        item_form = ItemForm(request.POST, request.FILES, instance=item)
        if item_form.is_valid():
            item_form.save()
            return redirect('items:items_feed')
    context = {
        'form': item_form,
    }
    return render(request, 'items/new_item.html', context)

@login_required
def categories_feed(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'items/categories_feed.html', context)


class CategoryEdit(LoginRequiredMixin, UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'items/category_edit.html'
    success_url = reverse_lazy('items:categories_feed')    


class CategoryCreate(LoginRequiredMixin, CreateView):
    template_name = 'items/category_new.html'
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('items:categories_feed')    


def items_dashboard(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    tags_coutn = Tag.objects.all().annotate(item_count=models.Count('item'))
    context = {
        'items': items[:10],
        'categiries': categories[:10],
        'tags': tags_coutn
    }
    return render(request, 'items/dashboard.html', context)
