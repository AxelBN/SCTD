from django.db import models
from django.contrib import admin
# Create your models here.
# Crea tus modelos aqui.
DOCUMENT_CHOICES = (
    ("CreditNote","CN"),
    ("ElectronicBill","EB")
)

class TrackDocument(models.Model):
    document = models.CharField(max_length=50)
    date = models.DateField()
    user = models.CharField(max_length=50)
    site = models.ForeignKey('Site', on_delete=models.CASCADE)
    type = models.CharField(
        max_length=20,
        choices = DOCUMENT_CHOICES,
    )
    def __str__(self):
        return self.user
class trackingAdmin(admin.ModelAdmin):
    fields = ['document','date','user','site','type']



admin.site.register(TrackDocument, trackingAdmin)
