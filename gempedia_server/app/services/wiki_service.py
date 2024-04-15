# wiki_service.py
from wikipediaapi import Wikipedia

from app.db.database import get_db
from app.core.logging_config import setup_logger, log_table, log_markdown
from app.models.models import Page
from app.services.google_gemini_service import GoogleGeminiService
from app.services.wiki_summary_prompt import generate_summary_prompt


logger = setup_logger()

wiki_wiki = Wikipedia(
    language='en',
    user_agent='gempedia-server/0.1.0 ('
)


def get_page_details(page_name: str):
    try:
        # Get the database session
        db = next(get_db())
        page = wiki_wiki.page(page_name)
        wiki_request = {
            "title": page.title,
            "summary": page.summary,
            "fullurl": page.fullurl,
            "exists": page.exists(),
            "sections": [s.title for s in page.sections],
            "categories": [c.title for c in page.categories.values()],
            "links": [link.title for link in page.links.values()],
            "langlinks": {k: v.title for k, v in page.langlinks.items()}
        }

        # Convert wiki_request to a list of dictionaries
        wiki_request_list = [wiki_request]

        # Log the data using log_table
        log_table(wiki_request_list, title="Page Details", caption="Details of the requested page")

        # Convert wiki_request to a Markdown-formatted string
        markdown_string = "\n".join(f"- **{k}**: {v}" for k, v in wiki_request.items())

        # Log the data using log_markdown
        log_markdown(markdown_string)

        # Create an instance of GoogleGeminiService
        gemini_service = GoogleGeminiService()

        # Generate a review for the Wikipedia page
        review_prompt = generate_summary_prompt(page)
        review = gemini_service.generate_wiki_summary(review_prompt)

        # Add the review to the wiki_request dictionary
        wiki_request["gemini_summary"] = review

        # Get the Page instance with the given page_name from the database
        db_page = db.query(Page).filter(Page.gemini_summary == page_name).first()

        # If it doesn't exist, create a new one
        if db_page is None:
            db_page = Page(gemini_summary=page_name)

        # Set the gemini_summary attribute to the review
        db_page.gemini_summary = review

        # Add the Page instance to the session and commit the changes
        db.add(db_page)
        db.commit()

        return wiki_request
    except Exception as e:
        logger.error(f"Error getting page: {e}")
        return None
