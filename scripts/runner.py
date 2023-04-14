from utils import connect_salesforce
import salesforce_ids


sf = connect_salesforce.connect()
table_names = sf.query_all("SELECT SObjectType FROM ObjectPermissions GROUP BY SObjectType")
table_names = [i['SobjectType'] for i in table_names['records']]

for table_name in table_names:
    ids = salesforce_ids.get_ids(sf, table_name)
