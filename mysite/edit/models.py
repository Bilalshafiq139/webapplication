from django.db import models

class edit(models.Model):
    Form_no = models.CharField(max_length=255)
    Status = models.CharField(max_length=255)
    Applicant_name = models.CharField(max_length=255)
    Father_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    CNIC = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    Hafiz_e_Quran = models.BooleanField()
    District = models.CharField(max_length=255)
    Religion = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    Program = models.CharField(max_length=255)
    DOB=models.DateField()
    Gender= models.CharField(max_length=255)
    Martial_Status= models.CharField(max_length=255)


