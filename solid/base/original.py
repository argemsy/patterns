import os
import sys


class PaymentMethod:
    pass


class CreditCard(PaymentMethod):
    pass


class DebitCard(PaymentMethod):
    pass


class PaymentManager:
    """Esta clase tiene comportamientos distintos"""

    def __init__(self, raw_data: dict) -> None:
        """_summary_

        Args:
            raw_data (dict): _description_
        """
        self.raw_data = raw_data

    def load_payments(self):
        """Carga de pagos"""
        with open(os.path.join(sys.path[0], "payment.json")) as f:
            return f.read()

    def identify_payments(self):
        """Identifica el tipo de pago

        Returns:
            _type_: _description_
        """
        if self.raw_data["type"] == "credit_card":
            return CreditCard()
        elif self.raw_data["type"] == "debit_card":
            return DebitCard()

    def notify_payment(self):
        """Notifica el/los pagos"""
        print(f"Notifying payment ... {self.raw_data}")


if __name__ == "__main__":
    instance = PaymentManager({"type": "credit_card"})
