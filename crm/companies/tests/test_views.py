from os import stat
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class CompaniesViewsTest(APITestCase):
    fixtures = ["companies.json"]

    def setUp(self):
        self.client = APIClient()

    def test_get_all_companies(self):
        response = self.client.get("/companies/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "ABC Computers")
        self.assertContains(response, "Capital Partners")
        self.assertContains(response, "Royal Institute of Trade Studies")

    def test_get_a_company(self):
        response = self.client.get("/companies/1/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "ABC Computers")
        self.assertNotContains(response, "Capital Partners")
        self.assertNotContains(response, "Royal Institute of Trade Studies")

    def test_get_all_companies_json(self):
        response = self.client.get("/companies.json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response["content-type"], "application/json")
