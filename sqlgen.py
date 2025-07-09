# app/sqlgen.py

import openai
import os

openai.api_key = os.getenv(\"OPENAI_API_KEY\")

def generate_sql_query(nl_prompt, table_schema=\"users(id, name, age, email)\"):
    system_prompt = (
        \"You are an expert SQL developer. Generate a safe, read-only SQL SELECT query. \" 
        \"Only generate the query, no explanation. Table schema: \" + table_schema
    )
    
    response = openai.ChatCompletion.create(
        model=\"gpt-4o\",
        messages=[
            {\"role\": \"system\", \"content\": system_prompt},
            {\"role\": \"user\", \"content\": nl_prompt}
        ]
    )
    sql_query = response.choices[0].message.content.strip()
    return sql_query

if __name__ == \"__main__\":
    sql = generate_sql_query(\"Show me all users older than 30.\")
    print(\"Generated SQL:\\n\", sql)
