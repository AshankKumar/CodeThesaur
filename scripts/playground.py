from metaphor_python import Metaphor
from dotenv import load_dotenv
import os
import openai

load_dotenv()

metaphor = Metaphor(os.getenv('METAPHOR_API_KEY'))
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_query_from_gpt(user_query):
    openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_query},
        ]
    )

def get_metaphor_results(query):    
    search_response = metaphor.search(
    query,
    include_domains=["github.com"],
    )

    contents_response = search_response.get_contents()
    # Print content for each result
    for content in contents_response.contents:
        print(f"Title: {content.title}\nURL: {content.url}\nContent:\n{content.extract}\n")

def extract_details(metaphor_response):
    return

if __name__ == "__main__":
    while True:
        user_query = input()
        gpt_query = get_query_from_gpt(user_query)
        get_metaphor_results(gpt_query)
