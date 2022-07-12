import time
from plyer import notification
if __name__  ==  "__main__" :
    while True:
        notification.notify(
            title = "Please drink water now",
            message = "Getting enough water every day is important for your health. Drinking water can prevent dehydration, a condition that can cause unclear thinking, result in mood change, cause your body to overheat, and lead to constipation and kidney stones.",
            app_icon = "C://Users//HP//OneDrive//Documents//resumeprojects//desktopnotification//icon1.ico",
            timeout = 12
            ) 
      #  time.sleep(6)
        time.sleep(60*60)

     