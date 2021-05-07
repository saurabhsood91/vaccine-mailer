import os


def get_recipients():
    recipients = os.environ.get('recipients')
    return recipients.split(',')