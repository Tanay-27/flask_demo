#import numpy as np
from flask import Flask, request, render_template, url_for
from instamojo_wrapper import Instamojo

app = Flask(__name__)
#model = pickle.load(open('model.pkl', 'rb'))
API_KEY = 'test_a7fe6937b28c505f371ce8ca286'
AUTH_TOKEN = 'test_a68ddfad2ea46762db39aadd1e3'
api = Instamojo(api_key=API_KEY,
                auth_token=AUTH_TOKEN,
                endpoint='https://test.instamojo.com/api/1.1/')

def createPayment(pur,amt):
    response = api.payment_request_create(
        amount=amt,
        purpose=pur,
        redirect_url= url_for('paymentredirect')
        )
    rep = response['payment_request']['longurl']
    return rep #response['payment_request']['longurl']
@app.route('/')
def home():
    amt = 15
    pur = "Check"
    x = createPayment(amt,pur)
    return render_template('index.html',x)

@app.route('/payments',methods=['POST'])
def paymentredirect():
    '''
    For rendering results on HTML GUI
    '''
    print(request.form['payment_request'])  # should display 'bar'
    return render_template('index.html',text = "Thankyou for Purchasing, your payment is recieved")

if __name__ == "__main__":
    app.run(debug=True)