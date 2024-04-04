-- Outining my Approach 

Data Manipulation 

Status_Changes Datasheet
Parse in Python:
    Only dates in PostDate column
    Only dates in Start_Date column

Table_History Datasheet
Parse in Python: 
    Customer type
    Current status
    Last Billed Date
    Last Visit Date
    Only dates in the Post Date Column

SQL:
Create tables, with some columns having NULL variables
Use JOIN statements to group using Customer_ID as PK
Below are starting points I would consider doing:

-- (1) Processing the Status Changes 
CREATE VIEW v_status_changes AS
SELECT
    customer_id,
    CAST(start_date AS DATE) AS start_date,
    status,
    CASE
        WHEN status = 'FREEZE' THEN 'freeze'
        WHEN status = 'TERMINATED' THEN 'cancel' -- This might need refinement based on the `membership_form_of_payment`
    END AS end_reason
FROM
    status_changes;


-- (2) Combine and Finalize the Dataset
SELECT
    h.customer_id,
    h.start_date,
    LEAD(h.start_date, 1) OVER(PARTITION BY h.customer_id ORDER BY h.start_date) AS end_date,
    sc.end_reason
FROM
    v_history h
JOIN
    v_status_changes sc ON h.customer_id = sc.customer_id
WHERE
    h.start_date IS NOT NULL
ORDER BY
    h.customer_id,
    h.start_date;
