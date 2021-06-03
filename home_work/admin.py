from django.contrib import admin

# Register your models here.
from home_work.models import Category, Product, Review


class Product_Admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'categorys']
    search_fields = ['title']
    list_filter = ['categorys']
    list_editable = ['categorys', 'title']


admin.site.register(Category, )
admin.site.register(Product, Product_Admin)
admin.site.register(Review)
