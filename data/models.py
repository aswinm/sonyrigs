from django.db import models

class Category(models.Model):

    def __unicode__(self):
        return self.name
        
    name = models.CharField(max_length=150)
    url = models.CharField(max_length=150,primary_key=True)

class Product(models.Model):
    def __unicode__(self):
        return self.name

    url = models.CharField(max_length=150,primary_key=True)
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="prodimages")
    desc = models.TextField(max_length=5500)
    cat = models.ForeignKey(Category)





# Create your models here.
