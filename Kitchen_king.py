from flask import Flask , render_template , redirect , url_for

app = Flask (__name__)

@app.route('/')

def home():
    return render_template('index.html')
@app.route('/feedback')
def feedbacksbmit():
    return redirect(url_for('home'))

app.run(debug=True, host='0.0.0.0', port=8080)