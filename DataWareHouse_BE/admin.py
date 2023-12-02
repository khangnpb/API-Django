from django.contrib import admin
from .models import DetailCustomer,DimCustomer,DimProduct,DimStore,FactEcommerceSales

admin.site.register(DetailCustomer)
admin.site.register(DimCustomer)
admin.site.register(DimProduct)
admin.site.register(DimStore)
admin.site.register(FactEcommerceSales)
