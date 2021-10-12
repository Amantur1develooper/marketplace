from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponseRedirect
from shop.models.product import Product


def delete(request,id):
    
    try:
        todo=Product.objects.get(id=id)
        todo.delete()
        return HttpResponseRedirect('/')
    except Product.DoesNotExist:
        return HttpResponseNotFound()