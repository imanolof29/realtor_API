import django_filters
from rest_framework import generics, permissions
from api import serializer
from api.serializer import RealtorsListSerializer, RealtorDetailsSerializer
from api.models import RealtorsList, RealtorDetails


class RealtorsListView(generics.ListAPIView):
    queryset = RealtorsList.objects.all()
    serializer_class = RealtorsListSerializer
    permission_classes = [permissions.IsAuthenticated]


class RealtorDetailsView(generics.ListAPIView):
    queryset = RealtorDetails.objects.all()
    serializer_class = RealtorDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

    #get queryset from url
    """def get_queryset(self):
        zipcode = self.request.query_params.get('zipcode') # format: zipcodes coma separated: http://127.0.0.1:8000/api/realtor_2/?zipcode=28011,28240
        date_insert_from = self.request.query_params.get('date_insert_from')
        date_insert_to = self.request.query_params.get('date_insert_to')
        if zipcode is not None:
            zipcode = zipcode.split(",") # convert to a list
            return self.queryset.filter(zipcode__in= zipcode)
        if date_insert_to is not None and date_insert_from is not None:
            return self.queryset.filter(date_insert__gte=date_insert_from, date_insert__lte=date_insert_to)
        else:
            if date_insert_from is not None and date_insert_to is None:
                return self.queryset.filter(date_insert__gte=date_insert_from)
            elif date_insert_from is None and date_insert_to is not None:
                return self.queryset.filter(date_insert__lte=date_insert_from)
        return self.queryset"""
        
        


#2021-11-07T17:45:53.747390

#2021-11-09T09:19:12.170616Z

#SELECT COUNT(*) from realtors_detail where date_insert>'2021-11-07T17:45:53.747390' AND date_insert<'2021-11-09T09:19:12.170616Z'

#SELECT COUNT(*) from realtors_detail where date_insert>'2021-11-07T17:45:53.747390'

#?zipcode=30380&date_insert_from=2021-11-07T17:45:53.747390&date_insert_to=2021-11-09T09:19:12.170616Z