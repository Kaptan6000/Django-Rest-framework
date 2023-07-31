from rest_framework.decorators import api_view 
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Person
from rest_framework.views import APIView
from .serializers import PeopleSerializer,LoginSerializer,RegisterSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class LoginAPI(APIView):
    def post(self,request):
        data=request.data 
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({'status':False,
                             'message':serializer.errors})
        user = authenticate(username=serializer.data['username'],password=serializer.data['password'])
        token, _ = Token.objects.get_or_create(user=user)
        print(token)
        return Response({'status':True,'message':'user login','token':str(token)})

class RegisterAPI(APIView):
    def post(self,request):
        data = request.data 
        serializer = RegisterSerializer(data=data)
        if not serializer.is_valid():
            return Response({'status':False,
                             'message':serializer.errors})
        serializer.save()
        return Response({'status':True,'message':'user created'})

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

class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class = PeopleSerializer
    queryset = Person.objects.all()
    def list(self,request):
        search = request.GET.get('search')
        queryset = self.queryset
        if search:
            queryset = queryset.filter(name__startswith = search)
        serializer = PeopleSerializer(queryset , many = True)  
        return Response({'status':200,'data':serializer.data})  