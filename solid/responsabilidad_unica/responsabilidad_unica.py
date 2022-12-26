from solid.responsabilidad_unica.output import Output
from solid.responsabilidad_unica.payment_reader import PaymentReader


class PaymentMethod:
    pass


class CreditCard(PaymentMethod):
    pass


class DebitCard(PaymentMethod):
    pass


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
        if self.raw_data["type"] == "credit_card":
            return CreditCard()
        elif self.raw_data["type"] == "debit_card":
            return DebitCard()

    def notify_payment(self):
        """_summary_"""
        self.output.notify_payment(self.raw_data)


if __name__ == "__main__":
    instance = PaymentManager({"type": "credit_card"})
