from django.shortcuts import render,redirect
# from django.shortcuts import render get_object_or_404
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# from ..models import product
from django.http import HttpResponseRedirect
# from models.product import Product
# from shop.models.product import Product
from ..models import product



def cart (request):
    cart_session=request.session.get('cart_session',[])
    products_cart= product.Product.objects.filter( id__in =cart_session)
    all_products_count = len(cart_session)
    summ=[]
    for i in cart_session:
        if i in summ:
            continue
        else:
            summ.append(i)
    # summ1=0
    # for p in summ:
    #     summ1+=p
    price=0
    for product_cart in products_cart :
        product_cart.count= cart_session.count(product_cart.id)
        product_cart.sum=product_cart.count * product_cart.price
        price +=  product_cart.sum

    # price= product.Product.objects.filter( id__in =cart_session)
    # price=0
    # for i in cart_session:
        # print(i)
    # print(products_cart[0])
    # print(price)
    # request.session['cart_session']=
    # product_pk=product.Product.objects.get(pk=pk)
    # product1=product.Product.objects.all()
    return render(request,'cart.html',{'products':products_cart,'cart_session':cart_session,"products_cart":products_cart,'summ':sum,'all':all_products_count,"price":price})


def addToCard(request,pk):
    cart_session=request.session.get('cart_session',[])
    cart_session.append(pk)
    request.session['cart_session']= cart_session
    return redirect('/')

# def remo
def remove_from_cart(request, pk):
    cart = request.session.get('cart_session',[])
    new_cart=[]
    for fk in cart:
        if fk != pk:
            new_cart.append(fk)
   
    request.session['cart_session']=new_cart
    return redirect('cart')