class NewPaymentGateway:
    def make_payment(self, card_details):
        pass

class OldPaymentSystem:
    def pay(self, card_details):
        print("Processing payment with Old Payment System.")

class PaymentAdapter(NewPaymentGateway):
    def __init__(self, old_system):
        self.old_system = old_system

    def make_payment(self, card_details):
        self.old_system.pay(card_details)

# Usage
old_payment_system = OldPaymentSystem()
adapter = PaymentAdapter(old_payment_system)
adapter.make_payment("1234-5678-9876-5432")
