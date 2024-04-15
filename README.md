# Gempedia Server

Gempedia Server is a FastAPI application that serves as an API for Wikipedia data. It also integrates with Google's Gemini API to generate advanced summaries of Wikipedia pages.

## Features

- Fetches page details from Wikipedia.
- Uses Google's Gemini API to generate advanced summaries of Wikipedia pages.
- Uses SQLAlchemy for database operations.
- Uses Pydantic for data validation.
- Uses Black for code formatting.
- Uses Loguru and Rich for logging.
- Uses SlowAPI for rate limiting.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/bantoinese83/gempedia_server.git
    ```
2. Change into the project directory:
    ```
    cd gempedia_server
    ```
3. Install the requirements:
    ```
    pip install -r requirements.txt
    ```

## Usage

1. Start the server:
    ```
    uvicorn main:app --reload
    ```
2. Open your browser and visit:
    ```
    http://localhost:8000
    ```
3. Use the `/page/{page_name}` endpoint to get the details of a Wikipedia page. Replace `{page_name}` with the name of the Wikipedia page you want to fetch.
4. The response will include an advanced summary of the Wikipedia page, generated using Google's Gemini API.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
