from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from .forms import CategoryForm, ProductForm
from .models import Category, Product, Shop

def main_page(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories' : categories,
        'products' : products
    }
    return render(request, 'main_page.html', context)

def category_sort(request, id):
    categories = Category.objects.all()
    products=Product.objects.filter(categories=id)
    context = {"products": products, 'categories': categories}
    return render(request, 'categories_products.html', context)

def product_detail(request, id):
    product = Product.objects.get(id = id)
    z = product.shop_set.all()
    products_in_shop = Product.objects.filter(shop__name = 'Алми')
    print(products_in_shop, 'продукты в магазине (Алми)')
    shops_for_products = Shop.objects.filter(products__title = 'BMW')
    print(shops_for_products, 'магазины с BMW')
    context = {
        'product': product,
        'shops': z,
    }
    return render(request, "product_detail.html", context)

def less_forms(request):
    cati = Category.objects.all()
    prod = Product.objects.all()
    shops = Shop.objects.all()
    form = CategoryForm()
    context = {
        'cati': cati,
        'prod': prod,
        'shops': shops,
        'form': form,
    }


    return render(request, 'less_forms.html', context)

def category_form(request):
    Category.objects.create(name = request.POST.get('category'))
    return redirect('main:less_forms')

def product_form(request):
    cati = Category.objects.all()
    prod = Product.objects.all()
    shops = Shop.objects.all()
    form = CategoryForm()
    context = {
        'cati': cati,
        'prod': prod,
        'shops': shops,
        'form': form,
    }
    print(request.POST)
    Product.objects.create(title=request.POST.get('product'),
                           description=request.POST.get('description'),
                           price=request.POST.get('price'),
                           image=request.POST.get('image'),
                           categories=Category.objects.get(name = request.POST.get('categories')))

    return render(request, 'less_forms.html', context)


def shop_form(request):
    prod = Product.objects.all()
    context = {
        'prod': prod,
    }
    print(prod)
    a = Shop.objects.create(name = request.POST.get('shop'),
                        city = request.POST.get('city'),
                        street = request.POST.get('street'))
    produ = request.POST.getlist('shop_products')
    for i in prod:
        for j in produ:
            if j == i.title:
                a.products.add(Product.objects.get(title = j))
    print(request.POST.getlist('shop_products'))
    return render(request, 'less_forms.html', context)

def form_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.errors)
    # return redirect('main:less_forms')
    context = {
        'form': form,
    }
    return render(request, 'errors_form.html', context)

def form_model(request):
    form = ProductForm()
    context = {
        'form':form,
    }
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return render(request, 'model_form.html', context)


