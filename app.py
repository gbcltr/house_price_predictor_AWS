from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))
scaler = pickle.load(open('scaler.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_placement():
    bedrooms =int(request.form.get('bedrooms'))
    bathrooms = int(request.form.get('bathrooms'))
    sqrt_living = float(request.form.get('sqrt_living'))
    floors = int(request.form.get('floors'))
    waterfront=int(request.form.get('waterfront'))
    view_score = int(request.form.get('view_score'))
    sqrt_above = float(request.form.get('sqrt_above'))
    sqrt_base = float(request.form.get('sqrt_base'))
    # city = int(request.form.get('city'))
    year_built_cat = int(request.form.get('year_built_cat'))





    # prediction
    result = model.predict(scaler.fit_transform(np.array([bedrooms,bathrooms,sqrt_living,floors,waterfront,view_score,sqrt_above,sqrt_base]).reshape(1,8)))
    # result = model.predict(np.array([bedrooms,bathrooms,sqrt_living,floors,waterfront,view_score,sqrt_above,sqrt_base]).reshape(1,8))

    # if result[0] == 1:
    #     result = 'placed'
    # else:
    #     result = 'not placed'

    return render_template('index.html',result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)