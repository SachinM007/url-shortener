# URL Shortener API

This is a URL shortener API built using **FastAPI**. It allows users to shorten URLs and later retrieve the original URLs by their corresponding shortened identifiers. This project demonstrates how to build a REST API with FastAPI, along with the integration of unit tests, code coverage, and mutation testing.

## Features

- Shorten URLs and return a shortened URL.
- Redirect from a shortened URL to the original URL.
- In-memory database to store the URL mappings.

## Tools and Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **Uvicorn**: ASGI server for serving FastAPI applications.
- **Pytest**: A framework for writing and running tests.
- **Coverage.py**: A tool for measuring code coverage.
- **Mutmut**: A mutation testing tool to evaluate the robustness of tests.
- **Python 3.11**: Programming language.

## Prerequisites

- Python 3.11 or higher
- Virtual environment (recommended)

## Setup Instructions

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/url-shortener.git
cd url-shortener
```

It’s recommended to use a virtual environment to manage dependencies:

```bash
python -m venv env
```

Activate the virtual environment:

- On Windows:
  ```bash
  .\env\Scripts\activate
  ```

- On macOS/Linux:
  ```bash
  source env/bin/activate
  ```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

To start the FastAPI application, run the following command:

```bash
uvicorn app.main:app --reload
```

This will start the server on `http://127.0.0.1:8000`. You can open this URL in your browser to see the API in action.

To run the unit tests for the project, use the following command:

```bash
pytest
```

This will run all the tests in the `tests` directory and provide feedback on the functionality of the API.

To generate a code coverage report, use the following command:

```bash
pytest --cov=app --cov-report=html
```

This will generate a detailed coverage report in the `htmlcov` directory, which you can open in your browser.

To check the effectiveness of the tests, you can run mutation testing with Mutmut:

```bash
mutmut run
mutmut summary
```

This will run mutations on the code and summarize the results. A high mutation score indicates strong test coverage.

## Endpoints

### `POST /shorten/`

Shortens a given URL.

#### Request:

- `original_url` (string): The original URL to be shortened. Should start with `http`.

#### Response:

- `short_url` (string): The shortened URL in the format `http://short.ly/{short_id}`.

#### Example:

**Request:**

```json
{
  "original_url": "http://example.com"
}
```

**Response:**

```json
{
  "short_url": "http://short.ly/abc123"
}
```

### `GET /{short_id}`

Redirects to the original URL based on the shortened URL's identifier.

#### Request:

- `short_id` (string): The shortened URL's unique identifier.

#### Response:

- `original_url` (string): The original URL associated with the shortened URL.

#### Example:

**Request:**

```bash
GET /abc123
```

**Response:**

```json
{
  "original_url": "http://example.com"
}
```

## Testing

### Unit Tests

The unit tests for this project are located in the `tests` directory. The tests validate the following:

- Shortening a URL and ensuring the correct short URL is returned.
- Redirecting a short URL to the original URL.

### Test Coverage

Code coverage is measured using **Coverage.py**, which is integrated into the testing process. The coverage report is available in the `htmlcov` directory.

### Mutation Testing

The project uses **Mutmut** to perform mutation testing, which helps assess the robustness of the unit tests by introducing changes to the code and checking whether the tests fail as expected.

## Contribution

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Ensure that you write tests for new features or bug fixes and maintain good code coverage.

## License

This project is licensed under the MIT License.
```

You can copy and paste the entire content as one single block. Let me know if you need any adjustments!
