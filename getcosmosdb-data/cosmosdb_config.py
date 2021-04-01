import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://leukemia-cosmosdbs-eus.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'a3mp9H8rOtfoAlg1TBOlhPVVxfXpawMNQAr00A0aW4U3io0gtKPYUe4lksJEPazVPSP1PswAD893VsG1J7qO12Q=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'imagecontainer'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),
}
