def find_missing_ids(salesforce_ids, azure_ids):
    missing_ids = tuple(set(salesforce_ids) - set(azure_ids))
    return missing_ids, len(missing_ids)
