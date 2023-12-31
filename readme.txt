The program takes in a query a certain dataset in natural language as user input, turns it into a SQL query, queries the database, analyses the information from the database and returns a response in natural language. To use it, add your OpenAI API key, run the code which will start the Gradio interface, enter your question and press "Run". Alternatively, you can test it here: https://huggingface.co/spaces/Yelaman/Text2SQL

You can ask any questions, such as: "How many active agency customers did we have on January 1st, 2022?", "When did we get the highest number of users per day in Q1 2023?", etc.

The program works with with small datasets and simpler requests. As an improvement, we can use vector search, but considering limited time, this version was implemented.

This program is connected to a Clickhouse database with dummy marketing data. The database consists of 100 rows, and its columns are: date for the date of the performance data, platform to specify the advertising platform, daily_users to track the number of users per day, daily_visits to monitor daily website visits, cpc to store cost per click data, clicks to record the number of clicks, ad_name to store the name of the ads and daily_active_customers to track the agency's daily active customers. It has data for January 2022, January 2023, beginning of February 2023 (till 08.02.2023) and April 2023. If you want to look through the database info, it is saved in the database_info.csv file in this repo.

Libraries used: Langchain for wrapping the processes, SQLAlchemy for interacting with the database, Gradio for a webapp interface.
