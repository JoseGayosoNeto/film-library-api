from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'
    
    def get_rate(self, obj):        
        
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        
        if rate:
            return f'{rate:.1f}/5.0'
        
        return None
    
    def validate_release_date(self, value):
        if value.year < 1888:
            raise serializers.ValidationError('Release date cannot be less than 1888.')
        return value
    
    def validate_resume(self,value):
        if len(value) > 500:
            raise serializers.ValidationError('Resume must not be longer than 200 characters.')
        return value