from django.shortcuts import render
from django.http.response import JsonResponse 
from .models import Guest , Movie , Reservation
from rest_framework.decorators import api_view
from .serializers import MovieSerializer , ReservationSerializer , GuestSerializer
from rest_framework import status , filters 
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics , mixins

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
@api_view(['GET', 'PUT', 'DELETE'])
def FBV_pk(request, pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # GET
    if request.method == 'GET':
        serializer = GuestSerializer(guest)
        return Response(serializer.data)

    # PUT
    elif request.method == 'PUT':
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    elif request.method == 'DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#4 CBV Class Based Views
#4.1 List and Create == GET and POST
class CBV_List(APIView):
    def get(self, request):
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 


#4.2 GET PUT DELETE Class Based View ---- pk
class CBV_pk(APIView):
	def get_object(self , pk):
		try:
			return Guest.objects.get(pk=pk)
		except Guest.DoesNotExist:
			raise Http404

	def get(self , request , pk):
		guest = self.get_object(pk)
		serializer = GuestSerializer(guest)
		return Response(serializer.data)
	def put(self , request , pk):
		guest = self.get_object(pk)
		serializer = GuestSerializer(guest, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def delete(self , request, pk):
		guest= self.get_object(pk)
		guest.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)





#5 Mixins
#5.1 Mixins list //  List and Create == GET and POST


class mixins_list(mixins.ListModelMixin , mixins.CreateModelMixin , generics.GenericAPIView):
	queryset = Guest.objects.all()
	serializer_class = GuestSerializer

	def get(self , request):
		return self.list(request)


	def post(self, request):
		return self.create(request)



#5.2 Mixins GET & PUT & DELETE
class mixins_pk(mixins.RetrieveModelMixin , mixins.UpdateModelMixin , mixins.DestroyModelMixin , generics.GenericAPIView):
	queryset = Guest.objects.all()
	serializer_class = GuestSerializer

	def get(self , request, pk):
		return self.retrieve(request)


	def put(self, request , pk):
		return self.update(request)

	def delete(self, request , pk):
		return self.destroy(request)




#6 Generics
#6.1 Generics GET & POST

class generics_list(generics.ListCreateAPIView):
	queryset = Guest.objects.all()
	serializer_class = GuestSerializer



#6.2 Generics GET & PUT & DELETE
class generics_pk(generics.RetrieveUpdataDestoryAPIView):
	queryset = Guest.objects.all()
	serializer_class = GuestSerializer







