import logging
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey

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

    def get_all_items(self):
        """ Read all the items from cosmos db
        """
        read_items = ""
        
        try:
            # get the document from cosmos db
            read_items = list(self.container.read_all_items(max_item_count=10))
        
            logging.info(f"Successfully received the data")
            
        except Exception as e:
            pass
            logging.error(
                f"Error while getting the items from the container")
            
        return read_items
    