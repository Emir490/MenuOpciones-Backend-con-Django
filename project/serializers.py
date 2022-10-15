from mimetypes import init
from rest_framework import serializers

class Name:
    def __init__(self, name):
        self.name = name

class Square:
    def __init__(self, area, perimeter):
        self.area = area
        self.perimeter = perimeter
        
class Word:
    def __init__(self, length):
        self.length = length 
        
class NameSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Name(**validated_data)

class FigureSerializer(serializers.Serializer):
    area = serializers.DecimalField(max_digits=10, decimal_places=2)
    perimeter = serializers.DecimalField(max_digits=10, decimal_places=2)
    
    def create(self, validated_data):
        return Square(**validated_data)
    
class WordSerializer(serializers.Serializer):
    length = serializers.IntegerField()
    
    def create(self, validated_data):
        return Word(**validated_data)