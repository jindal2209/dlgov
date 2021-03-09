from django.shortcuts import render
from .seraializers import ComplaintSerializer
from .models import Complaint
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser
from django.http import HttpResponse,Http404,JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from datetime import date,datetime
import requests

from rest_framework.decorators import api_view
# Create your views here.

# class ComplaintView(generics.CreateAPIView):
# 	serializer_class = ComplaintSerializer
# 	queryset = Complaint.objects.all()
# 	parser_classes = (MultiPartParser, FormParser,JSONParser)


def send_message(phone_number,msg):
	url = "https://www.fast2sms.com/dev/bulkV2"
	querystring = {

		"authorization":"4AnjbmwRhPDUsMXodxclz5Y1fiOHvEKpuk7VZS8eTQIJFLtG2NNWbh2yAa5nklY97j4rCJfoecVIXKdT",
		"sender_id":"CHKSMS",
		"message_text":msg,
		# "variables_values":"12345|asdaswdx",
		"route":"v3",
		"numbers":phone_number
	}
	headers = {
    	'cache-control': "no-cache"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	print(response.text)

@api_view(['POST'])
def complaintView(request):
	if request.method == "POST" :
		rdata = request.data
		tdate = date.today()
		tdate = tdate.strftime("%d%m%y")
		
		ctime = datetime.now()
		ctime = ctime.strftime("%H%M%S")

		rdata["complaint_number"] = "DL-{}-{}-{}".format(rdata["phone_number"][-3:],tdate,ctime)

		# print(rdata)

		serialized = ComplaintSerializer(data=rdata)
		if serialized.is_valid():
			serialized.save()
			responseData = {
				"complaint_number" : rdata['complaint_number'] 
			}
			cnum = rdata['complaint_number']
			fname = rdata['first_name'] + rdata['last_name']
			msg = "Hi " + fname + ". Your complaint has been registered. Your complaint number is " + cnum + " save this complaint number for future references"
			send_message(request.data['phone_number'],msg)
			# print(request.data['phone_number']) make an api call to phone number
			return Response(responseData,status=status.HTTP_201_CREATED)