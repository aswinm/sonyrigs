from django.contrib import admin
from data.models import Category,Product

class CatAdmin(admin.ModelAdmin):
    pass

class ProdAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category,CatAdmin)
admin.site.register(Product,ProdAdmin)
