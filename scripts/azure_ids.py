def get_ids(cursor, table_name):

    cursor.execute(f'SELECT Id FROM dbo.{table_name}')
    ids = cursor.fetchall()

    ids = [i[0] for i in ids]
    print(f'records in database: {str(len(ids))}')

    return ids
