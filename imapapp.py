from flask import Flask, render_template, request, render_template_string
import requests
from imap_tools import MailBox, A
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/my-link', methods=['POST', 'GET'])
def my_link():
    if request.method =='POST':
        email_name = request.form['email']
        email_password = request.form['passwort']
        email_url = request.form['provider']
        datum = request.form['date']
        date_format = datetime.datetime.strptime(datum, "%Y-%m-%d").date()  #richtiges Format für mailbox.fetch date_get

        with MailBox(email_url).login(email_name, email_password) as mailbox:
            for msg in mailbox.fetch(A(date_gte=date_format)):
                Datum = msg.date
                Subject = msg.subject
                Text = (msg.text)
                return render_template('index.html', Datum=Datum, Subject=Subject, Text=Text)

if __name__ == "__main__":
    app.run(debug=True)