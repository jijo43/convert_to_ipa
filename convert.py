from flask import Flask, request, jsonify
import epitran

app = Flask(__name__)

# Initialize Epitran for English
epi = epitran.Epitran('eng-Latn')

@app.route('/convert', methods=['POST'])
def convert_text_to_ipa():
    if 'text' in request.form:
        text = request.form['text']
        try:
            ipa = epi.transliterate(text)
            return jsonify({'ipa': ipa}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Text parameter not found in request'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
