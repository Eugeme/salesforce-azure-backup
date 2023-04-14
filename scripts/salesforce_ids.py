from utils import connect_salesforce
from simple_salesforce import exceptions


def get_ids():
    sf = connect_salesforce.connect()

    table_names = sf.query_all('SELECT SObjectType FROM ObjectPermissions GROUP BY SObjectType')
    table_names = [i['SobjectType'] for i in table_names['records']]

    all_ids = []

    for table_name in table_names:
        try:
            ids = sf.query_all(f'SELECT Id FROM {table_name}')
        except exceptions.SalesforceMalformedRequest:
            continue

        all_ids += [i['Id'] for i in ids['records']]

        print(f'records in {table_name}: {str(len(ids))}')

    return all_ids
