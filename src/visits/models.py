from django.db import models

# Create your models here.
class PageVisit(models.Model):
    #creating a db
    #track what pages visited and when visited 

    #id prim key 
    path = models.TextField(blank=True, null=True) #col
    timestamp = models.DateTimeField(auto_now_add=True) #col
    pass