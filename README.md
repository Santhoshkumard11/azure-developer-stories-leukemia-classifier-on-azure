# azure-developer-stories-leukemia-classifier-on-azure
Building a serverless leukemia classifier using Azure Functions and Logic Apps.


## List of services used
1. Azure function
2. Logic Apps
3. Cosmos DB
4. Blob Storage
5. Mailjet
6. Azure Devops

![screenshot](/images/resources-group-1.JPG)

## 1. Azure Function

- leukemia-predict -> triggered from logic app when a change in blob storage is detected
- StaticPage -> present the index page our application


![screenshot](/images/function-1.JPG)

## 2. Logic Apps

- Used to trigger the Azure function if a change is made to blob storage 

![screenshot](/images/logic-apps-1.JPG)

![screenshot](/images/logic-apps-2.JPG)

## 3. Cosmos DB

- Store the patient, prediction and hematologists details


example item stored in Cosmos DB

{
    "id": "865109",
    "patient_details": {
        "patient_name": "Samantha",
        "image_name": "865109_Wuhan_lab_1_Apr_21.jpg",
        "blood_group": "O+",
        "Age": "22"
    },
    "detection_results": {
        "predicted_type": "ALL",
        "diagnosed_with_leukemia": "no",
        "false_prediction_count": "0"
    },
    "physicians_results": {
        "hematologists1": "yes",
        "hematologists2": "yes",
        "chief_hematologists": "not evaluated"
    }
}

![screenshot](/images/cosmosdb-1.JPG)

## 4. Blob Storage

- To store the lab reports (microscopic blood sample images)

![screenshot](/images/blob-storage-1.JPG)

## 5. Mailjet

- Using SMTP relay in logic apps and API in Azure Functions to send out the mails to patients and hematologists

![screenshot](/images/mailject-1.JPG)

## 6. Azure Devops

- Create a issue work item if the prediction is wrong or misclassified by our custom ML model.

![screenshot](/imagesdevops-1.JPG)