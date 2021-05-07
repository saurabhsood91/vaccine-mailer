import boto3

from botocore.exceptions import ClientError
from typing import List

from . import AWS_REGION, RECIPIENT, SENDER, CHARSET, SUBJECT, EMAIL_TEMPLATE
from util.dateutils import get_formatted_date


def _format_content(appointments: List) -> str:
    appointment_str = []
    for appointment in appointments:
        name = appointment["name"]
        address = appointment["name"]
        district = appointment["district"]
        to_val = appointment["to"]
        from_val = appointment["from"]
        age_limit = appointment["age_limit"]
        date = appointment["date"]
        vaccine = appointment["vaccine"]
        app_str = """
        <b>Name:</b> {name}
        <b>Address:</b> {address}
        <b>District:</b> {district}
        <b>From:</b> {from_val}
        <b>To:</b> {to_val}
        <b>Age Limit:</b> {age_limit}
        <b>Date:</b> {date}
        <b>Vaccine:</b> {vaccine}
        """.format(name=name, address=address, district=district, vaccine=vaccine, age_limit=age_limit, to_val=to_val, from_val=from_val, date=date)
        appointment_str.append(app_str)
    return "<br /><br />".join(appointment_str)


def send_email(body, recipients):
    client = boto3.client('ses', region_name=AWS_REGION)

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': recipients,
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': body
                    }
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT
                }
            },
            Source=SENDER,
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print('Email successfully sent!, {}'.format(response['MessageId']))


def render_email_template(appointments):
    current_date = get_formatted_date()
    formatted_content = _format_content(appointments)
    return EMAIL_TEMPLATE.format(current_date=current_date, content=formatted_content)
