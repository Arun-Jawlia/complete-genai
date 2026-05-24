# Abstraction ( Using Abstract Base Class)

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def process_payment(self):
        pass


class CreditCarPayment(Payment):

    def process_payment(self):
        print("Credit Card is in Progress")


class UPIPayment(Payment):
    def process_payment(self):
        print("UPI Payment is in Progress")

creditPayment = CreditCarPayment()
creditPayment.process_payment()

upiPayment = UPIPayment()
upiPayment.process_payment()