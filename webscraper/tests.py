from django.test import TestCase


class TestCI(TestCase):

    def test_continuous_integration(self):
        self.assertTrue(True)

    def test_continuous_integration_2(self):
        self.assertEqual(1 + 1, 2)
