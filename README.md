# Azure Dev Stories - Leukemia Classifier on Azure Cloud #azuredevstories
Building a serverless leukemia classifier using Azure Functions and Logic Apps.

#azuredevstories

![azureporatgif](/images/azure-portal-gif.gif)

## YouTube Demo Video

https://youtu.be/6cub1Ifr6Wg

## Medium Blog

Link -> [Trigger Based Leukemia Classifier on Azure Cloud — Prediction and Reporting](https://santhoshkdhana.medium.com/trigger-based-leukemia-classifier-on-azure-cloud-prediction-and-reporting-6a1069b6406f)

## List of services used
1. Azure function
2. Logic Apps
3. Cosmos DB
4. Blob Storage
5. Mailjet
6. Azure Devops

![screenshot](/images/resource-group.JPG)

## 1. Azure Function

- leukemia-predict -> triggered from logic app when a change in blob storage is detected
- StaticPage -> present the index page our application
- SendMailTrigger -> Triggered when there is a change in Cosmos DB
- getcosmosdb-data -> will return all the items in the cosmos DB

![screenshot](/images/function-1.JPG)

## 2. Logic Apps

- Used to trigger the Azure function if a change is made to blob storage 

![screenshot](/images/logic-apps-1.JPG)

![screenshot](/images/logic-apps-2.JPG)

## 3. Cosmos DB

- Store the patient, prediction and hematologists details

![screenshot](/images/cosmosdb-1.JPG)

## 4. Blob Storage

- To store the lab reports (microscopic blood sample images)

![screenshot](/images/blob-storage-1.JPG)

## 5. Mailjet

- Using SMTP relay in logic apps and API in Azure Functions to send out the mails to patients and hematologists

![screenshot](/images/mailjet-1.JPG)

## 6. Azure Devops

- Create a issue work item if the prediction is wrong or misclassified by our custom ML model.

![screenshot](/images/devops-1.JPG)
