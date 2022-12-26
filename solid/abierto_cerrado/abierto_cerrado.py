from solid.abierto_cerrado.payments import (
    BankTransfer,
    CreditCard,
    DebitCard,
    PaymentMethod,
)
from solid.responsabilidad_unica.output import Output
from solid.responsabilidad_unica.payment_reader import PaymentReader


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
                return payment_method()

    def notify_payment(self):
        """_summary_"""
        self.output.notify_payment(self.raw_data)


if __name__ == "__main__":
    instance = PaymentManager({"type": "credit_card"})
