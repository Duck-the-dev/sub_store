from django.contrib import admin
from .models import product

admin.site.register(product)
admin.site.site_header = 'WOODENIA'
admin.site.site_title = 'WOODENIA'
