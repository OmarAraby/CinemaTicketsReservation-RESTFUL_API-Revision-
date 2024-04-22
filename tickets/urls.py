from django.urls import path , include
from . import views


app_name='tickets'

urlpatterns = [
    

    #1
    path('django/jsonresponse_no_model/', views.no_rest_no_model),
    #2
    path('django/jsonresponse_from_model/', views.no_rest_from_model),

    #3.1 GET & POST from rest framework function based view @api_view
    path('rest/fbvlist/', views.FBV_List),

    #3.2 GET & PUT & DELETE from rest framework function based view @api_view
    path('rest/fpvpk/<int:pk>', views.FBV_pk),

    #4.1 GET & POST from rest framework Class Based View APIView
    path('rest/cbv/', views.CBV_List.as_view()),

    #4.2 GET & PUT & DELETE from rest framework Class Based View APIView
    path('rest/cbv/<int:pk>', views.CBV_pk.as_view()),

    #5.1 GET & POST from rest framework Class Based View Mixins
    path('rest/mixins/', views.mixins_list.as_view()),

    #5.2 GET & PUT & DELETE from rest framework Class Based View Mixins
    path('rest/mixins/<int:pk>', views.mixins_pk.as_view()),

    #6. GET & POST from rest framework Class Based View Generics
    path('rest/generics/', views.generics_list.as_view()),

    #6.2 GET & PUT & DELETE from rest framework Class Based View Generics
    path('rest/generics/<int:pk>', views.generics_pk.as_view()),

]