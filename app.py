from flask import Flask, render_template, request, redirect, flash
import requests
import re

app = Flask(__name__, template_folder='templates_folder')

url =  "https://raw.githubusercontent.com/ByCodersTec/desafio-ruby-on-rails/master/CNAB.txt"
response = requests.get(url)
responselist = re.split('\n', response.text)




@app.route("/")
def index():
  return render_template('index.html', data=responselist[0])

if __name__ == "__main__":
 app.run()