from sunny_app import create_app
from flask import Flask, render_template
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route("/",methods=['GET'])
def home():
  return render_template('home.html')

if __name__ == "__main__":
  app = create_app()
  app.run(debug=True)