from django.urls import path

from .views import RealtorDetailsView, RealtorsListView


app_name = "realtor"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    #path('realtor/', Realtors_APIView.as_view()),
    path('realtor_seag/', RealtorDetailsView.as_view()),
]