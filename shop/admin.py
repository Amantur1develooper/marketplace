# from django.contrib import admin
from django.utils.safestring import mark_safe

# # Register your models here.
# from .models.Customer import Customer
# from .models.category import Category
# from .models.order import Order
# from .models.product import Product
# class CategoryAdmin(admin.ModelAdmin):
#     list_display=['name',]
# class CustomerAdmin(admin.ModelAdmin):
#     list_display=['first_name','last_name','phone','email','password']
#     # search_fields=('name','doctors','region')
#     # list_editable=('name','doctors') 
#     # list_filter=('name','region')

# class OrderAdmin(admin.ModelAdmin):
#     list_display=['customer','quantity','phone','price','address','date','status']

# class ProductAdmin(admin.ModelAdmin):
#     list_display=['name','price','category','description','image']

# admin.site.register(Product,ProductAdmin)

# admin.site.register(Customer,CustomerAdmin)

# admin.site.register(Category,CategoryAdmin)
# admin.site.register(Order, OrderAdmin)
# def show_image(self, img_obj):
#     if img_obj.image:
#         return mark_safe("<img width=60 src={}/>".format(img_obj.image.url))
from django.contrib import admin
from .models.category import Category
from .models.Customer import Customer
# from .models.Customer import Customer
from .models.order import Order
from .models.product import Product
from django.utils.safestring import mark_safe



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'phone','address']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','customer', 'quantity', 'price', 'address', 'date']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'description', 'show_img']

    def show_img(self, img_objects):
        if img_objects.image:
            return mark_safe("<img width=80px src='{}'/>".format(img_objects.image.url))
        return None
    show_img.__name__='Изображение'



admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)