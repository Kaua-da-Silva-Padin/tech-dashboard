from google import genai
import os

client = genai.Client(api_key=os.environ.get('GEMINI_KEY'))

def talk_with_gemini(query: str) -> str:
    interaction = client.interactions.create(
        model='gemini-3.6-flash',
        input=query
    )
    return interaction.output_text

if __name__ == '__main__':
    print(res := talk_with_gemini('Top programming languages (only answer with python data and never say stuff like "thank you" or anything besides just the data)'))