from rest_framework.serializers import ModelSerializer
from .models import Product,CustomerWiseProduct


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['p_id','pname']

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = CustomerWiseProduct
        fields = ['pc_id','c_name','pname','pprice']
