from SendMailTrigger.cosmos_db_client import CosmosDBClient
import logging

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    patient_id = req.params.get('patient_id')

    # create a new client with our custom cosmos DB client
    db = CosmosDBClient("leukemia_classifier_db","lab_reports")
    
    # initiate cosmos db connection
    db.connect()

    item = db.get_item(patient_id)
    
    db.validate_send_result(item)

    return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
