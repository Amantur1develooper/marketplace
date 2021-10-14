from django.shortcuts import render,redirect
from ..models.product import Product
from ..views import category
from django.db.models import Count

def search(request):
    if request.method=='POST':
        searched_product_from_input=request.POST.get('searched_product')
        print(searched_product_from_input)
        searchedproducts=Product.objects.filter(name__contains=searched_product_from_input)
        categories=category.Category.objects.all().annotate(products_count=Count('product'))
        products=Product.objects.all()
        return render(request,'search.html',{'search_product_from_input':searched_product_from_input,'categories':categories,'all_products':products,
        'searched_products':searchedproducts})

