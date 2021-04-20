from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from piiapi.serializers import AddressSerializer
from piidb.models import Addresses, query_address_by_args

# Create your views here.
class AddressesViewSet(viewsets.ModelViewSet):
    queryset = Addresses.objects.all()
    serializer_class = AddressSerializer

    def list(self, request, **kwargs):
        try:
            addresses = query_address_by_args(**request.query_params)
            serializer = AddressSerializer(addresses['items'], many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = addresses['draw']
            result['recordsTotal'] = addresses['total']
            result['recordsFiltered'] = addresses['count']
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)
