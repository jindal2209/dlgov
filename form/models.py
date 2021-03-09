from django.db import models

# Create your models here.
from django.db import models

class Complaint(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	phone_number = models.IntegerField()
	district = models.CharField(max_length=50)
	ward = models.CharField(max_length=100)
	department = models.CharField(max_length=200)
	file_uploaded = models.FileField(upload_to="Files",blank=True,null=True)
	complaint_text = models.TextField(max_length=1000,blank=True)
	status = models.BooleanField(default=False,blank=True)
	complaint_number = models.CharField(blank=True,max_length=100)

	def __str__(self):
		return ("{} {} {}").format(self.first_name , self.last_name , self.phone_number)