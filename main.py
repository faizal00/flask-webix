from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-data', methods=['POST'])
def sendData():
    print(request.form)
    return ''

app.run(port=8080, debug=True)