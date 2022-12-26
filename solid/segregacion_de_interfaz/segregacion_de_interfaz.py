import os
import sys
from abc import ABC, abstractmethod, abstractstaticmethod


class PaymentReader:
    def read_payments(self):
        """Carga de pagos"""
        with open(os.path.join(sys.path[0], "payment.json")) as f:
            return f.read()


###################################################################


class Output:
    def notify_payment(self, raw_data):
        """Notifica el/los pagos"""
        print(f"Notifying payment ... {raw_data}")


###################################################################


class PaymentMethod(ABC):
    def __init__(self, raw_data) -> None:
        self.raw_data = raw_data

    @abstractstaticmethod
    def meets_condition(raw_data):
        pass

    @abstractmethod
    def pay(self):
        pass


class PaymentMethodWithCard(PaymentMethod):
    def show_card_info(self):
        pass


class CreditCard(PaymentMethodWithCard):
    @staticmethod
    def meets_condition(raw_data):
        return raw_data.get("type") == "credit_card"

    def show_card_info(self):
        print(f"""Card number {self.raw_data["credit_card_number"]}""")
        print(f"""Expire {self.raw_data["expire_date"]}""")
        print(f"""CVV {self.raw_data["cvv"]}""")

    def pay(self):
        credit_card_number = self.raw_data.get("credit_card_number")
        print(f"paying with credit card ... {credit_card_number}")

    @abstractmethod
    def show_card_info():
        pass


class DebitCard(PaymentMethodWithCard):
    @staticmethod
    def meets_condition(raw_data):
        return raw_data.get("type") == "debit_card"

    def pay(self):
        debit_card_number = self.raw_data.get("debit_card_number")
        print(f"paying with credit card ... {debit_card_number}")

    def show_card_info(self):
        print(f"""Card number {self.raw_data["debit_card_number"]}""")
        print(f"""Expire {self.raw_data["expire_date"]}""")
        print(f"""CVV {self.raw_data["cvv"]}""")


class BankTransfer(PaymentMethod):
    @staticmethod
    def meets_condition(raw_data):
        return raw_data.get("type") == "bank_tranfer"

    def pay(self):
        bank_account_number = self.raw_data.get("bank_account_number")
        print(f"paying with account number ... {bank_account_number}")


###################################################################


def process_payment(payment_method: PaymentMethod):
    payment_method.pay()


###################################################################


class PaymentManager:
    def __init__(self, raw_data: dict) -> None:
        """_summary_

        Args:
            raw_data (dict): _description_
        """
        self.raw_data = raw_data
        self.payment_reader = PaymentReader()
        self.output = Output()

    def load_payments(self):
        """_summary_"""
        self.payment_reader.read_payments()

    def identify_payments(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        for payment_method in PaymentMethod.__subclasses__():
            if payment_method.meets_condition(self.raw_data):
                return payment_method(self.raw_data)

    def notify_payment(self):
        """_summary_"""
        self.output.notify_payment(self.raw_data)


if __name__ == "__main__":
    instance = PaymentManager({"type": "credit_card", "credit_card_number": 1})
    class_name = instance.identify_payments()
    class_name_ = class_name.__class__.__name__
    print(class_name_)
    process_payment(class_name)
    print(100 * "*")

    instance2 = PaymentManager({"type": "debit_card", "debit_card_number": 2})
    class_name2 = instance2.identify_payments()
    class_name2_ = class_name2.__class__.__name__
    print(class_name2_)
    process_payment(class_name2)
    print(100 * "?")

    instance3 = PaymentManager({"type": "bank_tranfer", "bank_account_number": 3})
    class_name3 = instance3.identify_payments()
    class_name3_ = class_name3.__class__.__name__
    print(class_name3_)
    process_payment(class_name3)
    print(100 * "#")
