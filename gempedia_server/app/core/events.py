from fastapi import FastAPI
from sqlalchemy import Engine

from app.core.logging_config import log_progress, log_tasks
from app.core.logging_config import setup_logger
from app.utils.utils import create_tasks

# Setup logger
logger = setup_logger()


# events.py
def startup_event(app: FastAPI, engine: Engine, event_logger):
    @app.on_event("startup")
    async def startup():
        try:
            tasks = create_tasks(app, engine)  # Get the tasks
            event_logger.info("Application startup")
            for task_name, task_func in tasks:
                event_logger.info(f"Running {task_name}")
                task_func()  # Execute the task function
                event_logger.info(f"Completed {task_name}")
            log_progress("Startup", 100, 100)
            log_tasks(tasks)  # Log the tasks
        except Exception as e:
            logger.error(f"Error occurred during startup: {str(e)}")


# Shutdown event handler
def shutdown_event(app: FastAPI, event_logger):
    @app.on_event("shutdown")
    async def shutdown():
        try:
            event_logger.info("Application shutdown")
            log_progress("Shutdown", 100, 100)
        except Exception as e:
            logger.error(f"Error occurred during shutdown: {str(e)}")
