from rest_framework import serializers
from piidb.models import Addresses


class AddressSerializer(serializers.ModelSerializer):
    # If your <field_name> is declared on your serializer with the parameter required=False
    # then this validation step will not take place if the field is not included.

    class Meta:
        model = Addresses
        # fields = '__all__'
        fields = ('addressid', 'aptnumber', 'city', 'nearest', 'state', 'streetname', 'streetnumber', 'zipcode', 'google_place_id')
