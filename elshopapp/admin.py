from django.contrib import admin
from .models import *
# Register your models here.


class ImagesTublerInline(admin.TabularInline):
    model = Images

class TagTublerInline(admin.TabularInline):
    model = Tag

class ProductAdmin(admin.ModelAdmin):
    inlines=[ImagesTublerInline,TagTublerInline]



class OrderItemTublerInline(admin.TabularInline):
    model=OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTublerInline]
    list_display=['first_name','phone','email','payment_id','paid','date']
    search_field=['first_name','email','payment_id']

admin.site.register(Contact)
admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Filter_Price)
admin.site.register(color)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images)
admin.site.register(Tag)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Profile)
admin.site.register(AddressMod)
