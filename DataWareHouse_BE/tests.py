from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime
import json

from DataWareHouse_BE.models import DetailCustomer

class DetailCustomerApiTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Create 2 DetailCustomer objects
        DetailCustomer.objects.create(
            customer_since=datetime.strptime('2020-01-01', "%Y-%m-%d"),
            first_name='John',
            last_name='Doe',
            loyal_group='Group1',
            birthday='1990-01-01',
            gender='Male',
            marital_status='Single',
            education='Graduate',
            occupation='Engineer',
            yearly_income=50000,
            total_children=2,
            is_active=1,
            recency=10,
            frequency=1.5,
            monetary=1000,
            monetary_m=1000.00,
            rfm=10,
            segment='Segment1',
        )
        DetailCustomer.objects.create(
            customer_since=datetime.strptime('2020-01-02', "%Y-%m-%d"),
            first_name='John',
            last_name='Doe',
            loyal_group='Group1',
            birthday='1990-01-01',
            gender='Male',
            marital_status='Single',
            education='Graduate',
            occupation='Engineer',
            yearly_income=50000,
            total_children=2,
            is_active=1,
            recency=10,
            frequency=1.5,
            monetary=1000,
            monetary_m=1000.00,
            rfm=10,
            segment='Segment1',
        )

    def test_post_detail_customers(self):
        url = reverse('detailcustomer-api')
        data = {'fromDate': '2020-01-01', 'toDate': '2020-01-02'}
        response = self.client.post(url, json.dumps(data), content_type='application/json')

        fromDate = datetime.strptime(data['fromDate'], "%Y-%m-%d")
        toDate = datetime.strptime(data['toDate'], "%Y-%m-%d")
        expected_count = DetailCustomer.objects.filter(customer_since__range=(fromDate, toDate)).count()
        
        print(f'response.content: {response.content}')
        print(f'expected_count: {expected_count}')
        
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'sum_customers': expected_count})  # Replace 0 with the expected count

    def test_post_detail_customers_invalid_data(self):
        url = reverse('detailcustomer-sumCustomers-api')
        data = {}  # Missing startDate and endDate
        response = self.client.post(url, json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {'error': 'startDate and endDate are required'})
