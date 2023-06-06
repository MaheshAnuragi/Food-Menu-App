from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name   #it will return item_name instead of object 

    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)  # it used for connection of User model to item model after that
                                                                            # if user add any food item then that name will show as well.
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=500)
    item_price = models.IntegerField()
    item_img = models.CharField(max_length=1000,default='https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg')

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
    