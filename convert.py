from flask import Flask, request, jsonify
import epitran

app = Flask(__name__)

# Initialize Epitran for English
epi = epitran.Epitran('eng-Latn')

@app.route('/convert.py', methods=['GET'])
def convert_text_to_ipa():
    text = request.args.get('text', '')
    if text:
        try:
            ipa = epi.transliterate(text)
            response = jsonify({'ipa': ipa})
            response.headers.add('Access-Control-Allow-Origin', '*') # Allow CORS
            return response, 200
        except Exception as e:
            response = jsonify({'error': str(e)})
            response.headers.add('Access-Control-Allow-Origin', '*') # Allow CORS
            return response, 500
    else:
        response = jsonify({'error': 'Text parameter not found in request'})
        response.headers.add('Access-Control-Allow-Origin', '*') # Allow CORS
        return response, 400

if __name__ == '__main__':
    app.run(debug=True)
