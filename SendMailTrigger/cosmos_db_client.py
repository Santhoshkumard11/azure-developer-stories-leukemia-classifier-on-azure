from SendMailTrigger.devops_api import create_issue
import logging
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import datetime
import os
from SendMailTrigger.send_mail import send_email

from . import cosmosdb_config

# Building a custom cosmos db client

class CosmosDBClient:

    def __init__(self, database_name: str, container_name: str):
        
        # get all the configurations to connect to the Cosmos DB
        self.HOST = cosmosdb_config.settings['host']
        self.MASTER_KEY = cosmosdb_config.settings['master_key']
        self.DATABASE_ID = cosmosdb_config.settings['database_id']
        self.CONTAINER_ID = cosmosdb_config.settings['container_id']

        self.database_name = database_name

        self.container_name = container_name

    def connect(self):
        """ Initiate a connection to cosmos DB
        """
        # connect with the cosmos DB client
        self.client = cosmos_client.CosmosClient(
            self.HOST, {'masterKey': self.MASTER_KEY}, user_agent="CosmosDB", user_agent_overwrite=True)

        # get the database connection object
        self.database = self.client.create_database_if_not_exists(
            id=self.database_name)

        # get the container connection object
        self.container = self.database.create_container_if_not_exists(
            id=self.container_name,
            partition_key=PartitionKey(path="/patient_details/image_name"),
            offer_throughput=400
        )

    def get_item(self, doc_id):
        """Update the item with the prediction result

        Args:
            predicted_type ([type]): the type of leukemia
        """

        image_name = doc_id + "_Wuhan_lab_1_Apr_21.jpg"

        try:
            # read the item from cosmos db
            read_item = self.container.read_item(
                item=doc_id, partition_key=image_name)
            
            logging.info(f"Successfully retrieved the item with the name {image_name}")
            
            return read_item
        
        except Exception as e:
            pass
            logging.error(
                f"Can't retrieve the item with the id {doc_id}, image name {image_name}")


    def validate_send_result(self, item):
        """Validate if both the hematologists have verified the result and send the result via mail

        Args:
            item ([object]): cosmos db item
        """
        patient_name = item["patient_details"]["patient_name"]
        leukemia_type = item["detection_results"]["predicted_type"]
        
        patient_id = item["id"]
        
        mail_type = ""
        
        if item["physicians_results"]["hematologists1"] == "yes" and item["physicians_results"]["hematologists2"] == "yes":
            mail_type = "doc"
        
        if item["physicians_results"]["chief_hematologists"] == "yes":
            mail_type = "patient"

        logging.info("Evaluated successfully!!")

        # send mail to the patient or the chief doctor
        send_email(patient_name,mail_type,leukemia_type)

        if item["detection_results"]["false_prediction_count"] == "1":

            logging.info("Creating  a work item in devops....")

            # create a new issue in azure devops
            create_issue(f"Misclassification image with id - {patient_id}")