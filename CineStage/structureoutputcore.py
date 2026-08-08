from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="mistral-small-2506")
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser


class Movie(BaseModel):
    title: str
    release_year: Optional[int] = None
    genre: List[str] 
    director: Optional[str]
    cast: List[str]
    rating: Optional[float] = None
    summary: str



parser = PydanticOutputParser(pydantic_object=Movie)

prompt=ChatPromptTemplate.from_messages([("system",
                                          """
                                          Extract movie information from the paragraph
                                          {format_instructions}
"""),
("human", 
 """
{paragraph}
"""
)])  


para=input("Give Your Paragraph: ")

final_prompt=prompt.invoke({ "paragraph": para ,
                            "format_instructions": parser.get_format_instructions()
                            })

response = model.invoke(final_prompt)
print(response.content)
