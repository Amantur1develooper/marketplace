from django.db import models

class Customer(models.Model):
    first_name=models.CharField(max_length=100)
    # last_name=models.CharField(max_length=100)
    # phone=models.CharField(max_length=20)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=30)

    def register(self): #сохранить данные
        self.save()
    
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