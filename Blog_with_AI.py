import openai
import os
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

# ✅ Get API key
openai.api_key = os.getenv("API_KEY")  # Works even if the .env file is missing quotes

def generate_blog(paragraph_topic):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful writing assistant."},
            {"role": "user", "content": f"Write a paragraph about the following topic: {paragraph_topic}"}
        ],
        temperature=0.3,
        max_tokens=400
    )
    return response.choices[0].message.content.strip()

# CLI loop
keep_writing = True

while keep_writing:
    answer = input("Write a paragraph? Y for yes, anything else for no. ")
    if answer.upper() == 'Y':
        paragraph_topic = input("What should this paragraph talk about? ")
        print("\n📝 Blog Paragraph:\n")
        print(generate_blog(paragraph_topic))
        print("\n" + "-" * 60 + "\n")
    else:
        keep_writing = False
        print("Thanks for using the blog generator!")