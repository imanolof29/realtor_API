from django.db import models

class RealtorsList(models.Model):
    class Meta:
        managed = False
        db_table = "realtors_list"

    commercialdataid = models.AutoField(db_column='commercialDataId', primary_key=True)  # Field name made lowercase.
    id_name = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    since_year = models.IntegerField(blank=True, null=True)
    date_insert = models.DateTimeField(auto_now_add=True)
    date_insert_epoc = models.IntegerField(blank=True, null=True)
    date_update = models.DateTimeField(auto_now=True)
    date_update_epoc = models.IntegerField(blank=True, null=True)
    url_href = models.CharField(max_length=200, blank=True, null=True)
    url_source = models.CharField(max_length=200, blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    success = models.IntegerField()
    active = models.IntegerField(blank=True, null=True)
    karma = models.IntegerField(blank=True, null=True)
    member = models.JSONField(blank=True, null=True)
    reason= models.CharField(max_length=30, blank=True, null=True)



class RealtorDetails(models.Model):
    class Meta:
        managed = False
        db_table = "realtors_detail"

    commercialdataid = models.OneToOneField(
        RealtorsList,
        on_delete=models.CASCADE,
        primary_key=True,)


    # commercialdataid = models.AutoField(db_column='commercialDataId', primary_key=True)  # Field name made lowercase.
    id_name = models.CharField(max_length=200, blank=True, null=True)
    micrositename = models.CharField(db_column='micrositeName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=1000, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    zipcode = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    web = models.CharField(max_length=1000, blank=True, null=True)
    since_year = models.IntegerField(blank=True, null=True)
    n_total_properties = models.IntegerField(blank=True, null=True)
    n_sale_homes = models.IntegerField(blank=True, null=True)
    n_rent_homes = models.IntegerField(blank=True, null=True)
    date_insert = models.DateTimeField(auto_now_add=True)
    date_insert_epoc = models.IntegerField(blank=True, null=True)
    date_update = models.DateTimeField(auto_now=True)
    date_update_epoc = models.IntegerField(blank=True, null=True)
    datetime_stamp = models.DateTimeField(blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    url_es_rent = models.CharField(max_length=200, blank=True, null=True)
    usedlocationid = models.CharField(db_column='usedLocationId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    level = models.CharField(max_length=200, blank=True, null=True)
    subitems_data_location_id = models.CharField(max_length=1000, blank=True, null=True)
    subitems_title = models.CharField(max_length=1000, blank=True, null=True)
    last_batch_name = models.CharField(max_length=1000, blank=True, null=True)
    url_source = models.CharField(max_length=200, blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    success = models.IntegerField()
    active = models.IntegerField(blank=True, null=True)
    zipcode_bis = models.CharField(max_length=200, blank=True, null=True)
    logo_url = models.CharField(max_length=150, blank=True, null=True)
    karma = models.IntegerField(blank=True, null=True)
    trademark = models.JSONField(blank=True, null=True)
    properties_recent_top_rent_homes = models.JSONField(blank=True, null=True)
    reason= models.CharField(max_length=30, blank=True, null=True)