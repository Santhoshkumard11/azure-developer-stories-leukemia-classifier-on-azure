import logging
from .leukemia_model import predict_output
from .file_operation import get_file_name_from_image_url, remove_file, save_file
from .cosmos_db_client import CosmosDBClient

def start_prediction_process(image_url: str):
    """
    Args:
        image_url (str): storage url of the image

    Returns:
        [str]: final prediction of the model
    """

    logging.info('Process started...')
    
    # get the image name from the url
    image_name = get_file_name_from_image_url(image_url)
    
    file_obj,temp_file_name = save_file(image_url)

    # get the predicted result from the ML model
    predicted_result = predict_output(temp_file_name)

    # create a new client with our custom cosmos DB client
    db = CosmosDBClient("leukemia_classifier_db","lab_reports")
    
    # initiate cosmos db connection
    db.connect()
    
    # updating the result of the prediction
    db.update_item(predicted_result, image_name)

    # close the file operation
    file_obj.close()
    
    # remove the image file which was downloaded for prediction
    # remove_file(temp_file_name)
    

    logging.info('Process ended successfully')

    return predicted_result
