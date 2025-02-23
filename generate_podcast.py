# generate_podcast.py
from methods.prompt import prompt_user
from methods.gnews import gnews_search
from methods.podcastfy import generate_podcast_audio_file_path
def generate_podcast(message: str):
    """
    This function will generate the podcast based on the provided name and email.
    This is just a placeholder for now, you can replace it with your podcast generation logic.
    """
    # print(f"Generating podcast for {name} with email {email}...")
    # Add the logic for podcast generation here
    chat_completion = prompt_user()
    # query = chat_completion.choices[0].to_dict()['message']['content'].split("\n\n</query_construction_process>\n\n")[1]
    query = chat_completion.choices[0].to_dict()['message']['content'].split("\n\nFinal Boolean search query string:\n\n")[1]
    
    articles = gnews_search(query)  

    urls = []
    for article in articles:
        if "reuters" in article['url']:
            continue
        else:
            urls.append(article['url'])
        if len(urls)>0:
            break
    
    podcast_path = generate_podcast_audio_file_path(urls)
    # Return the podcast and text document file names as placeholders
    return podcast_path[0], podcast_path[1]
