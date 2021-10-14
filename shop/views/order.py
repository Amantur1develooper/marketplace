from django.shortcuts import render,redirect
from ..models.product import Product
# from ..views import category
from django.contrib import messages
from ..models.Customer import Customer
from ..models.order import Order
def order(request):
    if request.method=="POST":
        cart_session=request.session.get('cart_session',[])
        if len(cart_session)==0:
            messages.error(request,'Ваша корзина пуста',extra_tags='danger')
            return redirect('cart')
        else:
            customer=Customer()
            customer.first_name=request.POST.get('c_name')
            customer.last_name=request.POST.get('c_lname')
            customer.phone=request.POST.get('c_phnumber')
            customer.email=request.POST.get('c_email')
            customer.address=request.POST.get('c_address')
            customer.save()

            for i in range(len(cart_session)):
                order=Order()
                order.product=Product.objects.get(id=cart_session[i])
                order.customer=customer
                order.price=order.product.price
                order.phone=customer.phone
                order.address=customer.address
                order.save()

            request.session['cart_session']=[]

            messages.error(request,'Success!',extra_tags='success')
            return redirect('cart')

