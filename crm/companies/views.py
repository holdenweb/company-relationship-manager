from rest_framework import viewsets
from companies.models import Company
from companies.serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
