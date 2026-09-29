import notification as noti

test_notif = noti.CreateNotification(title="Hello", message="World")
email_notif = noti.CreateNotification(title="Email", message="You have 1 new email", icon="email", wait=5)
instagram_notif = noti.CreateNotification(title="Instagram", message=f"@digse: \nHello :3", icon="instagram", wait=1)
docker_notif = noti.CreateNotification(title="Docker Desktop", message="Image succsessfully built", icon="docker", wait=30) #succsesfully waits full 30seconds
#note: windows default notification might be overidding wait intervals if its less than however long the windows pop up stays for.