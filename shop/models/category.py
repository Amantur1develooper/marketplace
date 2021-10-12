from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    # def register(self): #сохранить данные
        # self.save()

    def get_all_categories(self):
        return Category.objects.all()

