from rest_framework.test import APITestCase, APIClient
from companies.models import Company


class CompaniesModelsTest(APITestCase):
    fixtures = ["companies.json"]

    def setUp(self):
        self.client = APIClient()

    def test_get_all_companies(self):
        companies = Company.objects.all()

        self.assertEqual(companies[0].company_name, "ABC Computers")
        self.assertEqual(companies[1].company_name, "Capital Partners")
        self.assertEqual(companies[2].company_name, "Royal Institute of Trade Studies")
