from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Product, Order, OrderItem, ShippingAddress
from .serializers import ProductSerializer

User = get_user_model()



class ProductViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass', is_superuser=True, is_staff=True)
        self.product = Product.objects.create(
            user=self.user,
            name='Test Product',
            price=10,
            brand='Test Brand',
            countInStock=10,
            category='Test Category',
            description='Test Description'
        )

    def test_get_product(self):
        response = self.client.get(reverse('products:product', kwargs={'pk': self.product._id}))
        product = Product.objects.get(_id=self.product._id)
        serializer = ProductSerializer(product, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_delete_product(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(reverse('products:product-delete', kwargs={'pk': self.product._id}))
        self.assertEqual(response.status_code, 200)
        # Check if the product still exists in the database
        product_exists = Product.objects.filter(_id=self.product._id).exists()
        self.assertFalse(product_exists)

    def test_update_product(self):
        self.client.force_authenticate(user=self.user)
        new_product_details = {
            'name': 'Updated Product',
            'price': 30,
            'brand': 'Updated Brand',
            'countInStock': 30,
            'category': 'Updated Category',
            'description': 'Updated Description'
        }
        response = self.client.put(reverse('products:product-update', kwargs={'pk': self.product._id}), new_product_details, format='json')
        self.assertEqual(response.status_code, 200)
        # Check if the product details have been updated correctly
        updated_product = Product.objects.get(_id=self.product._id)
        for field, value in new_product_details.items():
            self.assertEqual(getattr(updated_product, field), value)




class UserViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='adam@example.com', password='pass', first_name='Adam', is_superuser=True, is_staff=True)
        self.admin = User.objects.create_user(username='admin@example.com', password='pass', first_name='Admin', is_staff=True, is_superuser=True)
        self.product = Product.objects.create(
            user=self.user,
            name='Test Product',
            price=10,
            brand='Test Brand',
            countInStock=10,
            category='Test Category',
            description='Test Description'
        )
        self.order = Order.objects.create(
            user=self.user,
            paymentMethod='Test Payment Method',
            taxPrice=1.0,
            shippingPrice=1.0,
            totalPrice=12.0,
        )
        self.orderItem = OrderItem.objects.create(
            product=self.product,
            order=self.order,
            name=self.product.name,
            qty=1,
            price=self.product.price,
            image=self.product.image.url,
        )
        self.shippingAddress = ShippingAddress.objects.create(
            order=self.order,
            address='Test Address',
            city='Test City',
            postalCode='Test Postal Code',
            country='Test Country',
        )

    def test_can_add_order_items(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('orders-add'), {
            'orderItems': [{
                'product': str(self.product._id),
                'qty': 1,
                'price': self.product.price,
            }],
            'paymentMethod': 'Test Payment Method',
            'taxPrice': 1.0,
            'shippingPrice': 1.0,
            'totalPrice': 12.0,
            'shippingAddress': {
                'address': 'Test Address',
                'city': 'Test City',
                'postalCode': 'Test Postal Code',
                'country': 'Test Country',
            },
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_user(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.delete(reverse('user-delete', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_get_user_by_id(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(reverse('user', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)





class OrderViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='adam', email='adam@example.com', password='pass', is_superuser=True, is_staff=True)
        self.admin = User.objects.create_user(username='admin@example.com', password='pass', first_name='Admin', is_staff=True)

    def test_can_register_user(self):
        response = self.client.post(reverse('register'), {
            'name': 'Test User',
            'email': 'test@example.com',
            'password': 'testpass',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'test@example.com')

    def test_can_update_user_profile(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put(reverse('users-profile-update'), {
            'name': 'Updated User',
            'email': 'updated@example.com',
            'password': 'newpass',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'updated@example.com')

    def test_can_get_user_profile(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('users-profile'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'adam@example.com')

    def test_can_get_users(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_can_get_user_by_id(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(reverse('user', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'adam@example.com')

    def test_can_update_user(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.put(reverse('user-update', args=[self.user.id]), {
            'name': 'Updated User',
            'email': 'updated@example.com',
            'isAdmin': False,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'updated@example.com')

    def test_can_delete_user(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.delete(reverse('user-delete', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


