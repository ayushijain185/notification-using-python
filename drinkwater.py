import time
from plyer import notification
if __name__ == '__main__':
    def notificatio():
        notification.notify(
            title="***Looking Thrusty!",
            message="Drink Some Water",
            # app_icon = "C:\Users\ayushi\Desktop\program\python\water.jpg" ,
            timeout = 20
        )
    while True:
        notificatio()
        time.sleep(60*60)


