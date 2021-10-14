from django.db import models

class Customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100, blank=True, null=True)
    phone=models.CharField(max_length=20, blank=True, null=True)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=30, blank=True, null=True)
    address=models.CharField(max_length=255,blank=True,null=True)
    # price=models.IntegerField()
    def register(self): #сохранить данные
        self.save()
    
    def __str__(self):
        return self.first_name
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.oblects.filter(email=self.email):
            return True
        return False