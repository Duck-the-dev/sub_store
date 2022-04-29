from django.contrib import admin
from .models import Product

admin.site.register(Product)
admin.site.site_header = 'WOODENIA'
admin.site.site_title = 'WOODENIA'
