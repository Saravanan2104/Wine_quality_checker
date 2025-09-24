"""
Started on Fri Sep 19 2025

Frontend: Ajith kumar
Backend: Saravanan
"""


import pickle
from flask import Flask, request




app=Flask(__name__)

pickle_in = open("wine_quality_model.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def predict_index():
    return '<body><h1>Wine Quality a Prediction</h1></body>'


@app.route('/predict',methods=["Post"])
def predict():

    """
    ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
     'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
     'pH', 'sulphates', 'alcohol']
   """
    input_cols=['fixed acidity', 'volatile acidity', 'citric acid', 
                'residual sugar','chlorides', 'free sulfur dioxide', 
                'total sulfur dioxide', 'density',
                'pH', 'sulphates', 'alcohol']
    
    filterd_cols = ['citric acid', 'fixed acidity', 'density', 'total sulfur dioxide',
       'sulphates', 'volatile acidity', 'alcohol']
    
    list1=[]
    for i in input_cols:
        val=request.args.get(i)
        if i in filterd_cols:
            list1.append(eval(val))


    prediction=classifier.predict([list1])
    prediction=round(prediction[0],2)
    status = ""  

    
    if prediction>10:
        prediction=None
        status = "Alcohol must be 0 to 35 only"
    elif prediction<0:
        prediction=None
        status = "Alcohol must be 0 to 35 only"
    else:        
        if 10>=prediction>=7:
            status = "Excellent Quality"
        elif 7>prediction>=4:
            status = "Average Quality"
        else:
            status = "Poor Quality"


    print(prediction)
    return ["Wine Quality is "+str(prediction),status]


if __name__=='__main__':
    app.run(debug=True)

