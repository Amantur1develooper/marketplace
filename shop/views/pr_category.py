# from ..models.product import Product
# from ..models.category import Category 
# # from django.shortcurts import render
# from django.shortcuts import render,redirect
# from django.db.models import Count
# def pr_category(request,pk):
#     products=Product.objects.filter(category=pk)
#     categories=Category.objects.all().annotate(products_cout=Count('products'))
#     # products_count= Category.objects.all().annotate(Count('product'))
#     # s=Category.objects.all().annotate[products_count=Count('product')]
#     # all_products=
    
#     # for i in categories:
#         # d+=i.products_count

#         # countcategory+=1

#     return render(request,'base.html',{'products':products,'categories1':categories,'all_products':products,})
from ..models.product import Product
from django.shortcuts import render
from ..models.category import Category
from django.db.models import Count

def pr_category(request, pk):
    
    all_products = Product.objects.all()
    products = Product.objects.filter(category=pk)
    categories = Category.objects.all().annotate(products_count=Count('product'))

    return render(request, 'base.html', {'products': products, 'categories':categories, 'all_products': all_products})