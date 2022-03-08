from django.contrib import admin
from .models import Customer, Branch

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "customer_id",
        "user",
        "date_of_open",
        "balance",
        "account_type",
        "branch_name",
        "phonenum",
    ]


class BranchAdmin(admin.ModelAdmin):
    list_display = ["branch_name", "branch_city", "branch_state"]


# class ContactAdmin(admin.ModelAdmin):
#     list_display=['full_name','email','message','date']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Branch, BranchAdmin)
# admin.site.register(Contact,ContactAdmin)
