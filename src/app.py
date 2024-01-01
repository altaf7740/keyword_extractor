from flask import Flask, request, jsonify
from commons import *

app = Flask(__name__)

@app.route('/extract-keyword/', methods=['POST'])
def process_html_and_extract_keywords():
    data = request.get_json()
    if 'html_content' not in data:
        return jsonify({'error': 'Missing "html_content" parameter'}), 400
    html_content = data['html_content']
    processed_text = process_html(html_content)
    keywords = extract_keywords(processed_text)
    response = {
        'keywords': [{'keyword': keyword, 'score': score} for keyword, score in keywords]
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False, port=5000)
