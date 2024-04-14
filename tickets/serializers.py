from rest_framework import serializers
from tickets.models import Movie , Guest , Reservation



class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = MovieSerializer
		fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reservation
		fields = '__all__'



class GuestSerializer(serializers.ModelSerializer):
	class Meta:
		model = Guest
		fields = ['pk','reservation', 'name','mobile']   ##### uuid or slag instead of pk 