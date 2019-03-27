from django.db import models
# Create your models here.


class Client(models.Model):
    clientID = models.CharField(max_length=3)
    clientName = models.CharField(max_length=25)
    clientType = models.CharField(max_length=25)

    def __str__(self):
        return self.clientID


class User(models.Model):
    userID = models.CharField(max_length=25)
    clientID = models.ForeignKey(Client, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=15)
    middlleName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)
    jobTitle = models.CharField(max_length=15)
    email = models.CharField(max_length=15)
    officePhone = models.CharField(max_length=15)
    cellPhone = models.CharField(max_length=15)
    prefix = models.CharField(max_length=10)

    def __str__(self):
        return self.userID


class Location(models.Model):
    locationID = models.IntegerField()
    clientID = models.ForeignKey(Client, on_delete=models.CASCADE)
    address1 =  models.CharField(max_length=25)
    address2 =  models.CharField(max_length=25)
    city =  models.CharField(max_length=25)
    state =  models.CharField(max_length=25)
    postalCode =  models.CharField(max_length=25)
    country =  models.CharField(max_length=25)
    phoneNumber =  models.CharField(max_length=25)
    faxNumber =  models.CharField(max_length=25)

    def __str__(self):
        return self.locationID


class TestStandard(models.Model):
    testStandardID = models.IntegerField()
    standardName = models.CharField(max_length=25)
    description = models.TextField()
    publishedDate = models.DateField()

    def __str__(self):
        return self.testStandardID


class Service(models.Model):
    serviceID = models.CharField(max_length=25)
    serviceName = models.CharField(max_length=25)
    description = models.TextField()
    isFIrequired = models.BooleanField()
    fiFrequency = models.IntegerField()
    testStandardID = models.ForeignKey(TestStandard, on_delete=models.CASCADE)

    def __str__(self):
        return self.serviceID


class Product(models.Model):
    modelNum = models.IntegerField()
    name =  models.CharField(max_length=25)
    cellTechnology = models.CharField(max_length=25)
    cellManufacturer = models.CharField(max_length=25)
    numberOfCells = models.IntegerField()
    numberOfCellsInSeries = models.IntegerField()
    numberOfSeriesStrings = models.IntegerField()
    numberOfDiodes = models.IntegerField()
    productLength = models.FloatField(max_length=25)
    productWidth = models.FloatField(max_length=25)
    productWeigtht = models.FloatField(max_length=25)
    superstrateType = models.CharField(max_length=25)
    superstrateManufacturer = models.CharField(max_length=25)
    substrateType = models.CharField(max_length=25)
    substrateManufacturer = models.CharField(max_length=25)
    frameType = models.CharField(max_length=25)
    frameAdhesive = models.CharField(max_length=25)
    encapsulantType = models.CharField(max_length=25)
    encapsulantManufacturer = models.CharField(max_length=25)
    junctionBoxType = models.CharField(max_length=25)
    junctionBoxManufacturer = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class TestSequence(models.Model):
    SequenceID = models.CharField(max_length=25)
    SequenceName =  models.CharField(max_length=25)

    def __str__(self):
        return self.SequenceID


class PerformanceData(models.Model):
    modelNum = models.ForeignKey(Product, on_delete=models.CASCADE)
    testSequenceID = models.ForeignKey(TestSequence, on_delete=models.CASCADE)
    maxSystemVoltage = models.IntegerField()
    voc = models.IntegerField()
    isc = models.IntegerField()
    vmp = models.IntegerField()
    imp = models.IntegerField()
    pmp = models.IntegerField()
    ff = models.IntegerField()

    def __str__(self):
        return self.modelNum


class Certificate(models.Model):
    cert_ID = models.IntegerField()
    certNumber = models.IntegerField()
    locationID =  models.ForeignKey(Location, on_delete=models.CASCADE)
    reportNumber = models.IntegerField()
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    testStandard = models.ForeignKey(TestStandard, on_delete=models.CASCADE)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)
    certIssueDate = models.DateField()

    def __str__(self):
        return self.cert_ID