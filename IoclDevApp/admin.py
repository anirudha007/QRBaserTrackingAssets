from django.contrib import admin

# Register your models here.
from . models import *

# admin.site.register(Customer)
# admin.site.register(Transiction)
#admin.site.register(Device_Info)
#admin.site.register(MainFeed)
#admin.site.register(PaymentStatus)

@admin.register(Transiction)
class TransationTable(admin.ModelAdmin):
    list_display = Transiction.DisplayFields
    search_fields = Transiction.SerchFilds
    list_filter = Transiction.FilterFilds

@admin.register(Qrdatatable)
class TransationTable(admin.ModelAdmin):
    list_display = Qrdatatable.DisplayFields
    search_fields = Qrdatatable.SerchFilds
    list_filter = Qrdatatable.FilterFilds