This program is connected to a Clickhouse database with dummy marketing data. The database consists of 100 rows, and its columns are: date for the date of the performance data, platform to specify the advertising platform, daily_users to track the number of users per day, daily_visits to monitor daily website visits, cpc to store cost per click data, clicks to record the number of clicks, ad_name to store the name of the ads and daily_active_customers to track the agency's daily active customers. It has data for January 2022, January 2023, beginning of February 2023 (till 08.02.2023) and April 2023. 

The program takes in a query on the data in natural language as user input, turns it into a SQL query, queries the database, analyses the information from the database and returns a response in natural language.

Libraries used: langchain for wrapping the processes, sqlalchemy for interacting with the database, gradio for a webapp interface.
