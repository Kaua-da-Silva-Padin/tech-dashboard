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
    print(res := talk_with_gemini('Most used programming languages, you must include at least 10 (only answer with a python style list) enter these informations inside each item on the list: usage percentage (only numbers and not with a percentage sign), name, main job that uses it and average salary for junior, mid-level and senior developers for people doing said job (never say stuff like "thank you" or anything besides just the data)'))