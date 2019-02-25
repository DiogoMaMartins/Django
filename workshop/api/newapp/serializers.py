from rest_framework import  serializers,fields
from . import models

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Book
		fields= '__all__'
