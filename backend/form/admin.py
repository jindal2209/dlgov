from django.contrib import admin
from .models import Complaint

# Register your models here.
@admin.register(Complaint)
class ComplaintView(admin.ModelAdmin):
	list_display = ('complaint_number',"phone_number","status",'district','ward')
	list_filter = ("status",'district','ward','department')
	search_fields = ('complaint_number','phone_number')