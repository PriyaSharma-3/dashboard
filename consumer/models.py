from django.db import models

class Consumer(models.Model):
  Id = models.IntegerField(primary_key=True)
  SurveyId = models.CharField(max_length=500,blank=True)
  Latitude = models.CharField(max_length=500,blank=True)
  Longitude = models.CharField(max_length=500,blank=True)
  Username = models.CharField(max_length=500,blank=True)
  Date_Time = models.DateTimeField(blank=True,null=True)
  SubDivision= models.CharField(max_length=500,blank=True)
  Section= models.CharField(max_length=500,blank=True)
  BuildingReferenceNumber= models.CharField(max_length=500,blank=True)
  ConnectedPoleNo= models.CharField(max_length=500,blank=True)
  PaintedPoleNo= models.CharField(max_length=500,blank=True)
  FeederName= models.CharField(max_length=500,blank=True)
  DTCode= models.CharField(max_length=500,blank=True)
  ConsumerName= models.CharField(max_length=500,blank=True)
  NewAccountNumber= models.CharField(max_length=500,blank=True)
  OldAccountNumber= models.CharField(max_length=500,blank=True)
  SCNumber= models.CharField(max_length=500,blank=True)
  CustomerMobileNumber= models.CharField(max_length=500,blank=True)
  FlatNo= models.CharField(max_length=500,blank=True)
  Address1 = models.CharField(max_length=500,blank=True)
  Address2 = models.CharField(max_length=500,blank=True)
  Address3 = models.CharField(max_length=500,blank=True)
  ConsumerDoorLock= models.CharField(max_length=500,blank=True)
  AMRInstalled= models.CharField(max_length=500,blank=True)
  CommunicationType= models.CharField(max_length=500,blank=True)
  CTRatio= models.CharField(max_length=500,blank=True)
  DisplayCondition= models.CharField(max_length=500,blank=True)
  MaximumDemand= models.CharField(max_length=500,blank=True)
  MeterAvailability= models.CharField(max_length=500,blank=True)
  MeterBox= models.CharField(max_length=500,blank=True)
  MeterLocation= models.CharField(max_length=500,blank=True)
  HeightGT5ft= models.CharField(max_length=500,blank=True)
  MeterStatus= models.CharField(max_length=500,blank=True)
  NominalVoltage= models.CharField(max_length=500,blank=True)
  PhaseConnection= models.CharField(max_length=500,blank=True)
  SealCondition= models.CharField(max_length=500,blank=True)
  SealType= models.CharField(max_length=500,blank=True)
  TotalMF= models.CharField(max_length=500,blank=True)
  kWh= models.CharField(max_length=500,blank=True)
  Bypass= models.CharField(max_length=500,blank=True)
  Category= models.CharField(max_length=500,blank=True)
  Type= models.CharField(max_length=500,blank=True)
  SubType= models.CharField(max_length=500,blank=True)
  MeterSerialNumber= models.CharField(max_length=500,blank=True)
  MeterMake= models.CharField(max_length=500,blank=True)
  Theft= models.CharField(max_length=500,blank=True)
  BillDelivered= models.CharField(max_length=500,blank=True)
  BillShown= models.CharField(max_length=500,blank=True)
  MeterPhoto = models.ImageField(upload_to='static/media/TPWODL/MeterPhoto/',blank=True)
  BillPhoto = models.ImageField(upload_to='static/media/TPWODL/BillPhoto/',blank=True)
  OtherPhoto =  models.ImageField(upload_to='static/media/TPWODL/OtherPhoto/',blank=True)
  NeighbouringMeterNo= models.CharField(max_length=500,blank=True)
  NeighbouringConsumerNo= models.CharField(max_length=500,blank=True)
  NoofDigits= models.CharField(max_length=500,blank=True)
  SurveyorRemark= models.CharField(max_length=500,blank=True)

  class Meta:  
    db_table = "Consumer"
