import os

from errors.exceptions import EnvironmentException
from emails.interface import render_email_template, send_email
from util.email import get_recipients
from util.vaccine import fetch_vaccine_appointments


def validate_environment():
    email = os.environ.get('email')
    aws_region = os.environ.get('aws_region')
    recipients = os.environ.get('recipients')

    return (email is not None) and (aws_region is not None) and (recipients is not None)


def _process():
    appointments = fetch_vaccine_appointments()
    email_body = render_email_template(appointments)
    recipients = get_recipients()

    send_email(email_body, recipients)


def main(event=None, context=None):
    if not validate_environment():
        raise EnvironmentException('Environment misconfigured')
    _process()


if __name__ == '__main__':
    main('', '')