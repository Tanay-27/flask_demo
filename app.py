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

response = api.payment_request_create(
	amount=15,
	purpose="app test",
	send_email=True,
	email="tanayshah027@gmail.com",
	redirect_url="https://amvmpayments-api.herokuapp.com/payments"   ,  #url_for('paymentredirect')     #"https://salaryprices-api.herokuapp.com/payments"
	)
    #rep = response['payment_request']['longurl']
    #return 'done' #rep #response['payment_request']['longurl']
#@app.route('/')
#def home():
#    amt = 15
#    pur = "Check"
#    #x = createPayment(amt,pur)
#    return render_template('index.html')

@app.route(r'/payments',methods=['POST'])
def paymentredirect():
    '''
    For rendering results on HTML GUI
    '''
    id = request.args.get('payment_id')
    stat = request.args.get('payemnt_status')
    req = reuest.args.get('payment_reuqest_id')
    print(request.form['payment_request'])  # should display 'bar'
    dict = {
        'text':"Thankyou for purchasing",
        'id': id,
        'status':stat
        'req':req

    }
    return render_template('index.html',dict)

if __name__ == "__main__":
    app.run(debug=True)