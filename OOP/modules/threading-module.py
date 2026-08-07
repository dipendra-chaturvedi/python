import threading
import time


def send_email():
    time.sleep(3)
    print("Email Sent")


def send_sms():
    time.sleep(2)
    print("SMS Sent")


def save_audit_log():
    time.sleep(1)
    print("Audit Log Saved")


email_thread = threading.Thread(target=send_email)
sms_thread = threading.Thread(target=send_sms)
log_thread = threading.Thread(target=save_audit_log)

email_thread.start()
sms_thread.start()
log_thread.start()

email_thread.join()
sms_thread.join()
log_thread.join()

print("Employee Registration Completed")


#Thread()
#start()
#join()
#Lock()
#Event()
#Semaphore()