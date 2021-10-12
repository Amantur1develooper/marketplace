from django.shortcuts import render
from ..models import product
from ..models import category
from ..models import Customer
from django.views.generic import TemplateView
from django.db.models import Count

def homepage(request):
    products = product.Product.objects.all()
    categories = category.Category.objects.all()
    customers = Customer.Customer.objects.all()

    categories = category.Category.objects.all().annotate(products_count=Count('product'))

    return render(request, 'base.html', {'categories':categories, 'customers':customers, 'products':products, 'all_products':products})


class HomePageView(TemplateView):
    template_name = 'base.html'