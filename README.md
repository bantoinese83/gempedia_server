# Gempedia Server

Gempedia Server is a robust FastAPI application designed to serve as a comprehensive API for Wikipedia data. It leverages the power of Google's Gemini API to generate advanced summaries of Wikipedia pages, providing a rich and detailed overview of the content.

## Key Features

- **Wikipedia Data Fetching**: Seamlessly fetches detailed information from Wikipedia pages.
- **Advanced Summaries**: Utilizes Google's Gemini API to generate in-depth summaries of Wikipedia pages.
- **Database Operations**: Employs SQLAlchemy for efficient and reliable database operations.
- **Data Validation**: Incorporates Pydantic for robust data validation.
- **Code Formatting**: Adopts Black for consistent and readable code formatting.
- **Logging**: Implements Loguru and Rich for comprehensive and visually appealing logging.
- **Rate Limiting**: Integrates SlowAPI for effective rate limiting to prevent abuse.

## Installation Guide

Follow the steps below to get Gempedia Server up and running:

1. **Clone the Repository**
    ```bash
    git clone https://github.com/bantoinese83/gempedia_server.git
    ```
2. **Navigate to the Project Directory**
    ```bash
    cd gempedia_server
    ```
3. **Install the Required Packages**
    ```bash
    pip install -r requirements.txt
    ```
4. **Set Up Environment Variables**
    Create a `.env` file in the project directory and add the following environment variables:
    ```dotenv
    GEMINI_API_KEY=YOUR_GEMINI_API_KEY
    SQLALCHEMY_DATABASE_URL=postgresql://DATABASE_USERNAME:DATABASE_PASSWORD@localhost/DATABASE_NAME
    ```
    Replace `YOUR_GEMINI_API_KEY` with your Google Gemini API key and `DATABASE_USERNAME`,
   `DATABASE_PASSWORD`, and `DATABASE_NAME` with your database credentials.

## Database Setup

1. **Create a PostgreSQL Database**
    ```bash
    createdb DATABASE_NAME
    ```
2. **Run Migration Script**
    Execute the `migrate.py` script to create the necessary database tables:
    ```bash
    python migrate.py
    ```
3. **Run Migrations**
    Execute the `migrations.py` script to apply database migrations:
    ```bash
    python migrations.py
    ```

## Usage Instructions

1. **Start the Server**
    ```bash
    uvicorn main:app --reload
    ```
2. **Access the Application**
    Open your web browser and navigate to:
    ```
    http://localhost:8000
    ```
3. **Fetch Wikipedia Page Details**
    Use the `/page/{page_name}` endpoint to fetch the details of a Wikipedia page. Replace `{page_name}` with the name of the Wikipedia page you want to fetch. The response will include an advanced summary of the Wikipedia page, generated using Google's Gemini API.

## Contributing

We welcome contributions from the community. If you wish to propose major changes, please open an issue first to discuss your ideas.

## License

