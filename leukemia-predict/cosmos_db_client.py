import logging
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import datetime
import os

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

    def update_item(self, predicted_type, image_name):
        """Update the item with the prediction result

        Args:
            predicted_type ([type]): the type of leukemia
            image_name ([type]): name of the test image
        """

        # get the document id from the image name
        doc_id = image_name.split('_')[0]

        # get the document from cosmos db
        read_item = self.container.read_item(
            item=doc_id, partition_key=image_name)

        # update the predicted_type
        read_item['detection_results']['predicted_type'] = predicted_type

        try:
            # push the updated item to cosmos db
            response = self.container.upsert_item(body=read_item)
            logging.info(f"Successfully updated the item with the name as {image_name}")
        except Exception as e:
            pass
            logging.error(
                f"Can't update the item with the id {doc_id}, predicted result {predicted_type}, image name {image_name}")
