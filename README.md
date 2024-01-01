# Flask App for Keyword Extraction

This is a Flask web application that processes HTML content, removes specific HTML tags, and extracts keywords using YAKE (Yet Another Keyword Extractor).

## Prerequisites

Make sure you have Docker installed on your machine.

## Running the App

### Build Docker Image

```bash
docker build -t learn_coding_keyword_extracton .
docker run --name learn_coding_keyword_extracton_container -p 5000:5000 learn_coding_keyword_extracton
```

The Flask app will be accessible at http://127.0.0.1:5000/.

## API Endpoint

- Endpoint: /extract-keyword
- Method: POST
- Request Payload: 
```json
{
  "html_content": "<html><body><p>This is a sample HTML content.</p></body></html>"
  }
```
- Response
```json
{
  "processed_text": "This is a sample HTML content.",
  "keywords": [
    {"keyword": "sample", "score": 1.0},
    {"keyword": "HTML", "score": 0.9},
    {"keyword": "content", "score": 0.8}
    // ... other keywords
  ]
}
```