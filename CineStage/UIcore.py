from dotenv import load_dotenv
import streamlit as st
from typing import List, Optional
from pydantic import BaseModel, Field

from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from langchain_core.output_parsers import PydanticOutputParser

# Load environment variables from .env file
load_dotenv()


# ------------------ PYDANTIC MODEL ------------------

class Movie(BaseModel):
    title: str = Field(description="Title of the movie")
    release_year: Optional[int] = Field(default=None, description="Release year of the movie")
    genre: List[str] = Field(default_factory=list, description="List of genres")
    director: Optional[str] = Field(default=None, description="Director of the movie")
    cast: List[str] = Field(default_factory=list, description="List of main cast members")
    rating: Optional[float] = Field(default=None, description="Rating out of 10")
    summary: str = Field(description="Brief summary of the movie")


# ------------------ MODEL & PARSER ------------------

model = ChatMistralAI(model="mistral-small-2506")
parser = PydanticOutputParser(pydantic_object=Movie)


# ------------------ PROMPT ------------------

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Extract movie information from the paragraph below.\n{format_instructions}"
    ),
    (
        "human",
        "{paragraph}"
    )
])

# LangChain Expression Language (LCEL) Chain
chain = prompt | model | parser


# ------------------ STREAMLIT UI ------------------

st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Information Extractor")
st.write("Enter a paragraph containing movie information.")

para = st.text_area(
    "Give Your Paragraph:",
    height=200,
    placeholder="Enter your movie paragraph here..."
)

if st.button("Extract Movie Information", type="primary"):
    if para.strip():
        with st.spinner("Extracting movie information..."):
            try:
                # Runs prompt -> model -> pydantic parser automatically
                extracted_movie = chain.invoke({
                    "paragraph": para,
                    "format_instructions": parser.get_format_instructions()
                })

                st.subheader("Extracted Information")
                # Displays pretty-printed JSON from the parsed Pydantic object
                st.code(extracted_movie.model_dump_json(indent=2), language="json")

            except Exception as e:
                st.error(f"An error occurred during extraction: {e}")
    else:
        st.warning("Please enter a paragraph.")