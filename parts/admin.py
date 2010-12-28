# encoding: utf-8

from parts.models import *
from django.contrib import admin


class LineItemInline(admin.TabularInline):
    model = LineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [LineItemInline]
    list_display = ('order_num', 'distributor', 'order_date')
    

class OrderInline(admin.TabularInline):
    model = Order


class DistributorAdmin(admin.ModelAdmin):
    inlines = [OrderInline]


class PartAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'part_num', 'description', 'value')


class DistributorPartAdmin(admin.ModelAdmin):
    list_display = ('distributor', 'part')



admin.site.register(Distributor,)
admin.site.register(Classification)
admin.site.register(StorageLocation)
admin.site.register(Part)
admin.site.register(DistributorPart)
admin.site.register(Order)
