
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle
import os
#import logging as lg
from wsgiref import simple_server 
import json

app = Flask(__name__) # initializing a flask app
#lg.basicConfig(filename='LogFile.log',level= lg.INFO,format='%(asctime)s %(message)s')

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    #lg.info("User form rendered")
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def predict():
    if request.method == 'POST':
        try:
            #lg.info("Got user input")
            gender=1 if request.form['Gender']=='male' else 0
            age=int(request.form['age'])
            PI=1 if request.form['PI']=='Yes' else 0
            #x = 2 if i > 100 else 1 if i < 100 else 0 -- elif condition in single line
            VA = 2 if (request.form['VA'])=='less_than_2_years' else 1 if (request.form['VA']=='less_than_1_year') else 0
            IVD=1 if request.form['IVD']=='Yes' else 0
            AP=float(request.form['AP'])
            Vin=int(request.form['Vin'])
            #lg.info("user inputs are gender %d , age %d , PReviously insuranced or not %d , vehicle age %d , is vehicle damage ? %d , annual premium %d , Vintage %d",gender,age,PI,VA,IVD,AP,Vin)
            #lg.info("sending user input into model")
            algo = 1 if request.form['algo']=='logistic' else 0
            if(algo==1):
                filename='logistic.pkl'
                #lg.info('choosen algorithm is logistic regression')
                #loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
                #prediction=loaded_model.predict([[gender,age,PI,VA,IVD,AP,Vin]])
            else:
                filename = 'DT_model.pkl'
                #lg.info('choosen algorithm is decision tree')
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            prediction=loaded_model.predict([[gender,age,PI,VA,IVD,AP,Vin]])
            if (prediction==0):
                #lg.info("Person is not interested in Vehicle insurance")
                return render_template('results.html',prediction='Person will not be interested in Vehicle insurance')
            else:
                #lg.info("Person is interested in Vehicle insurance")
                return render_template('results.html',prediction='Person will be interested in Vehicle insurance')
        except Exception as e:
            #lg.info("Something went wrong inside")
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='http://localhost', port=8001, debug=True)
	app.run(debug=True) # running the app

'''
port = int(os.getenv("PORT", 5000))
if __name__ == "__main__":
    host = '0.0.0.0'
    # port = 5000
    httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()
'''