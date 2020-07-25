
from django.contrib import admin
from . models import Hospital, Center, Beneficiary, Children, Donor, Transaction
# Register your models here.
admin.site.register(Hospital)
admin.site.register(Center)
admin.site.register(Beneficiary)
admin.site.register(Children)
admin.site.register(Donor)
admin.site.register(Transaction)