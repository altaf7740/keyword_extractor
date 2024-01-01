from bs4 import BeautifulSoup
import yake

def process_html(input_html):
    # Parse the HTML content
    soup = BeautifulSoup(input_html, 'html.parser')

    # Remove all <pre> and <img> tags and their content
    unwanted_tags = ['pre', 'img']
    for unwanted_tag in unwanted_tags:
        for selected_tag in soup.find_all(unwanted_tag):
            selected_tag.decompose()

    # Remove all other HTML tags, keeping only the content
    processed_text = ' '.join(soup.stripped_strings)

    return processed_text

def extract_keywords(text):
    # Specify language and create YAKE extractor
    language = "en"
    max_ngram_size = 5
    deduplication_threshold = 0.9

    extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold)

    # Extract keywords
    keywords = extractor.extract_keywords(text)

    return keywords