from rest_framework import serializers
from items.models import Item , User, FavoriteItem


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model= User
		fields= ['first_name','last_name']

class ListSerializer(serializers.ModelSerializer):
	added_by = UserSerializer()
	favorited= serializers.SerializerMethodField()
	detail = serializers.HyperlinkedIdentityField(
    view_name = "api-detail",
    lookup_field = "id",
    lookup_url_kwarg = "item_id"
    )
	class Meta:
		model= Item
		fields= ['image','name','description','favorited','added_by','detail']

	def get_favorited(self,obj):
		return obj.favs.count()


class FavoriteItemSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = FavoriteItem
		fields=['id','user',]



class DetailSerializer(serializers.ModelSerializer):
	favs= FavoriteItemSerializer(many=True)
	class Meta:
		model= Item
		fields='__all__'





