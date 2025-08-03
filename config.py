import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Choose LLM: 'grok', 'gemini', or 'openai'
LLM_TYPE = os.getenv("LLM_TYPE", "gemini")

def get_llm():
    if LLM_TYPE == "grok":
        # Placeholder for Grok integration (not publicly available as a package)
        # Replace with actual xAI API integration if available
        raise NotImplementedError(
            "Grok LLM is not supported in this setup. "
            "Use xAI API[](https://x.ai/api) or choose 'gemini'/'openai'."
        )
    elif LLM_TYPE == "gemini":
        # Gemini model setup using LangChain's integration
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set.")
        return ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",  # Use a valid Gemini model name
            google_api_key=api_key,
            temperature=0.7
        )
    else:
        # OpenAI model setup
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set.")
        return ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.7,
            openai_api_key=api_key
        )