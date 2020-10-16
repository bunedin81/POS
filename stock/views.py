from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm, UpdateProductForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    #paginator = Paginator(products, 10)

    #page = request.GET.get('page')
    #items = paginator.get_page(page)

    context = {
        'products': products
    }
    return render(request, 'stock/product_list.html', context)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            new_product = form.save()
        return HttpResponseRedirect('/stock/product_list/')
    form = ProductForm()
    return render(request, 'stock/product_create.html', {'form': form})


def update_product(request):
    if request.method == 'POST' and 'id' in request.POST:
        item = get_object_or_404(Product, pk=request.POST.get('id'))
        form = UpdateProductForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
    elif request.method == 'GET':
        item = get_object_or_404(Product, pk=request.GET.get('id'))
        form = ProductForm(instance=item)
        return render(request, 'stock/product_update.html', {'form': form})
    return HttpResponseRedirect('/stock/product_list')

