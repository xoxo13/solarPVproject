from rest_framework import serializers
from ..models import Product, Certificate, Service


class ProductSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Product
		fields = ['modelNum', 'name', 'cellTechnology', 'cellManufacturer', 'numberOfCells',
		    'numberOfCellsInSeries', 'numberOfSeriesStrings','numberOfDiodes', 'productLength', 
		    'productWidth', 'productWeigtht', 'superstrateType', 'superstrateManufacturer', 
		    'substrateType', 'substrateManufacturer', 'frameType', 'frameAdhesive', 
		    'encapsulantType', 'encapsulantManufacturer', 'junctionBoxType', 'junctionBoxManufacturer'
			]

	
class CertificateSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Certificate
		fields = ['cert_ID', 'certNumber', 'locationID', 'reportNumber',
			'userID', 'testStandard', 'productID', 'certIssueDate'
			]


class ServiceSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Service
		fields = ['serviceID', 'serviceName','description', 'isFIrequired',
			'fiFrequency', 'testStandardID' 
			]
