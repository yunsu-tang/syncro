import os
from openai import OpenAI

def prompt_user():
    # Define the prompt
    company_name = "Aviva"  # Change this as needed
    prompt = f"""
    You are an expert in constructing Boolean search queries for structured news searches, specializing in the insurance industry. Your task is to create a comprehensive query for a specific insurance company.

    Here is the name of the company you'll be focusing on:

    <company_name>
    {company_name}
    </company_name>

    Your goal is to construct a Boolean search query that will effectively capture relevant news and information about this company. The query should incorporate keywords related to the following elements:

    1. The company's name
    2. Leadership team
    3. Regulatory bodies relevant to the insurance industry
    4. Trade associations in the insurance sector
    5. Competitors of the company
    6. Key policy agendas shaping the insurance industry

    Please follow these steps to construct your query, working through the process inside <query_construction_process> tags:

    1. For each element (company name, leadership, regulatory bodies, etc.):
    a. List key terms
    b. Generate synonyms and alternate phrasings
    c. Group terms with Boolean operators

    2. After listing all elements:
    a. Combine the groups into a comprehensive query
    b. Review and refine the query for adherence to guidelines
    c. Present the final query string

    When constructing your query, adhere to these important guidelines:
    • Use Boolean operators (AND, OR, NOT) to optimize relevance and filter out unrelated results.
    • Utilize parentheses to group terms and establish precedence where necessary.
    • Do not use any special characters
    • Ensure the final output is a single Boolean search string.
    • Please do not include any quotation marks in the final string anywhere

    Here are examples of valid query structures:
    • Microsoft Windows 10
    • Apple OR Microsoft
    • Apple AND NOT iPhone
    • (Windows 7) AND (Windows 10)
    • Intel AND (i7 OR i9)
    • (Intel AND (i7 OR i9-13900K)) AND NOT AMD AND NOT i7-13700K

    After your query construction process, present ONLY your final Boolean search query as a single string, ensuring it adheres to the specified format and guidelines. Do not include any explanations or additional text with the final query.

    Begin your query construction process now. ONLY provide the final string.
    """

    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),  # This is the default and can be omitted
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an expert in Boolean search query construction."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1,  # Adjust for creativity (lower = more precise)
        model="gpt-4",
    )

    return chat_completion