from rest_framework import serializers
from .models import Person

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person 
        depth = 1
        #exclude=
        fields = '__all__'

    # def validate_age(self,data):

    def validate(self, data):
        spl = "!@#$%^&*?()<>,~`"
        if any(i in data['name'] for i in spl):
            raise serializers.ValidationError('name csnnot not contain special chracters')
        if data['age']<18:
            raise serializers.ValidationError('age should be greater than 18')
        return data