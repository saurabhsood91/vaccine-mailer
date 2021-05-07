import os


def get_recipients():
    recipients = os.environ('recipients')
    return recipients.split(',')