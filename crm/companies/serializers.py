from rest_framework import serializers
from companies.models import Company


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = [
            "date_created",
            "company_name",
            "registered_name",
            "email",
            "company_reference",
        ]
