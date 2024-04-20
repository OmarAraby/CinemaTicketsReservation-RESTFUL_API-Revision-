from django.shortcuts import render
from django.http.response import JsonResponse 
from .models import Guest , Movie , Reservation
from rest_framework.decorators import api_view
from .serializers import MovieSerializer , ReservationSerializer , GuestSerializer
from rest_framework import status , filters 
from rest_framework.response import Response
# Create your views here.



#1 without REST and No model Query FBV  ' Static'
def no_rest_no_model(request):
	guests= [

		{
			'id': 1 ,
			'Name': 'Omar',
			'mobile':5555555,
		},
		{

			'id':2,
			'Name': 'Araby',
			'mobile': 4444444,
		}

	]

	return JsonResponse(guests, safe=False)



#2 model data default django without rest -----> import my data from my database
def no_rest_from_model(request):
	data = Guest.objects.all()
	response = {
		'guests': list(data.values('name','mobile')),
	}

	return JsonResponse(response)


# List == GET
# Create == POST
# pk query == GET
# Update == PUT
# destroy == DELETE



#3 Function based views
#3.1 GET POST
@api_view(['GET','POST'])
def FBV_List(request):

	# GET
	if request.method == 'GET':
		guests = Guest.objects.all()
		serializer = GuestSerializer(guests, many=True)
		return Response(serializer.data)

	# POST
	elif request.method == 'POST':
		serializer = GuestSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response (serializer.data, status= status.HTTP_201_CREATED)
		return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)





#3.2 GET PUT DELETE
@api_view(['GET','PUT','DELETE'])
def FBV_pk(request, pk ):
 
	guests = Guest.objects.get(pk=pk)
	# GET
	if request.method == 'GET':
		serializer = GuestSerializer(guests, many=True)
		return Response(serializer.data)

	# PUT
	elif request.method == 'PUT':
		serializer = GuestSerializer(guests, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response (serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

	# DELETE
	if request.method == 'DELETE':
		guests.delete()
		return Response(status= status.HTTP_204_NO_CONTENT)
