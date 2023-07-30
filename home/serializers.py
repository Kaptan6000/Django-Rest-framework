from rest_framework import serializers
from .models import Person,Color
from django.contrib.auth.models import User 

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    def validate(self,data):
        if data['username']:
            if User.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError('username is taken')
        if data['email']:
            if User.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError('email is taken')    
        return data
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        return validated_data

class LoginSerializer(serializers.Serializer):
    email= serializers.EmailField()
    password = serializers.CharField()

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Color
        fields = ['color_name']

class PeopleSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    color_info = serializers.SerializerMethodField()
    class Meta:
        model = Person 
        # depth = 1
        #exclude=
        fields = '__all__'
    def get_color_info(self,obj):
        color_obj = Color.objects.get(id=obj.color.id)
        return {'colr_name':color_obj.color_name,'hex_code':'#000'}
    # def validate_age(self,data):

    def validate(self, data):
        spl = "!@#$%^&*?()<>,~`"
        if any(i in data['name'] for i in spl):
            raise serializers.ValidationError('name csnnot not contain special chracters')
        if data['age']<18:
            raise serializers.ValidationError('age should be greater than 18')
        return data