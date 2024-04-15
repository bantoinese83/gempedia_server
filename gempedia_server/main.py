# main.py
from fastapi import FastAPI

from app.api.routes import router
from app.core.config import setup_database, setup_wikipedia
from app.core.events import shutdown_event, startup_event
from app.core.logging_config import setup_logger
from app.db.database import engine
from app.middlewares.cors import setup_cors
from app.middlewares.exception_handlers import setup_exception_handlers
from app.middlewares.limiter import setup_limiter

app = FastAPI(
    title="Gempedia API", description="API for Wikipedia data", version="0.1.0"
)

# Setup CORS
setup_cors(app)

# Setup exception handlers
setup_exception_handlers(app)

# Setup logging
logger = setup_logger()

# Setup rate limiting
limiter = setup_limiter()


class State:
    pass


app.state = State()
app.state.limiter = limiter

# Include the router
app.include_router(router)

# Call the setup functions
setup_database()
wiki_wiki = setup_wikipedia()

# Setup startup and shutdown events
startup_event(app, engine, logger)  # Pass logger to startup_event
shutdown_event(app, logger)  # Pass logger to shutdown_event
