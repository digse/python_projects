from notifypy import Notify
import time

"""
* notification program using the notifypy library
* wanted to turn it into a class so it could be reused for mutiple notifications

* new class syntax is 
    CreateNotification
        (
        title, 
        message, 
        icon (changable), 
        wait (defaults to 0.1 unless changed)
        )

* for testing purposes under /icons is where icons are located; free use downloaded from: https://icon-icons.com/
"""

class CreateNotification:
    def __init__(self, title: str, message: str, icon: str="default", wait: int=0.1):
        self.title = title
        self.message = message
        self.icon = 'icons/' + icon + '.png'
        self.wait = time.sleep(wait)
        self.send_notification()

    def send_notification(self):
        notification = Notify()

        notification.title = self.title
        notification.message = self.message
        notification.icon = self.icon
        notification.application_name = "Notification"
        notification.send()

#email:CreateNotification = CreateNotification(title="Email", message="You have 1 new email", icon="email", wait=1)
#instagram_notification:CreateNotification = CreateNotification(title="Instagram", message=f"@digse: \nHello :3", icon="instagram", wait=1)
#docker_notification:CreateNotification = CreateNotification(title="Docker Desktop", message="Image succsessfully built", icon="docker", wait=1)