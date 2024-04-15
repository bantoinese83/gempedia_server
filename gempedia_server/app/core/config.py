from dotenv import load_dotenv

import os

from loguru import logger
from rich.logging import RichHandler
from wikipediaapi import Wikipedia

from app.db.database import engine
from app.models import models

load_dotenv()


def setup_database():
    # Database setup
    models.Base.metadata.create_all(bind=engine)


def setup_logger():
    # Setup logging
    FORMAT = "%(time)s %(level)s %(message)s"
    logger.remove()
    logger.add(RichHandler(rich_tracebacks=True), format=FORMAT)


def setup_wikipedia():
    # Wikipedia API setup
    language = os.getenv('WIKIPEDIA_LANGUAGE', 'en')
    user_agent = os.getenv('WIKIPEDIA_USER_AGENT', 'gempedia-server/0.1.0')
    return Wikipedia(language=language, user_agent=user_agent)


# Call the setup functions
setup_database()
setup_logger()
wiki_wiki = setup_wikipedia()
