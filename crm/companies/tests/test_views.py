from rest_framework import status
from rest_framework.test import APIClient, APITestCase


# class CompaniesViewsTest(APITestCase):
#     fixtures = ["books.json", "users.json"]

#     def setUp(self):
#         self.client = APIClient()

#     def test_get_all_books(self):
#         response = self.client.get("/books/")

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertContains(response, "Moby-Dick")
#         self.assertContains(response, "Architecture Patterns with Python")
#         self.assertContains(response, "The Oxford Handbook of Happiness")

#     def test_get_a_book(self):
#         response = self.client.get(f"/books/1/")

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertContains(response, "Moby-Dick")
#         self.assertNotContains(response, "Architecture Patterns with Python")
#         self.assertNotContains(response, "The Oxford Handbook of Happiness")

#     def test_get_all_books_json(self):
#         response = self.client.get("/books.json")

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response["content-type"], "application/json")
