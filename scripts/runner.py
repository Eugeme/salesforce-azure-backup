from utils import connect_salesforce, connect_azure
import salesforce_ids
import azure_ids
import missing_records


sf = connect_salesforce.connect()
table_names = sf.query_all('SELECT SObjectType FROM ObjectPermissions GROUP BY SObjectType')
table_names = [i['SobjectType'] for i in table_names['records']]

cnxn = connect_azure.connect()
cursor = cnxn.cursor()

for table_name in table_names:
    salesforce_ids = salesforce_ids.get_ids(sf, table_name)
    azure_ids = azure_ids.get_ids(cursor, table_name)
    missing_ids = missing_records.find_missing_ids(salesforce_ids, azure_ids)
