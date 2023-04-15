from utils import connect_salesforce, connect_azure
import salesforce_id
import azure_id
import missing_records
from simple_salesforce import exceptions
import pyodbc

sf = connect_salesforce.connect()
table_names = sf.query_all('SELECT SObjectType FROM ObjectPermissions GROUP BY SObjectType')
table_names = [i['SobjectType'] for i in table_names['records']]

cursor = connect_azure.connect()

for table_name in table_names:
    try:
        salesforce_ids = salesforce_id.get_ids(sf, table_name)
        azure_ids = azure_id.get_ids(cursor, table_name)
        missing_ids = missing_records.find_missing_ids(salesforce_ids, azure_ids)

    except exceptions.SalesforceMalformedRequest as e:
        print(e)
        continue

    except pyodbc.ProgrammingError as e:
        print(f'no {table_name} object in Azure')
        continue
