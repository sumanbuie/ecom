from django.contrib import admin
from .models import *

admin.site.register(Castomer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


# https://developer.paypal.com/demo/checkout/#/pattern/style ->paypal c link
# https://www.sandbox.paypal.com/  -> sandbox account