# Exercise 2

## Business Process Description

An overview of processes involved when an Invoice of a Membership Purchase has been generated through the 'Approach' enterprise system after a payment has been made in-person.

## Fact Table

| Invoice | Type | Description |
| --- | --- | --- |
| Invoice_ID | Int | The ID of the invoice. |
| Invoice_Date | Varchar | The date the invoice was generated. |
| Staff_ID  | Varchar | The ID of the staff that's associated with the invoice. |
| Acount_ID  | Int | The ID of the account. |
| Location_ID  | Int | The ID of the gym location. |
| Member_ID  | Varchar | The ID of the gym member. |
| Member_FirstName  | Varchar | The first name of the gym member. |
| Member_LastName  | Varchar | The last name of the gym member. |
| Member_Email  | Varchar | The email of the gym member. |
| Confirmation_Number  | Varchar | The confirmation number of the payment. |
| Payment_Status  | Varchar | The status of the payment: paid, in-process, not paid. |
| Sales_Tax  | Decimal | - |
| Total_Amount  | Decimal | - |

## Dimensions

| Gym Member | Type | Description |
| --- | --- | --- |
| Member_ID | Varchar | - |
| Member_Email | Varchar | - |
| Member_FirstName | Varchar | - |
| Member_LastName | Varchar | - |
| Phone_Number | Varchar | - |
| Street_Address | Varchar | - |
| City | Varchar | - |
| State | Varchar | - |
| Zip_Code | Varchar | - | 

| Gym | Type | Description |
| --- | --- | --- |
| Location_ID | Varchar | - |
| Phone_Number | Varchar | -|
| Street_Address | Varchar | - |
| City | Varchar | - |
| State | Varchar| - |
| Zip_Code | Varchar| - | 

| Membership | Type | Description |
| --- | --- | --- |
| Membership_ID | Varchar| - |
| Membership_Type | Varchar| - |
| Start_Date | Varchar | - |
| End_Date | Varchar| - |
| Renewnal_Date | Varchar | - |
| Emergency_Contact | Varchar | - | 
| Signed_Waiver | Varchar | - | 

| Payment Information | Type | Description |
| --- | --- | --- |
| Confirmation_Number | Varchar | - |
| First_Name | Varchar | - |
| Last_name | Varchar | - |
| Credit_Card_Number | Varchar | -|
| Exp_Date | Date | - |

| Staff | Type | Description |
| --- | --- | --- |
| Staff_ID | Varchar | - |
| Staff_First_Name | Varchar | - |
| Staff_Last_name | Varchar | - |
| Staff_Email | Varchar| - |


