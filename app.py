# importing the required libraries

# request is used to call the request method to display data at front end, 
# render template library is used to show the front end index.html template 
from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

# loading the model we saved, this line deserialized the data using read byte (rb) option
model = pickle.load(open('model.pkl', 'rb'))

# flask application
app = Flask(__name__)

# this line re routes and load the index.html template on the web
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
# make the prediction based on the data we get from the front end
def predict():
    
    # getting all the features given by the user on frontend form
    features = request.form['feature']
    
    # splitting the features
    features = features.split(',')

    #converting the features to a numpy array
    np_features = np.asarray(features, dtype=np.float32)

    # Doing the prediction of the model
    pred = model.predict(np_features.reshape(1, -1))
    
    # display the message using list compreshension
    message = ['Cancerous' if pred[0] == 1 else 'Not Cancerous']
    
    # print(message[0])
    return render_template('index.html', message=message)

# python main functiokn
if __name__ == '__main__':
    app.run(debug=True)

