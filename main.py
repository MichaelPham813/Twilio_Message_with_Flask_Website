from flask import Flask,render_template,flash,redirect,url_for
import twilio_message

app = Flask(__name__)
app.secret_key = "12345"
#Default/page
@app.route('/')
def index():
  return render_template("index.html")

#Same pages but now with the messages via flash
@app.route('/messages/', methods = ['POST'])
def message():
  twilio_message.messaging()
  flash('SMS has been sent successfully!', 'success')
  return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)