from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List,Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()
from langchain_mistralai import ChatMistralAI


model = ChatMistralAI(model = 'mistral-small-2506')


# for schema
class Movie(BaseModel):
    title: str 
    release_year : Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str


# for check data is filled correct or not
parser = PydanticOutputParser(pydantic_object=Movie)

# create systemmanage and humanmanage define
prompt = ChatPromptTemplate.from_messages([
    ('system',"""
Extract movie information from the paragraph
     {format_instructions}
"""),
("human","{paragraph}")
]
)



para = input("Give your paragraph : ")

final_prompt = prompt.invoke(
    {"paragraph" : para,
     'format_instructions': parser.get_format_instructions()
     }
)

response = model.invoke(final_prompt)
movie_data = parser.parse(response.content)

print(movie_data)