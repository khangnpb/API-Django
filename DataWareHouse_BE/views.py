from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.db.models.functions import ExtractYear
from django.db.models import Count

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view

from DataWareHouse_BE.models import DetailCustomer,DimCustomer,DimProduct,FactEcommerceSales,DimStore
from DataWareHouse_BE.serializers import DetailCustomerSerializer,DimCustomerSerializer,DimProductSerializer,DimStoreSerializer,FactEcommerceSalesSerializer

from django.core.files.storage import default_storage

from datetime import datetime

# Create your views here.

# if you need to pass the CSRF protection for POST method, using this decorator: @csrf_exempt
@csrf_exempt
@api_view(['GET', 'POST'])
def DetailCustomerApi(request,id=0):
    # if request.method=='GET':
    #     detail_customers = DetailCustomer.objects.all().count()
    #     detail_customers_serializer=DetailCustomerSerializer(detail_customers,many=True)
    #     return JsonResponse(detail_customers_serializer.data,safe=False)
    
    if request.method=='GET':
        detail_customers = DetailCustomer.objects.all().count()
        # detail_customers_serializer=DetailCustomerSerializer(detail_customers,many=True)
        return JsonResponse(detail_customers,safe=False)
    
    # this function used for retrieve sum of customer between fromDate, toDate #
    ## ------- Format: fromDate, toDate: 'YYYY-MM-DD' ------- ##
    elif request.method == 'POST':
        try:
            # export data receiving from Frontend
            fromDate_str = request.data.get('fromDate')
            toDate_str = request.data.get('toDate')

            # Convert date strings to datetime objects
            fromDate = datetime.strptime(fromDate_str, '%Y-%m-%d').strftime('%Y-%m-%d')
            toDate = datetime.strptime(toDate_str, '%Y-%m-%d').strftime('%Y-%m-%d')

            # get sum of customer between fromDate and toDate
            sum_customers = DetailCustomer.objects.filter(customer_since__range=(fromDate, toDate)).count()
            return Response({'sum_customers': sum_customers})
        except:
            return Response({'error': 'Invalid request method'}, status=400)

        # serializer = DetailCustomerSerializer(data=data)

        # if serializer.is_valid():
        #     fromDate = serializer.validated_data.get('fromDate')
        #     toDate = serializer.validated_data.get('toDate')

        #     sum_customers = DetailCustomer.objects.filter(customer_since__range=(fromDate, toDate)).count()
        #     return Response({'sum_customers': sum_customers})
        # else:
        #     return Response({'error': serializer.errors}, status=400)

@api_view(['GET'])
def customerCountByGender(request,id=0):
    # if request.method=='GET':
    male_customers = DetailCustomer.objects.filter(gender='Nam').count()
    female_customers = DetailCustomer.objects.filter(gender='Nữ').count()
    # detail_customers_serializer=DetailCustomerSerializer(detail_customers,many=True)
    return JsonResponse([{'gender': 'male', 'count': male_customers}, {'gender': 'male', 'count': female_customers}],safe=False)

@api_view(['GET'])
def customerCountByAge(request,id=0):
    # Assuming your birthday field is a DateField or DateTimeField
    # Also, assuming the format is %YYYY-%MM-%DD
    current_year = datetime.now().year

    # Calculate the birth year and age
    customers_by_age = (
        DetailCustomer.objects.annotate(
            # birth_year=ExtractYear('birthday'),
            age=current_year - ExtractYear('birthday')
        )
        .values('age')
        .annotate(count=Count('customer_key'))
        .order_by('age')
    )

    # Convert the queryset to a list for JSON serialization
    result_list = list(customers_by_age)

    return JsonResponse(result_list, safe=False)

@csrf_exempt
@api_view(['GET'])
def customerCountByOccupation(request,id=0):
    customers_by_occupation = (
        DetailCustomer.objects.values('occupation')
        .annotate(count=Count('customer_key'))
        .order_by('occupation')
    )

    result_list = list(customers_by_occupation)

    return JsonResponse(result_list, safe=False)

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
        # fact_ecommerce_sales = FactEcommerceSales.objects.get(order_key=334324)
        fact_ecommerce_sales_serializer=FactEcommerceSalesSerializer(fact_ecommerce_sales,many=True)
        return JsonResponse(fact_ecommerce_sales_serializer.data,safe=False)
    
