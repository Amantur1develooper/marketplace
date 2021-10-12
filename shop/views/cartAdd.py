from django.shortcuts import render
from shop.models.product import Product
from shop.models.category import Category


products=[]

def cartAdd(request,pk):
    product_pk=Product.objects.get(pk=pk)
    products.append(product_pk)
    return render(request, 'cart.html',{'products':products} )