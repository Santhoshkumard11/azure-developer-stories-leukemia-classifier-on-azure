import logging
from mailjet_rest import Client

api_key = 'b0c0da5d8f5e215c5499dc644a98e93a'
api_secret = '85a8d2afcf895ef72d176e9395ea30f9'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')

def send_email(patient_name:str, mail_type = "doc", leukemia_type = "no"):
    """Send the patient or the chief doctor the mail for final approval

    Args:
        patient_name (str): name of the patient
        mail_type (str, optional): to whom it should be sent. Defaults to "doc".
        leukemia_type (str, optional): the type of leukemia predicted. Defaults to "no".

    Returns:
        [type]: [description]
    """
    
    data = {
            "Messages": [
                {
                    "From": {"Email": "santhoshkdhana@gmail.com", "Name": "WuhanLab"},
                    "To": [{"Email": "santhoshkumar112232@gmail.com"}],
                    "Subject": "Update - New report Review",
                    "TextPart": f"Hi Doc, \n\nThis is to inform you that the initial testing for the patient {patient_name} is complete. \n\n Requesting you to review and make the final decision.",
                    "CustomID": "AppGettingStartedTest",
                }
            ]
        }
    
    if mail_type != "doc":
        
        data = {
            "Messages": [
                {
                    "From": {"Email": "santhoshkdhana@gmail.com", "Name": "WuhanLab"},
                    "To": [{"Email": "santhoshkumar112232@gmail.com"}],
                    "Subject": "Update on your Leukemia Test - Positive Result",
                    "TextPart": f"Hi {patient_name}, \n\nWe are sorry to inform that you are diagnosed with leukemia of {leukemia_type} type. You will get guidance for the futher process from our office staff on your treatment.",
                    "CustomID": "AppGettingStartedTest",
                }
            ]
        }
    
    
    result = mailjet.send.create(data=data)
    print(result.status_code)

    logging.info("Email sent successfully!!!")