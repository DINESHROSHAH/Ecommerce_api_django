from django.contrib import admin
from .models import usersInfo,product,orders


class usersInfoAdmin(admin.ModelAdmin):
    list_dispaly=("username","password","Email","mobile_number",)

class productAdmin(admin.ModelAdmin):
    list_display=("id","ProductName","ProductCatageries","ProductDescription","Price","created_at")


class ordersAdmin(admin.ModelAdmin):
    list_display=("productid","userid","quantity","totalamount","created_at",)

admin.site.register(usersInfo,usersInfoAdmin)
admin.site.register(product,productAdmin)
admin.site.register(orders,ordersAdmin)