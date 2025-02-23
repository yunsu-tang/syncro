from podcastfy.client import generate_podcast
import os

custom_config = {
    "word_count": 25,  # Longer to allow for detailed arguments
    "conversation_style": ["executive summary", "analytical", "high level"],  # Appropriate for academic discourse
    "roles_person1": "Main presenter",  # Presents the main argument
    "roles_person2": "clarifier",  # Challenges the thesis
    "dialogue_structure": [
        "Headline summary","Main Content Summary","Things to look out for in the future"
    ],  # Mimics a structured debate format
    "podcast_name": "Morning Alert",
    "user_instructions": "Mention at the start that the podcast is for James",
    # "engagement_techniques": [
    #     "socratic questioning",
    #     "historical references",
    #     "thought experiments"
    # ],  # Techniques to stimulate critical thinking
    "creativity": 0  # Low creativity to maintain focus on facts and logic
}

def generate_podcast_audio_file_path(urls: list) -> str:
    return generate_podcast(
        urls=urls,
        api_key_label=os.getenv("OPENAI_API_KEY"),
        conversation_config=custom_config
    )  
