from django.db import models


BANK_CHOICES = [
    
    ('EQuityBank', 'Equity Bank'),
    ('CogeBanque', 'CogeBanque'),
    ('BK', 'Bank of Kigali'),
    ('GT', 'GT Bank'),
    ('KCB', 'KCB'),
]


class Gas(models.Model):

    CYLINDER_CHOISES = [
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
    cylinder_type = models.CharField(choices=CYLINDER_CHOISES, default='6kg')


class Retailer(models.Model):
    owner_name =  models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    tin_number = models.IntegerField()
    location = models.CharField()                               # TO-DO: must become PointField using GIS.
    bank = models.CharField(choices=BANK_CHOICES)
    bank_account = models.IntegerField(blank=True)
    gas_importer = models.CharField(max_length=100)

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
    bank = models.CharField(choices=BANK_CHOICES, blank=True)
    bank_account = models.IntegerField(blank=True)


