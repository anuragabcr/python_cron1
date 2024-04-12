import schedule
import time

from actions import find_documents 

def job():
    print("Hello")
    cursor = find_documents("Anurag", "students", {})
    for document in cursor:
        print(document)

schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(59)
