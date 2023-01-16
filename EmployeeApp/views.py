# from django.http import HttpResponse
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

# def home(request):
#     return HttpResponse('home page')

# def about(request):
#     return HttpResponse('about page')

# def contact(request):
#     return HttpResponse('contact page')

# Create your views here.

#get api Overview using get api
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Api Overview': '/',
        'All': '/all/',
        'Add': '/add/',
        'Update': '/update/pk/',
        'Delete': '/delete/pk/'
    }
    return Response(api_urls)

#get all data which we have added using POST api
@api_view(['GET'])
def view_depData(request):
    items = Departments.objects.all()
    serializer = DepartmentSerializer(items, many=True)
    if items:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

#add data using Post api 
@api_view(['POST'])
def add_depData(request):
    item = DepartmentSerializer(data=request.data)
    # validating for already existing data
    if Departments.objects.filter(**request.data).exists():
        raise DepartmentSerializer.ValidationError('This data already exists')
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

#update data which we have added using POST api
@api_view(['POST'])
def update_depData(request, pk):
    item = Departments.objects.get(pk=pk)
    data = DepartmentSerializer(instance=item, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

#delete data which we have added using POST api
@api_view(['DELETE'])
def delete_depData(request,pk):
    item = get_object_or_404(Departments, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

#api for Employee
@api_view(['GET','POST'])
def viewOrAddEmployeeDetail(request):
    if request.method == 'GET':
        items = Employees.objects.all()
        serializer = EmployeeSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        emp = request.data
        item = EmployeeSerializer(data=emp)
        item.is_valid()
        item.save()     
        return Response(item.data)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT','DELETE'])
def updateOrDeleteEmployeeDetail(request, pk):
    if request.method == 'PUT':
        item = Employees.objects.get(pk=pk)
        data = EmployeeSerializer(instance=item, data=request.data)
        data.is_valid()
        data.save()
        return Response(data.data)
    
    elif request.method == 'DELETE':
        item = get_object_or_404(Employees, pk=pk)
        item.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    


       
   

        
            
       
  

    
    

   
    

   