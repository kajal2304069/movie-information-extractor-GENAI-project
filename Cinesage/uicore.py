from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI
import streamlit as st

load_dotenv()

# ------------------ MODEL ------------------
model = ChatMistralAI(
    model="mistral-small-2506"
)

# ------------------ SCHEMA ------------------
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
Extract movie information from the paragraph.

{format_instructions}
"""
    ),
    ("human", "{paragraph}")
])

# ------------------ UI ------------------
st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Information Extractor")
st.markdown(
    "Paste a movie description and let AI extract structured information."
)

paragraph = st.text_area(
    "📝 Enter Movie Paragraph",
    height=220,
    placeholder="Example: 3 Idiots is a 2009 Indian comedy-drama film directed by Rajkumar Hirani..."
)

if st.button("🚀 Extract Information", use_container_width=True):

    if not paragraph.strip():
        st.warning("⚠️ Please enter a movie paragraph.")
        st.stop()

    with st.spinner("🔍 Extracting movie details..."):

        final_prompt = prompt.invoke(
            {
                "paragraph": paragraph,
                "format_instructions": parser.get_format_instructions()
            }
        )

        response = model.invoke(final_prompt)
        movie_data = parser.parse(response.content)

    st.success("✅ Information Extracted Successfully!")

    st.subheader("🎥 Movie Details")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("🎬 Title", movie_data.title)

    with col2:
        st.metric(
            "📅 Release Year",
            movie_data.release_year if movie_data.release_year else "N/A"
        )

    st.markdown("---")

    st.write("🎭 **Genre**")
    st.write(", ".join(movie_data.genre))

    st.write("🎬 **Director**")
    st.write(movie_data.director or "N/A")

    st.write("⭐ **Rating**")
    st.write(movie_data.rating if movie_data.rating else "N/A")

    st.write("👥 **Cast**")
    for actor in movie_data.cast:
        st.write(f"• {actor}")

    st.write("📖 **Summary**")
    st.info(movie_data.summary)

    with st.expander("📦 View Raw Structured Data"):
        st.json(movie_data.model_dump())