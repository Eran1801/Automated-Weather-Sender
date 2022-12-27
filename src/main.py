from deta import app
from weather import *


# define a function to run on a schedule
# the function must take an event as an argument
@app.lib.cron()
def cron_job(event):
    send_email(subject="My LOVE",
               receiver_email=receiver_email,
               message=create_message())
    return 'OK'
