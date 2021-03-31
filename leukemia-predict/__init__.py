import azure.functions as func
import logging
from .driver import start_prediction_process

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Funcation Triggered....')

    # get the params from the request

    # image_url = req.get["image_url"]
    
    # if it's not in the url search it in the request body

    req_body = req.get_json()

    image_url = req_body.get('image_url')

    # Test response for trigger testing
    # if name == "demo":
    #     return func.HttpResponse(f"Thanks for using our ML service. Pass a different parameter to get the model working!!")       
     
    logging.info('Entering into prediction mode..')
    
    predicted_result = start_prediction_process(image_url)

    return func.HttpResponse(f"The predicted output is {predicted_result}")
