from companies.models import Company
from companies.serializers import CompanySerializer
from rest_framework.test import APIClient, APITestCase


class CompaniesSerializersTest(APITestCase):
    fixtures = ["companies.json"]

    def setUp(self):
        self.client = APIClient()

    def test_get_all_companies(self):
        companies = Company.objects.all()

        serializer = CompanySerializer(companies, many=True)

        self.assertEqual(serializer.data[0]["company_name"], "ABC Computers")
        self.assertEqual(serializer.data[1]["company_name"], "Capital Partners")
        self.assertEqual(
            serializer.data[2]["company_name"], "Royal Institute of Trade Studies"
        )
