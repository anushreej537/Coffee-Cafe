from django.db import models


class Coffee(models.Model):
    coffee_name = models.CharField(max_length = 255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.CharField(max_length = 2083)

    def __str__(self):
        return self.coffee_name
    
class User(models.Model):
    name = models.CharField(max_length = 250)
    email = models.EmailField(max_length = 300)
    coffee = models.ForeignKey(Coffee,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
