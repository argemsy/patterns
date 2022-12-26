import os
import sys


class PaymentReader:
    def read_payments(self):
        """Carga de pagos"""
        with open(os.path.join(sys.path[0], "payment.json")) as f:
            return f.read()
