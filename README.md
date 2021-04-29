CosmoDB
Prerequisites

Azure subscription
create cosmo db account

Go to the Azure portal to create an Azure Cosmos DB account. Search for and select Azure Cosmos DB.
Select Add.
On the Create Azure Cosmos DB Account page, enter the basic settings for the new Azure Cosmos account.
Select Review + create. You can skip the Network and Tags sections.
Review the account settings, and then select Create. It takes a few minutes to create the account. Wait for the portal page to display Your deployment is complete
Select Go to resource to go to the Azure Cosmos DB account page.
Add a database and a container
Select Data Explorer from the left navigation on your Azure Cosmos DB account page, and then select New Container.
In the Add container pane, enter the settings for the new container.
Select OK. The Data Explorer displays the new database and the container that you created.
Add data to your database
In Data Explorer, expand the ToDoList database, and expand the Items container. Next, select Items, and then select New Item.
Create a data factory

Launch Microsoft Edge or Google Chrome web browser. Currently, Data Factory UI is supported only in Microsoft Edge and Google Chrome web browsers.
Go to the Azure portal.
From the Azure portal menu, select Create a resource.
Select Integration, and then select Data Factory.
On the Create Data Factory page, under Basics tab, select your Azure Subscription in which you want to create the data factory.
For Resource Group, take one of the following steps:
Select an existing resource group from the drop-down list.
Select Create new, and enter the name of a new resource group.
For Region, select the location for the data factory.
For Name, enter name of the Azure data factory must be globally unique.
For Version, select V2.
Select Next: Git configuration, and then select Configure Git later check box.
Select Review + create, and select Create after the validation is passed. After the creation is complete, select Go to resource to navigate to the Data Factory page.
Select the Author & Monitor tile to start the Azure Data Factory user interface (UI) application on a separate browser tab.
Reference:

https://docs.microsoft.com/en-us/azure/cosmos-db/create-cosmosdb-resources-portal
https://docs.microsoft.com/en-us/azure/data-factory/quickstart-create-data-factory-portal
