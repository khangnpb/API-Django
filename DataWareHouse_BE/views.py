from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from DataWareHouse_BE.models import DetailCustomer,DimCustomer,DimProduct,FactEcommerceSales,DimStore
from DataWareHouse_BE.serializers import DetailCustomerSerializer,DimCustomerSerializer,DimProductSerializer,DimStoreSerializer,FactEcommerceSalesSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def DetailCustomerApi(request,id=0):
    if request.method=='GET':
        detail_customers = DetailCustomer.objects.all()
        detail_customers_serializer=DetailCustomerSerializer(detail_customers,many=True)
        return JsonResponse(detail_customers_serializer.data,safe=False)
    
def DimCustomerApi(request,id=0):
    if request.method=='GET':
        dim_customers = DimCustomer.objects.all()
        dim_customers_serializer=DimCustomerSerializer(dim_customers,many=True)
        return JsonResponse(dim_customers_serializer.data,safe=False)
    
def DimProductApi(request,id=0):
    if request.method=='GET':
        dim_product = DimProduct.objects.all()
        dim_product_serializer=DimProductSerializer(dim_product,many=True)
        return JsonResponse(dim_product_serializer.data,safe=False)
    
def DimStoreApi(request,id=0):
    if request.method=='GET':
        dim_store = DimStore.objects.all()
        dim_store_serializer=DimStoreSerializer(dim_store,many=True)
        return JsonResponse(dim_store_serializer.data,safe=False)
    
def FactEcommerceSalesApi(request,id=0):
    if request.method=='GET':
        fact_ecommerce_sales = FactEcommerceSales.objects.all()
        fact_ecommerce_sales_serializer=FactEcommerceSalesSerializer(fact_ecommerce_sales,many=True)
        return JsonResponse(fact_ecommerce_sales_serializer.data,safe=False)
    
