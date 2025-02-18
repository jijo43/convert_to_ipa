from flask import Flask, request, jsonify
import epitran

app = Flask(__name__)

# Initialize Epitran for English
epi = epitran.Epitran('eng-Latn')

@app.route('/')
def index():
    text = request.args.get('text', '')
    try:
        ipa = epi.transliterate(text)
        return jsonify({'ipa': ipa}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
