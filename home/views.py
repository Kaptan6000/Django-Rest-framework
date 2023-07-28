from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .models import Person
from .serializers import PeopleSerializer,LoginSerializer

@api_view(['GET'])
def index(request):
    data = request.GET.get('name')
    print(data)
    coarses = {
        'course_name':'python',
        'learn' : ['flask', 'Django' ,'FastAPi'],
        'course_provider' : 'Scaler'
    }
    return Response(coarses)

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def person(request):
    if request.method == 'GET':
        obj = Person.objects.all()
        serializer = PeopleSerializer(obj , many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data 
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data 
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj,data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data 
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({"person's data is deleted"})
    

@api_view(['POST'])
def Login(request):    
    data = request.data 
    serializer = LoginSerializer(data=data)
    if serializer.is_valid():
        data = serializer.data
        return Response({'message':'success'})
    return Response(serializer.errors)