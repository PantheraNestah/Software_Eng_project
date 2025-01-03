from django.shortcuts import render
from rest_framework import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .models import AppUser
from .models import Item
from .models import Staff
from .models import Product


# Create your views here.
def home(request):
    return Response({'message': 'Welcome to the home page'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def user_registration(request):
    if request.method == "POST":
        data = request.data

        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        phone_number = data.get('phone_number')

        if not all([username, password, email, phone_number]):
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
        if AppUser.objects.filter(username=username).exists():
            return Response({'error': 'Username already taken'}, status=status.HTTP_400_BAD_REQUEST)
        if AppUser.objects.filter(email=email).exists():
            return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)

        hashed_password = make_password(password)
        user = AppUser.objects.create(
            username=username, 
            password=hashed_password, 
            email=email, 
            phone_number=phone_number
        )
    return Response({'message': 'User registered successfully', 'user_id': user.id}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def user_login(request):
    if request.method == "POST":
        data = request.data

        username = data.get('username')
        password = data.get('password')

        if not all([username, password]):
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
        if not AppUser.objects.filter(username=username).exists():
            return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)

        user = AppUser.objects.get(username=username)
        if not user.check_password(password):
            return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'User logged in successfully', 'user_id': user.id}, status=status.HTTP_200_OK)

@api_view(['POST'])
def staff_registration(request):
    if request.method == "POST":
        data = request.data

        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        phone_number = data.get('phone_number')
        department = data.get('department')

        if not all([username, password, email, phone_number, department]):
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
        if Staff.objects.filter(username=username).exists():
            return Response({'error': 'Username already taken'}, status=status.HTTP_400_BAD_REQUEST)
        if Staff.objects.filter(email=email).exists():
            return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)

        hashed_password = make_password(password)
        staff = Staff.objects.create(
            username=username, 
            password=hashed_password, 
            email=email, 
            phone_number=phone_number, 
            department=department
        )
    return Response({'message': 'Staff registered successfully', 'staff_id': staff.id}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def staff_login(request):
    if request.method == "POST":
        data = request.data

        username = data.get('username')
        password = data.get('password')

        if not all([username, password]):
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
        if not Staff.objects.filter(username=username).exists():
            return Response({'error': 'Staff not found'}, status=status.HTTP_400_BAD_REQUEST)

        staff = Staff.objects.get(username=username)
        if not staff.check_password(password):
            return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'Staff logged in successfully', 'staff_id': staff.id}, status=status.HTTP_200_OK)


@api_view(['POST'])
def item_registration(request):
    if request.method == "POST":
        data = request.data

        name = data.get('name')
        description = data.get('description')
        category = data.get('category')
        condition = data.get('condition')
        value = data.get('value')
        pickup_location = data.get('pickup_location')

        if not all([name, description, category, condition, value, pickup_location]):
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        item = Item.objects.create(
            name=name, 
            description=description, 
            category=category, 
            condition=condition, 
            value=value, 
            pickup_location=pickup_location
        )
    return Response({'message': 'Item registered successfully', 'item_id': item.id}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def items_list(request):
    if request.method == "GET":
        items = Item.objects.all()
        items_list = []
        for item in items:
            items_list.append({
                'id': item.id,
                'name': item.name,
                'description': item.description,
                'category': item.category,
                'condition': item.condition,
                'value': item.value,
                'pickup_location': item.pickup_location,
                'approval_status': item.approval_status,
                'pickup_status': item.pickup_status
            })
    return Response({'items': items_list}, status=status.HTTP_200_OK)

@api_view(['GET'])
def item_details(request, item_id):
    if request.method == "GET":
        if not Item.objects.filter(id=item_id).exists():
            return Response({'error': 'Item not found'}, status=status.HTTP_400_BAD_REQUEST)

        item = Item.objects.get(id=item_id)
        item_details = {
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'category': item.category,
            'condition': item.condition,
            'value': item.value,
            'pickup_location': item.pickup_location,
            'approval_status': item.approval_status,
            'pickup_status': item.pickup_status
        }
    return Response({'item': item_details}, status=status.HTTP_200_OK)

@api_view(['GET'])
def products_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        products_list = []
        for product in products:
            products_list.append({
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'category': product.category
            })
    return Response({'products': products_list}, status=status.HTTP_200_OK)