# Exercise 2

## Business Process Description

An overview of processes involved when an Invoice of a Membership Purchase has been made through the 'Approach' enterprise system.

## Fact Table

| Invoice | Type | Description |
| --- | --- | --- |
| Invoice_ID | Int Primary Key | - |
| Invoice_Date | Varchar (20) | - |
| Staff_ID  | Varchar (20) | Foreign Key |
| Membership_ID  | Int | Foreign Key |
| Location_ID  | Varchar (20) | Foreign Key |
| Member_ID  | Varchar (20) | Foreign Key |
| Member_FirstName  | Varchar (50) | Foreign Key |
| Member_LastName  | Varchar (50) | Foreign Key |
| Member_Email  | Varchar (100) | Foreign Key |
| Confirmation_Number  | Varchar (50) | Foreign Key |
| Payment_Status  | Varchar (20) | - |
| Sales_Tax  | Decimal(10, 2) | - |
| Total_Amount  | Decimal(10, 2) | - |

## Dimensions

| Gym Member | Type | Description |
| --- | --- | --- |
| Member_ID | Varchar (20) Primary Key | some text here |
| Member_Email | Varchar (100) | some text here |
| Member_FirstName | Varchar (50) | some text here |
| Member_LastName | Varchar (50) | some text here |
| Phone_Number | Varchar (20) | some text here |
| Street_Address | Varchar (100) | some text here |
| City | Varchar (50) | some text here |
| State | Varchar (20) | some text here |
| Zip_Code | Varchar (10) | some text here | 

| Gym | Type | Description |
| --- | --- | --- |
| Location_ID | Varchar (20) Primary Key | some text here |
| Phone_Number | Varchar (20) | some text here |
| Street_Address | Varchar (100) | some text here |
| City | Varchar (50) | some text here |
| State | Varchar (20) | some text here |
| Zip_Code | Varchar (10) | some text here | 

| Membership | Type | Description |
| --- | --- | --- |
| Membership_ID | Varchar (20) Primary Key | some text here |
| Membership_Type | Varchar (20) | some text here |
| Start_Date | Varchar (100) | some text here |
| End_Date | Varchar (50) | some text here |
| Renewnal_Date | Varchar (20) | some text here |
| Emergency_Contact | Varchar (50) | some text here | 
| Signed_Waiver | Varchar (10) | some text here | 

| Payment Information | Type | Description |
| --- | --- | --- |
| Confirmation_Number | Varchar (20) Primary Key | some text here |
| First_Name | Varchar (20) | some text here |
| Last_name | Varchar (100) | some text here |
| Credit_Card_Number | Varchar (50) | some text here |
| Exp_Date | Varchar (20) | some text here |

| Staff | Type | Description |
| --- | --- | --- |
| Confirmation_ID | Varchar (20) Primary Key | some text here |
| Staff_First_Name | Varchar (20) | some text here |
| Staff_Last_name | Varchar (100) | some text here |
| Staff_Email | Varchar (50) | some text here |


