#! -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase, RequestFactory

User = get_user_model()


class InitialTestCase(TestCase):

    def test_1_plus_1(self):
        self.assertEqual(1 + 1, 2)
