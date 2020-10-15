from django.shortcuts import render, redirect
from items.models import Item, Category, Tag
from items.forms import *
from django.views.generic import ListView

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


def categories_feed(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'items/categories_feed.html', context)


def categories_edit(request, pk):
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('items:categories_feed')
    context = {
        'form': form
    }
    return render(request, 'items/category_form.html', context)


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
