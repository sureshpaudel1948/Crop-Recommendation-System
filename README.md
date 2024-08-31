Crop Recommendation System
.Table of Contents
.Project Overview
.Features
.Project Structure
.Installation
.Usage
.Technologies Used
.Contributors
.License

Project Overview:
The Crop Recommendation System is a machine learning-based web application designed to help farmers and agriculturists choose the best crops to grow based on various environmental factors. Users input data such as nitrogen, phosphorus, potassium levels, temperature, humidity, pH, and rainfall, and the system recommends the most suitable crop for cultivation.

Features:
Dynamic Crop Recommendation: Uses machine learning to suggest the best crop based on environmental conditions.
User-Friendly Interface: Simple form-based input for easy data entry.
Responsive Design: The application is accessible and functional on various devices.
Visual Representation: Displays recommended crops with relevant images.
Interactive Navbar: Easy navigation across the application with a custom favicon logo.

Project Structure:

Crop-Recommendation-System/
│
├── static/
│   ├── images/
│   │   ├── CR-LOGO.png
│   │   ├── waterfall.jpg
│   │   └── field.jpg
│   ├── css/
│   │   └── style.css
│
├── templates/
│   ├── index.html
│   └── contact.html
│
├── app.py
├── Crop Classification With Recommendation System.ipynb
├── Crop_recommendation.csv
├── minmaxscaler.pkl
├── model.pkl
├── standscaler.pkl
└── README.md
Key Files and Directories:
app.py: The main Python file that runs the Flask application.
static/: Contains static assets such as images and CSS files.
templates/: Contains HTML template files for the web pages.
Crop Classification With Recommendation System.ipynb: Jupyter notebook with the machine learning model and data processing.
model.pkl: The serialized machine learning model used for prediction.
Crop_recommendation.csv: Dataset used for training the model.

Installation:
Prerequisites
Python 3.x
Flask
Jupyter Notebook (optional, for viewing the notebook)
Steps
Clone the repository:
git clone https://github.com/your-username/crop-recommendation-system.git
cd crop-recommendation-system
Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install required dependencies:

pip install -r requirements.txt
Run the Flask application:

python app.py
Open the application in your browser:

http://127.0.0.1:5000/

Usage:
Open the application in your web browser.
Enter the required environmental data (e.g., Nitrogen, Phosphorus, etc.).
Click "Get Recommendation" to see the recommended crop for your input conditions.

Technologies Used:
Python
Flask: Web framework for building the application.
HTML/CSS/Bootstrap: For front-end design and layout.
Pandas & Scikit-Learn: For data processing and machine learning.

Contributors:
Anupam Paudel: Focused on coding, dataset assembly, and crop research.
Aashish Dhakal: Prepared datasets and conducted research.
Roshan Gautam: Worked on design, layout, and crop recommendations based on climatic conditions.

License:
This project is licensed under the MIT License - see the LICENSE file for details.
