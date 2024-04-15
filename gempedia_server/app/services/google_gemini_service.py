import os
from typing import Optional, cast
from app.core.logging_config import setup_logger

import google.generativeai as genai
from dotenv import load_dotenv

# Constants
ENV_VAR_NAME = "GOOGLE_API_KEY"
DEFAULT_MODEL = "gemini-1.5-pro-latest"

# Load environment variables
load_dotenv()

# Setup logging
logger = setup_logger()


class GoogleGeminiService:
    def __init__(self) -> None:
        self.api_key: Optional[str] = os.getenv(ENV_VAR_NAME)
        if not self.api_key:
            logger.error(
                f"No API key provided. Please set the {ENV_VAR_NAME} environment variable."
            )
            raise ValueError(
                f"No API key provided. Please set the {ENV_VAR_NAME} environment variable."
            )

        try:
            genai.configure(api_key=self.api_key)
            logger.info("API configured successfully with the provided API key.")
        except Exception as e:
            logger.error(f"Failed to configure the API with provided API key: {e}")
            raise

    @staticmethod
    def generate_wiki_summary(prompt: str, model: str = DEFAULT_MODEL) -> Optional[str]:
        if not model:
            logger.error("No model provided. Please specify a model.")
            return None

        try:
            response = genai.GenerativeModel(model).generate_content(prompt)
            if response and hasattr(response, "text"):
                logger.info(f"Text generated successfully for prompt: {prompt}")
                return cast(str, response.text)
            else:
                logger.warning("The response from the API was empty or malformed.")
                return None
        except Exception as e:
            logger.error(f"Error generating text for prompt: {prompt}. Error: {e}")
            return None
