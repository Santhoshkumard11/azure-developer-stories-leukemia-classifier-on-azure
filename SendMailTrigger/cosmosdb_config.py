import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://leukemia-cosmosdbs-eus.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'YOUR ACCOUNT KEY'),
    'database_id': os.environ.get('COSMOS_DATABASE', 'imagecontainer'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),
}
