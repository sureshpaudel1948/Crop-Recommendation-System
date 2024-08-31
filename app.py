from flask import Flask, request, render_template, redirect, url_for
import numpy as np
import pickle

# importing model
model = pickle.load(open('model.pkl', 'rb'))
sc = pickle.load(open('standscaler.pkl', 'rb'))
ms = pickle.load(open('minmaxscaler.pkl', 'rb'))

# creating flask app
app = Flask(__name__)

# Mapping of crop names to image filenames
CROP_IMAGES = {
    "Rice": 'rice.jpg',
    "Maize": 'maize.jpg',
    "Jute": 'jute.jpg',
    "Cotton": 'cotton.jpg',
    "Coconut": 'coconut.jpg',
    "Papaya": 'papaya.jpg',
    "Orange": 'orange.jpg',
    "Apple": 'apple.jpg',
    "Muskmelon": 'muskmelon.jpg',
    "Watermelon": 'watermelon.jpg',
    "Grapes": 'grapes.jpg',
    "Mango": 'mango.jpg',
    "Banana": 'banana.jpg',
    "Pomegranate": 'pomegranate.jpg',
    "Lentil": 'lentil.jpg',
    "Blackgram": 'blackgram.jpg',
    "Mungbean": 'mungbean.jpg',
    "Mothbeans": 'mothbeans.jpg',
    "Pigeonpeas": 'pigeonpeas.jpg',
    "Kidneybeans": 'kidneybeans.jpg',
    "Chickpea": 'chickpea.jpg',
    "Coffee": 'coffee.jpg'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/predict", methods=['POST'])
def predict():
    N = request.form['Nitrogen']
    P = request.form['Phosporus']
    K = request.form['Potassium']
    temp = request.form['Temperature']
    humidity = request.form['Humidity']
    ph = request.form['Ph']
    rainfall = request.form['Rainfall']

    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)

    scaled_features = ms.transform(single_pred)
    final_features = sc.transform(scaled_features)
    prediction = model.predict(final_features)

    crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

    if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]
        result = "{} is the best crop to be cultivated right there".format(crop)
        crop_image = CROP_IMAGES.get(crop, 'default.jpg')  # Fallback image if crop is not found
    else:
        result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
        crop_image = 'default.jpg'  # Fallback image in case of no recommendation

    return render_template('index.html', result=result, crop_image=crop_image)

if __name__ == '__main__':
    app.run(debug=True)
