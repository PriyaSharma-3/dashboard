from ast import Or
from django.http import HttpResponse, JsonResponse,response
from django.shortcuts import render, redirect
from .forms import ConsumerForm
from .models import Consumer
import csv 
from django.core import serializers
import os 
import json
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

def index(request):
    return render(request,"index.html")

def consumer(request):  
    return render(request,"consumer.html")

def show(request):
    # NewAccountNumber = request.POST['NewAccountNumber']
    # Username = request.POST['Username']
    # FeederName = request.POST['FeederName']
    # consumers = Consumer.objects.all().filter(NewAccountNumber=NewAccountNumber,Username=Username)
    # return render(request, 'consumer.html',{'Consumers' : consumers})

    NewAccountNumber=request.GET.get('NewAccountNumber')
    Username=request.GET.get('Username')
    FeederName = request.GET.get('FeederName')
    Date_Time = request.GET.get('Date_Time')
  
    # Date_Time =" " + "'" + Date_Time + "%'" +" "
    
    # Date_Time =" " +"'%2022-02-21%'" + "  "
    
    condition = ""
    if (NewAccountNumber!=""):
        condition = condition + "and \"NewAccountNumber\" = " + "'" + NewAccountNumber + "'" +"  "
            
    
    if (Username!=""):
        condition = condition + "and \"Username\"= " + "'" + Username + "'" +"  "

    if (FeederName!=""):
        condition = condition + "and \"FeederName\"= " + "'" + FeederName + "'" +"  "
        
        
    if (Date_Time!=""):
     
        # condition = condition + "and CAST(\"Date_Time\" AS TEXT)= " + "'" + Date_Time + "'" +"  "
        condition = condition + "and  substring(CAST(\"Date_Time\" AS TEXT) for 10) = " + "'" + Date_Time + "'" +"  "
    
       
        print(condition)
    
  
    # else:
    # consumer = Consumer.objects.filter(Date_Time__contains=Date_Time).filter(FeederName=FeederName).filter(Username=Username).filter(NewAccountNumber=NewAccountNumber)
    # consumer = Consumer.objects.raw("Select * from \"Consumer\" where \"Username\"= " + "'" + Username + "'" +" ") 
    consumer = Consumer.objects.raw("Select * from \"Consumer\" where true "+condition+" ") 
    paginator = Paginator(consumer,10)

    page = request.GET.get('page')
    try:
        consumer = paginator.page(page)
    except PageNotAnInteger:
        consumer = paginator.page(1)
    except EmptyPage:
        consumer = paginator.page(paginator.num_pages)

 
    con = {
                'Consumers' : consumer,
                'NewAccountNumber':NewAccountNumber,
                'FeederName':FeederName,
                'Username':Username,
                'Date_Time':Date_Time,
    }
        
    return render(request, 'consumer.html',con)



# def show_NewAccountNumber(request):
#     # print(request.POST)
#     NewAccountNumber = request.POST['NewAccountNumber']
#     consumer = Consumer.objects.filter(NewAccountNumber=NewAccountNumber)
#     return render(request, 'consumer.html',{'Consumers' : consumer})

# def show_Username(request):
#     # print(request.POST)
#     Username = request.POST['Username']
#     consumer = Consumer.objects.filter(Username=Username)
#     return render(request, 'consumer.html',{'Consumers' : consumer})

# def show_FeederName(request):
#     # print(request.POST)
#     FeederName = request.POST['FeederName']
#     consumer = Consumer.objects.filter(FeederName=FeederName)
#     return render(request, 'consumer.html',{'Consumers' : consumer})
    
def consumer_excel(request):
    if request.method == 'POST':
            form = ConsumerForm(request.POST) 

            Username = request.POST.get['Username']
            Date_Time = request.POST.get['Date_Time']

            try:
                consumer = Consumer.objects.get(Username_Consumer=Username,Date_Time_Consumer=Date_Time)   
            except Consumer.DoesNotExist:
                consumer = None
                         
            if consumer is not None:
                return redirect('/excel_download')                                           
            else:
                return render(request, 'consumer_excel.html')

    return render(request,"consumer_excel.html")     

def excel_download(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="consumer.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['Id','SurveyId','Latitude','Longitude','Username','Date_Time','SubDivision','Section','BuildingReferenceNumber','ConnectedPoleNo','PaintedPoleNo',
            'FeederName','DTCode','ConsumerName','NewAccountNumber','OldAccountNumber','SCNumber','CustomerMobileNumber','FlatNo','Address1','Address2','Address3',
            'ConsumerDoorLock','AMRInstalled','CommunicationType','CTRatio','DisplayCondition','MaximumDemand','MeterAvailability','MeterBox','MeterLocation',
            'HeightGT5ft','MeterStatus','NominalVoltage','PhaseConnection','SealCondition','SealType','TotalMF','kWh','Bypass','Category','Type','SubType',
            'MeterSerialNumber','MeterMake','Theft','BillDelivered','BillShown','MeterPhoto','BillPhoto','OtherPhoto','NeighbouringMeterNo','NeighbouringConsumerNo',
            'NoofDigits','SurveyorRemark'])

    Username=request.POST.get('Username_Consumer')
    Date_Time=request.POST.get('Date_Time_Consumer')

    if Username == 'all':

        for consumer in Consumer.objects.all().filter(Date_Time__contains=Date_Time).values_list('Id','SurveyId','Latitude','Longitude','Username','Date_Time','SubDivision','Section','BuildingReferenceNumber','ConnectedPoleNo','PaintedPoleNo',
            'FeederName','DTCode','ConsumerName','NewAccountNumber','OldAccountNumber','SCNumber','CustomerMobileNumber','FlatNo','Address1','Address2','Address3',
            'ConsumerDoorLock','AMRInstalled','CommunicationType','CTRatio','DisplayCondition','MaximumDemand','MeterAvailability','MeterBox','MeterLocation',
            'HeightGT5ft','MeterStatus','NominalVoltage','PhaseConnection','SealCondition','SealType','TotalMF','kWh','Bypass','Category','Type','SubType',
            'MeterSerialNumber','MeterMake','Theft','BillDelivered','BillShown','MeterPhoto','BillPhoto','OtherPhoto','NeighbouringMeterNo','NeighbouringConsumerNo',
            'NoofDigits','SurveyorRemark'):
            writer.writerow(consumer)
 
    else:

        for consumer in Consumer.objects.all().filter(Username=Username,Date_Time__contains=Date_Time).values_list('Id','SurveyId','Latitude','Longitude','Username','Date_Time','SubDivision','Section','BuildingReferenceNumber','ConnectedPoleNo','PaintedPoleNo',
            'FeederName','DTCode','ConsumerName','NewAccountNumber','OldAccountNumber','SCNumber','CustomerMobileNumber','FlatNo','Address1','Address2','Address3',
            'ConsumerDoorLock','AMRInstalled','CommunicationType','CTRatio','DisplayCondition','MaximumDemand','MeterAvailability','MeterBox','MeterLocation',
            'HeightGT5ft','MeterStatus','NominalVoltage','PhaseConnection','SealCondition','SealType','TotalMF','kWh','Bypass','Category','Type','SubType',
            'MeterSerialNumber','MeterMake','Theft','BillDelivered','BillShown','MeterPhoto','BillPhoto','OtherPhoto','NeighbouringMeterNo','NeighbouringConsumerNo',
            'NoofDigits','SurveyorRemark'):
            writer.writerow(consumer)

    return response

def consumer_edit(request, Id):  
    employee = Consumer.objects.get(Id=Id)  
    return render(request,'consumer_edit.html', {'Consumer':employee})  


def update(request, Id):  
    
    employee = Consumer.objects.get(Id=Id)  
    form = ConsumerForm(request.POST, instance = employee)
    
    if form.is_valid():  
        # print(form.cleaned_data['NewAccountNumber'])
        form.save()
        messages.success(request, 'Data Updated successfully')  
        return redirect("/consumer")
    else:
        messages.warning(request, "Data was not inserted")
    # print(form.errors)  
    return render(request, 'consumer_edit.html', {'Consumer': employee})  



def consumer_delete(request, Id):  
    consumer = Consumer.objects.get(Id=Id)   
    consumer.delete()  
    messages.success(request, 'Data Deleted successfully')
    return redirect("/consumer")  


def consumer_view(request, Id):
    if request.method == "GET": 
            consumer = Consumer.objects.get(Id=Id)   
              
            return render(request, 'consumer_view.html',{'Consumer' : consumer})            
    else:
        return render(request, 'consumer.html')


def consumer_map(request, Id):
    if request.method == "GET": 
        consumer = Consumer.objects.get(Id=Id)   
              
        return render(request, 'consumer_map.html',{'Consumer' : consumer})            
    else:
        return render(request, 'consumer.html')


def logout(request):
    return render(request,"login.html")


def autocompleteModel(request):
    if request.is_ajax():
        q = request.GET.get('term')

        my_dict = {
            'NewAccountNumber':"%"+q+"%",         
        } 
        consumer = Consumer.objects.raw('Select * from \"Consumer\" ', my_dict)
        print(consumer)

        results = []
        for pl in consumer:
            NewAccountNumber1 = {}
            NewAccountNumber1 = pl.NewAccountNumber 
            results.append(NewAccountNumber1)
        data = json.dumps(results)
    
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

