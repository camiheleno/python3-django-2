# coding=utf-8
from django.test import TestCase
from model_mommy import mommy
from ..models import Financial, FinancialType


class TestFinancial(TestCase):

    def setUp(self):
        self.financial_type = mommy.make(FinancialType, name='Test Type')
        self.financial = mommy.make(Financial, name='Test', value=10.0, type=self.financial_type)

    def test_record_creation(self):
        self.assertTrue(isinstance(self.financial, Financial))
        self.assertEquals(self.financial.__str__(), self.financial.name)
