
from flask import Flask , render_template , redirect , url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SECRET_KEY'] = 'ALSKJFDAASDFSADFLSDKFASDF'

db = SQLAlchemy(app)

class form_inputs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=True)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/templates')
def learn_more():
    return render_template('generic.html')

@app.route('/authorities')
def auth():
    return render_template('gallery.html')

@app.route('/elements')
def elements():
    return render_template('elements.html')

@app.route('/feedback', methods=['GET', 'POST'])
def submit_feedback():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        db.session.add(form_inputs(full_name=name, email=email, message=message)) # entry added into db
        db.session.commit() # entry commited into db

    data = form_inputs.query.all() # SELECT * from form_inputs

    return render_template('feedback.html', data=data)

app.run(debug=True, host='0.0.0.0', port=8080)