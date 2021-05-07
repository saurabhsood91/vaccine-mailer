import os

EMAIL_TEMPLATE = """
<html>
    <head></head>
    <body>
        <h1>Vaccine appointments in Pune: {current_date}</h1>
        <div>
            {content}
        </div>
    </body>
</html>
"""

SENDER = RECIPIENT = os.environ.get('email')

AWS_REGION = os.environ.get('aws_region')
SUBJECT = 'Vaccine appointment'
CHARSET = 'UTF-8'
