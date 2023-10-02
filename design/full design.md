# Drop-Shipping desigh
The goal of this project is to automate drop-shipping with minimal human involvement.

The project should be for all the target sites - our stores, from the resource sites - the site from which we will buy the product
In the first step, AliExpress will be the resource site, and eBay will be the destination site.


>**Assumption:** The site from which we will order the products will not block the user for us due to multiple orders. (because there is no reason for someone to buy dozens of products from the same place and to different addresses each time)

## Full design diagram
[![full design diagram](diagrams\full_design_diagram.png)](https://lucid.app/lucidchart/a9938a4e-10a5-4a33-9fb8-92a6f0274b58/edit?invitationId=inv_6b7e7a84-0118-41cb-a98e-92860c770e7c&page=0_0#)

### Let break it dwon!
The project is made up of several parts:
* Fetch information about products from the source site and saving them
* A periodic process that checks that the saved information is still available (if it's website accessibility, complete if published...)
* Adding the product for the relevant stores
* In the case of a customer purchase, automatic purchase of the product from the source site and sending it to the customer

### Fetch prodact information
[![fetch product information](diagrams/fetch_product_information_diagram.png)](https://lucid.app/lucidspark/ea30920c-7f1d-48b6-bc8c-6c89a1820785/edit?invitationId=inv_37e3cd85-418e-4f84-af44-07fb4fe8cca1&page=0_0#)
The purpose of this component is to fetch information about a product that we would like to sell from the source site

When you want to add a new product for sale, the user will make a request through GUI to import information about the product using the url where the product is located  
The request will be sent to a scripts server where the url will be decoded to know from which site the product was taken  
And trigger a script depending on the site (script for each site), will decode the information in it and return the information to the server which it will send to the user  
The user will see the information about the product, verify with the site that the information is extracted correctly, and add the product to the DB

### Periodic information verification
[![periodic information verification](diagrams/periodic_information_verification.png)](https://lucid.app/lucidspark/ea30920c-7f1d-48b6-bc8c-6c89a1820785/edit?invitationId=inv_37e3cd85-418e-4f84-af44-07fb4fe8cca1&page=0_0#)
The purpose of this component is to check that the source site is still available, to check inventory if the source site publishes this information.
If there is no access to the site or if there is no stock


A periodic process pulls all products from the DB
For each product, the process will do the following:
fetch product information using the url that save in the DB
The request will be sent to a scripts server where the url will be decoded to know from which site the product was taken  
And trigger a script depending on the site (script for each site), will decode the information in it and return the information to the server which it will send to periodic process.  
A comparison will be made between the information from the DB and the information we received from the website
If the information is different, an appropriate action will be taken according to the change and a message will be sent to the manager

### Add prodacr to stores


[![add prodact to stores](diagrams/add_product_to_stores_diagram.png)](https://lucid.app/lucidspark/ea30920c-7f1d-48b6-bc8c-6c89a1820785/edit?invitationId=inv_37e3cd85-418e-4f84-af44-07fb4fe8cca1&page=0_0#)
When a new product enters the DB, a process that adds the new product to all stores will be triggered
When a new product enters the DB, a process that adds the new product to all ^[relevant] stores will be triggered
Each store has a process that adds products to it.
>**Assumption:** Adding a product to different stores from the same site you can use the same process but you will need different parameters to access the store

^[relevant]: Not all stores will advertise all products. From maximum profit limits for the store, creating a concept for the store (garden, furniture...) etc.

### Prodact purchase
[![prodact purchase](diagrams\product_purchase_diagram.png
)](https://lucid.app/lucidspark/ea30920c-7f1d-48b6-bc8c-6c89a1820785/edit?invitationId=inv_37e3cd85-418e-4f84-af44-07fb4fe8cca1&page=0_0#)
The following process is designed to make a purchase for the customer

When a customer makes a purchase, behind the scenes they access a url that accesses the scripts server  
The scripts server trigger a script according to the drop shipping from which the product is made  
The script accesses the website and makes a purchase for the customer

## Milestons
[![milestone 1](diagrams\milestone_1_diagram.png
)](https://lucid.app/lucidspark/ea30920c-7f1d-48b6-bc8c-6c89a1820785/edit?invitationId=inv_37e3cd85-418e-4f84-af44-07fb4fe8cca1&page=0_0#)
In the first phase we will support one source site - Aliexpress and one product in one store on one destination site - Ebay.  
The purchase of the orders will be done manually