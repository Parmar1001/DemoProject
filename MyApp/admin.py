from django.contrib import admin
from .models import Customer,Branch

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=['customer_id','user_name','date_of_open','balance','account_type','branch_name','phonenum']

class BranchAdmin(admin.ModelAdmin):
    list_display=['name','city','state']


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Branch,BranchAdmin)

