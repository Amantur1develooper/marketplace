from django.contrib import admin
from shop.views.homepage import homepage
from shop.views.darail import datail
from django.urls import path, include 
from shop.views.cart import cart, addToCard
from shop.views.register1 import register
from shop.views.signin import signin
from shop.views.cart import remove_from_cart
from shop.views.signout import signout
from shop.views.cartAdd import cartAdd
from shop.views.pr_category import pr_category
from shop.views.search import search
from shop.views.order import order
# from django.views.generic. import TemplateView
from .views.register import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('detail/<int:pk>' , datail, name='datail'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('cart/',cart, name='cart'),
    path('register',register,name='register'), #регимтрация
    path('signin',signin,name='signin'),
    path('signout',signout,name='signout'),
    path('addToCard/<int:pk>', addToCard,name=' addToCard'),
    # path('delete/<int:id>',delete,name='delete'),
    path('remove_from_cart/<int:pk>', remove_from_cart, name='remove_from_cart'),
    path('category/<int:pk>',pr_category, name='pr_categoty'),
    path('SEARCH',search,name='search'),
    path('order',order,name='order')
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('signup/', SignUpView.as_view(), name='signup'),

]