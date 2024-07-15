from flask import Flask, request, jsonify, render_template
import epitran

app = Flask(__name__)

# Initialize Epitran for English
epi = epitran.Epitran('eng-Latn')

@app.route('/convert', methods=['GET'])
def convert_text_to_ipa():
    text = request.args.get('text', '')
    if text:
        try:
            ipa = epi.transliterate(text)
            return render_template('ipa_display.html', ipa=ipa)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Text parameter not found in request'}), 400

if __name__ == '__main__':
    app.run(debug=True)
