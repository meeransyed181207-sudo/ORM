from django.db import models
from django.contrib import admin
class product(models.Model):
    productName=models.CharField(max_length=30)
    productID=models.CharField(primary_key=True,max_length=7)
    category=models.CharField(max_length=12)
    description=models.CharField(max_length=400)
    stock=models.IntegerField()
    price=models.IntegerField()

class productAdmin(admin.ModelAdmin):
    list_display=["productName","productID","category","description","stock","price"]
    actions_on_bottom=True
    action_on_top=False
    list_display_links=["productID"]
    list_filter=["category"]