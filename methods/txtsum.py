import openai
import os

def generate_podcast_text(message: str) -> str:
    """
    Summarizes input text concisely for executive consumption using ChatGPT API.
    
    :param message: The input text to summarize.
    :return: The filename of the saved summarized text.
    """
    openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure API key is set

    # Call ChatGPT API for summarization
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Summarize the following text concisely for executive consumption."},
            {"role": "user", "content": message}
        ],
        temperature=0.3  # Low temperature for more factual summaries
    )

    summary = response["choices"][0]["message"]["content"]

    # Save the summary to a text file
    filename = "text_doc.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(summary)

    return filename

# Example usage:
# file_name = generate_podcast_text("Your long input text here...")
# print(f"Summary saved in: {file_name}")
