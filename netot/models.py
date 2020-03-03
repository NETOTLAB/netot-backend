from django.db import models


class RetailerOwner(models.Model):
    # fname, lname, telephone, email, sector, district, province,
    pass


class Gas(models.Model):

    CHOISES = [
        ('6kg' , '6kg'),
        ('12kg', '12kg'),
        ('15kg', '15kg'),
        ('18kg', '18kg'),
        ('20kg', '20kg'),
    ]

    device_id = models.CharField(max_length=20, unique=True)
    location = models.CharField()                               # TO-DO: must become PointField using GIS.
    gas_flow = models.FloatField()                              # in Millilitters
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    cylinder_type = models.CharField(choices=CHOICES, default='6kg')


class Retailer(models.Model):
    name = models.CharField(max_length=20)
    tin_number = models.IntegerField()
    location = models.CharField()                               # TO-DO: must become PointField using GIS.

class Household(models.Model):
    # fname, lname, email, telephone, sector, district, Province, Bank account, account_number
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=10) #TO-DO: add a Validator later
    #province = models.CharField(choice=)
    #district = models.CharField(choice=)
    #sector = models.CharField(choice=)
    gaz = models.ForeignKey('Gas', on_delete=models.CASCADE)


