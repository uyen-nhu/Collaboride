import os
from dotenv import load_dotenv
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

# Load our .env file to environment
load_dotenv()
# We got our access and secret key without hardcoding!
mailchimp_api_token = os.getenv('MAILCHIMP_API_TOKEN')


def send_email_to_emails(api_key=mailchimp_api_token):

    client = MailchimpMarketing.Client()
    client.set_config({
        "api_key": api_key,
        "server": "us17"
    })

    response = client.campaigns.list()
    print(response)
    try:
        response = client.campaigns.send(campaign_id='dcc95451e4')
        print(response)
    except ApiClientError as error:
        print("Error: {}".format(error.text))
