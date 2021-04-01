import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://leukemia-cosmosdb-eus.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'a3mp9H8rOtfoAlg1TBOlhPVVxfXpawMNQAr00A0aW4U3io0gtKPYUe4lksJEPazVPSP1PswAD893VsGJ7qO12Q=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'imagecontainer'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),
}
