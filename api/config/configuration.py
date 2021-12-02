from django.db import models

# Configuration to be used in the application

class Configuration(models.Model):
    MAX_RECORD_COUNT = 100  # 10000
    APIKEYS = ["ce9d77b308c149d5992a80073637e4d5",
               "ce9d77b308c149d5992a80073637e4d6"]
    REQUIRED_PARAMETERS = ["zipcode",
                           ]


