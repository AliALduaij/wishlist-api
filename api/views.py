from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from .serializers import ListSerializer, DetailSerializer
from items.models import Item
from .permissions import staff_owner

# Create your views here.
class ItemListView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ListSerializer
	filter_backends = [SearchFilter,OrderingFilter]
	search_fields = ['name']
	permission_classes = [AllowAny,]

class ItemDetailView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = DetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	permission_classes = [staff_owner]