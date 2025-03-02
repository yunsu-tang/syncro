import openai
import os

def generate_podcast_text(message: str) -> str:
    """
    Summarizes input text concisely for executive consumption using OpenAI's latest API.

    :param message: The input text to summarize.
    :return: The filename of the saved summarized text.
    """
    key = os.getenv("OPENAI_API_KEY")
    client = openai.OpenAI(api_key=key)  # Initialize OpenAI client

    # Call OpenAI API for summarization
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Summarize the following text concisely for executive consumption."},
            {"role": "user", "content": message}
        ],
        temperature=0.3  # Low temperature for more factual summaries
    )

    summary = response.choices[0].message.content

    # # Save the summary to a text file
    filename = "./data/summaries/text_doc.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(summary)

    return filename
