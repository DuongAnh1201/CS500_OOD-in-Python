from abc import ABC, abstractmethod

#Target Interface
class PayPalPaymentGateWay(ABC):
    @abstractmethod
    def process_paypal_payment(self, email_address: str, amount: float) -> bool:
        pass

#Adaptee
class LegacyPaymentGateway:
    def process_credit_card_payment(self, credit_card_number: str, expiration_date: str, cvv: str, amount: float) -> bool:
        print("Simulates processing a credit card payment")
        return True

#Adapter
class LegacyPaymentAdapter(PayPalPaymentGateWay):
    def __init__(self, obj: LegacyPaymentGateway) -> None:
        self.__obj = obj

    def process_paypal_payment(self, email_address: str, amount: float) -> bool:
        credit_card_number = self.get_credit_number(email_address)
        expiration_date = self.get_expiration_date(email_address)
        cvv = self.get_cvv(email_address)
        return self.__obj.process_credit_card_payment(credit_card_number, expiration_date, cvv, amount)

    #Simulates looking up the card linked to the PayPal account
    def get_credit_number(self, email_address: str) -> str:
        return "1111222233334444"

    def get_expiration_date(self, email_address: str) -> str:
        return "11/26"

    def get_cvv(self, email_address: str) -> str:
        return "000"

class PaymentGateWayFactory:
    @staticmethod
    def create_gateway() -> PayPalPaymentGateWay:
        return LegacyPaymentAdapter(LegacyPaymentGateway())

def main():
    payment = PaymentGateWayFactory.create_gateway()
    print(payment.process_paypal_payment("customer@example.com", 1000.0))

if __name__ == "__main__":
    main()
