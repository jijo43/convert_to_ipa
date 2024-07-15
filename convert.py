from flask import Flask, request, jsonify
import epitran

app = Flask(__name__)

# Initialize Epitran for English
epi = epitran.Epitran('eng-Latn')

@app.route('/')
def index():
    text = request.args.get('text', '')
    if text:
        try:
            ipa = epi.transliterate(text)
            return f'IPA: {ipa}'
        except Exception as e:
            return f'Error: {str(e)}'
    else:
        return 'Text parameter not found in request'

if __name__ == '__main__':
    app.run(debug=True)
