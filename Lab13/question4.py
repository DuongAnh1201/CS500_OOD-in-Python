from abc import ABC, abstractmethod

#Target Interface
class NewNotificationSystem(ABC):
    @abstractmethod
    def send_email_notification(self, emailAddress: str, subject: str, body: str) -> None:
        pass

    @abstractmethod
    def sendPushNotification(self, deviceToken: str, title: str, message: str) -> None:
        pass

    @abstractmethod
    def send_social_media_update(self, social_media_platform: str, postContent: str) -> None:
        pass

#Adaptee
class LegacyNotificationSystem:
    def send_sms_notification(self, phoneNumber: str, message: str) -> None:
        print("Simulates sending an SMS notification")
        print(f"  To {phoneNumber}: {message}")

#Adapter
class LegacyNotificationAdapter(NewNotificationSystem):
    def __init__(self, obj: LegacyNotificationSystem) -> None:
        self.__obj = obj

    def send_email_notification(self, emailAddress: str, subject: str, body: str) -> None:
        phone_number = self.get_phone_by_email(emailAddress)
        message = f"[Email] {subject}: {body}"
        self.__obj.send_sms_notification(phone_number, message)

    def sendPushNotification(self, deviceToken: str, title: str, message: str) -> None:
        phone_number = self.get_phone_by_device(deviceToken)
        sms = f"[Push] {title}: {message}"
        self.__obj.send_sms_notification(phone_number, sms)

    def send_social_media_update(self, social_media_platform: str, postContent: str) -> None:
        phone_number = self.get_phone_by_platform(social_media_platform)
        message = f"[{social_media_platform}] {postContent}"
        self.__obj.send_sms_notification(phone_number, message)

    #Simulates looking up the phone number linked to each channel
    def get_phone_by_email(self, emailAddress: str) -> str:
        return "111"

    def get_phone_by_device(self, deviceToken: str) -> str:
        return "222"

    def get_phone_by_platform(self, social_media_platform: str) -> str:
        return "333"

class NotificationFactory:
    @staticmethod
    def create_notification_system() -> NewNotificationSystem:
        return LegacyNotificationAdapter(LegacyNotificationSystem())

def main():
    notifier = NotificationFactory.create_notification_system()
    notifier.send_email_notification("tomnguyen6766@gmail.com", "Order", "Your order has shipped")
    notifier.sendPushNotification("IPhone 15", "Reminder", "Hellp, testing")
    notifier.send_social_media_update("Hi", "helloooo")

if __name__ == "__main__":
    main()
