import codecs
import csv

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

fs = FileSystemStorage(location='tmp/')

from .models import Site
# Create your views here.
# Serializer
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Site
        fields = "__all__"


# Viewset
class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Product.
    """
    queryset = Site.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        """Upload data from CSV"""
        file = request.FILES["file"]

        content = file.read()  # these are bytes
        file_content = ContentFile(content)
        file_name = fs.save(
            "_tmp.csv", file_content
        )
        tmp_file = fs.path(file_name)

        csv_file = open(tmp_file, errors="ignore")
        reader = csv.reader(csv_file)
        next(reader)
        
        product_list = []
        for id_, row in enumerate(reader):
            (
                site_id	,
                site_name,
                country,
                order_id,
                purchase_id,
                csm_name,
                serial,
                ip_address,
                model,
                macaddr
               
            ) = row
            product_list.append(
                Site(
                    site_id=site_id,
                    site_name = site_name,
                    country = country,
                    order_id = order_id,
                    purchase_id = purchase_id,
                    csm_name = csm_name,
                    serial =serial,
                    ip_address =ip_address,
                    model = model,
                    macaddr = macaddr


                
                )
            )

        Site.objects.bulk_create(product_list)

        return Response("Successfully upload the data")
