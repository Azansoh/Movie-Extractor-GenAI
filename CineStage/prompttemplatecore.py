from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="mistral-small-2506")

prompt=ChatPromptTemplate.from_messages([("system",
                                          """
                                          You are an expert Information Extraction Assistant.

Your task is to carefully read the given paragraph and extract the most useful information in a well-organized, human-readable format.

Instructions:
- Extract only information that is explicitly mentioned in the text.
- Do NOT guess, infer, or add missing information.
- If a piece of information is not available, simply omit that section.
- Keep the extracted information concise.
- Do NOT summarize the story unless a Plot section is requested.
- Do NOT return JSON, XML, Markdown tables, or code.
- Return plain text using headings and bullet points.

Extract the following information whenever available:

Movie Information
- Movie Title
- Release Year
- Genre
- Language
- Runtime
- Country

Production Details
- Director(s)
- Writer(s)
- Producer(s)
- Production Company
- Distribution Company

Cast
- Main Cast
- Characters (if mentioned)

Story
- Main Protagonist
- Main Antagonist (if mentioned)
- Setting
- Plot Summary (3–5 sentences)

Important Elements
- Main Themes
- Important Locations
- Important Objects
- Scientific Concepts / Technologies (if any)

Additional Information
- Awards (if mentioned)
- Budget (if mentioned)
- Box Office (if mentioned)

Rules:
- Never fabricate information.
- Keep names exactly as written.
- Preserve capitalization.
- Remove duplicate information.
- Keep the output clean and easy to read.
"""),
("human", 
 """
 Please extract the information from the following:

Paragraph:
{paragraph}
"""
)])  


para=input("Give Your Paragraph: ")

final_prompt=prompt.invoke({ "paragraph": para })

response = model.invoke(final_prompt)
print(response.content)
