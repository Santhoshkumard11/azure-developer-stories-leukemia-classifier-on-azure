import json
import logging
from .cosmos_db_client import CosmosDBClient
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Retriving the cosmos db triggered...')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    # create a new client with our custom cosmos DB client
    db = CosmosDBClient("leukemia_classifier_db","lab_reports")
    
    # initiate cosmos db connection
    db.connect()

    return_string = db.get_all_items()
    
    return json.dumps(return_string,default=str)