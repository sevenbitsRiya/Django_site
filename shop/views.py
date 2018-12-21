from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator
from django_filters.views import FilterView
from .forms import FilterForm
#from shop.filters import PriceFilter
#from decimal import Decimal as D

def home(request):
    return render(request,'shop/product/index.html')

def search(request):
    try:  
        q = request.GET.get('search-product')
    except:
        q = None
    if q:
        products = Product.objects.filter(slug__icontains=q)
        context = {'query': q, 'products': products}    
        template = 'shop/product/list.html'
    else:   
        context = {'query': q}      
        template = 'shop/product/list.html'
    return render(request, template, context)

def sort(request):
    form = FilterForm(request.POST or None)
    answer = ''
    if form.is_valid():
        answer = form.cleaned_data.get('sorting1')
        l2h = Product.objects.order_by('price')
        h2l = Product.objects.order_by('-price')
    
    context = {'l2h':l2h, 'h2l':h2l, 'answer':answer}
    template = 'shop/product/list.html'
    return render(request, template, context)

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    paginator = Paginator(products, 9)
    page =  request.GET.get('page')
    products = paginator.get_page(page) 
   
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
        paginator = Paginator(products, 9)
        page =  request.GET.get('page')
        products = paginator.get_page(page) 

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
     
    return render(request, 'shop/product/list.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)
