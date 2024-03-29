"""Simple Salesforce is a basic Salesforce.com REST API client built for Python.
  https://buildmedia.readthedocs.org/media/pdf/simple-salesforce/latest/simple-salesforce.pdf"""

from simple_salesforce import Salesforce
from dotenv import dotenv_values


def connect():
    """create connection with salesforce"""

    config = dotenv_values('.env')  # take environment variables from .env file

    username = config['SF_USERNAME']
    password = config['SF_PASSWORD']
    security_token = config['TOKEN']
    instance = config['INSTANCE']
    domain = config['DOMAIN']

    sf = Salesforce(username=username,
                    password=password,
                    security_token=security_token,
                    instance=instance,
                    domain=domain,
                    client_id='Backup script')   # track where your API calls come from by adding client_id
    return sf
