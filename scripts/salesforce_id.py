def get_ids(sf, table_name):
    ids = sf.query_all(f'SELECT Id FROM {table_name}')

    ids = [i['Id'] for i in ids['records']]

    print(f'records in {table_name}: {str(len(ids))}')

    return ids

