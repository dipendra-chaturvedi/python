class Notification:

    def send(self, message):
        pass

class Email(Notification):

    def send(self, message):
        print("Email:", message)

class SMS(Notification):

    def send(self, message):
        print("SMS:", message)

class WhatsApp(Notification):

    def send(self, message):
        print("WhatsApp:", message)

Email().send("Welcome")
SMS().send("OTP: 1234")
WhatsApp().send("Order Delivered")