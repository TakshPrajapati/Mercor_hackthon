import textbase
from textbase.message import Message
from textbase import models
from langchain.chat_models import ChatOpenAI
from langchain.chains import create_tagging_chain_pydantic
from pydantic import BaseModel, Field, conlist
from typing import Optional, List 
import os
import random
import spacy

# Load the spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Load your OpenAI API key
models.OpenAI.api_key = "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"

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """You are chatting with a College Admission Query Bot. Feel free to ask any questions related to college admissions, courses, application process, requirements, and more. I'm here to help!
"""

# Initialize Langchain and OpenAI models
os.environ["OPENAI_API_KEY"] = "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"
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

# Define the AdmissionQuery class for user queries
class AdmissionQuery(BaseModel):
    query: Optional[str] = Field(
        None,
        description="User's admission-related query.",
    )
tagging_chain = create_tagging_chain_pydantic(AdmissionQuery, llm)

# Function to generate responses for admission queries
def generate_admission_response(query):
    # Process the user's query using spaCy
    doc = nlp(query)

    # Identify key entities and keywords in the query
    entities = [ent.text.lower() for ent in doc.ents]
    keywords = [token.text.lower() for token in doc if not token.is_stop and token.is_alpha]

    response = ""

    if any(course_keyword in keywords for course_keyword in ["course", "program"]):
        response = "Sure! We offer a wide range of courses in various disciplines including..."
        # Provide a list of popular courses or provide a link to the course catalog.

    elif any(keyword in keywords for keyword in ["apply", "application", "process"]):
        response = "The application process includes..."
        # Provide step-by-step information about the application process.

    elif any(keyword in keywords for keyword in ["requirement", "eligibility"]):
        response = "To apply for admission, you need to fulfill the following requirements..."
        # List out the admission requirements such as academic qualifications, test scores, etc.

    elif any(keyword in keywords for keyword in ["scholarship", "financial aid"]):
        response = "We offer scholarships for outstanding students. Some of our scholarship programs include..."
        # Provide information about available scholarships and eligibility criteria.

    else:
        response = "Thank you for your query. Here's some general information:..."
        # Provide a generic response if the query doesn't match specific features.

    return response

def on_message(message_history: List[Message], state: dict = None):
    if state is None or "counter" not in state:
        state = {"counter": 0}
    else:
        state["counter"] += 1

    if len(message_history) > 0:
        user_message = message_history[-1].content.strip()
    else:
        user_message = ""

    # Generate GPT-3.5 Turbo response
    bot_response = models.OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history,
        model="gpt-3.5-turbo",
    )

    # Process user query and generate admission-related response
    if "user" in bot_response.lower():
        # Use the tagging chain to capture the admission query
        admission_query = tagging_chain.extract(user_message)
        if admission_query.query:
            # Generate a response based on the admission query
            admission_response = generate_admission_response(admission_query.query)
            # Concatenate the admission response with the GPT-3.5 Turbo response
            bot_response += f"\n\n{admission_response}"

    return bot_response, state

# Run the textbase chatbot with the on_message function
if __name__ == "__main__":
    textbase.run(on_message)
