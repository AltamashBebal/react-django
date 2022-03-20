from django.shortcuts import render
from .models import Product,CustomerWiseProduct
# Create your views here.
from .serializers import ProductSerializer,CustomerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getProducts(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def addProduct(request):
    data = request.data
    product = Product.objects.create(
        pname=data['pname']
    )
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def deleteProduct(request, pk):
    product = Product.objects.get(p_id=pk)
    product.delete()
    return Response('Product was deleted!')




@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def addProductForCustomer(request):
    data = request.data
    print(data)
    product = CustomerWiseProduct.objects.create(
        c_name=data['c_name'],
        p_id=data['p_id'],
        p_price=data['p_price']
    )
    print(product)
    serializer = CustomerSerializer(product, many=False)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getCustomerWise(request, cname):
    product = CustomerWiseProduct.objects.filter(c_name=cname)
    serializer = CustomerSerializer(product, many=True)
    return Response(serializer.data)
   


@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def deleteCustomerWise(request, pc_id):
    product = CustomerWiseProduct.objects.filter(pc_id=pc_id)
    product.delete()
    return Response('Product was deleted!')

@api_view(['PUT'])
@permission_classes((permissions.AllowAny,))
def updateProduct(request, pk):
    data = request.data
    product = Product.objects.get(p_id=pk)
    serializer = ProductSerializer(instance=product, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)