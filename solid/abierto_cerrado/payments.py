from abc import ABC, abstractstaticmethod


class PaymentMethod(ABC):
    @abstractstaticmethod
    def meets_condition(raw_data):
        pass


class CreditCard(PaymentMethod):
    @staticmethod
    def meets_condition(raw_data):
        return raw_data.get("type") == "credit_card"


class DebitCard(PaymentMethod):
    @staticmethod
    def meets_condition(raw_data):
        return raw_data.get("type") == "debit_card"


class BankTransfer(PaymentMethod):
    @staticmethod
    def meets_condition(raw_data):
        return raw_data.get("type") == "bank_tranfer"
