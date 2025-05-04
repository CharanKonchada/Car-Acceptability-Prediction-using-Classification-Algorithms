# Car Evaluation Prediction Flask App

This Flask application allows users to predict car evaluations based on various features. It uses a pickled machine learning model trained to classify cars as unacceptable, acceptable, good, or very good.

## Features
- User-friendly web interface for entering car attributes
- Real-time display of encoded feature values
- Prediction using your pre-trained model
- Display of prediction results

## Setup Instructions

### Prerequisites
- Python 3.6 or higher
- Flask
- Numpy
- Your trained model pickle file

### Installation Steps

1. **Clone or download this repository**

2. **Create a virtual environment** (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**:
   ```
   pip install flask numpy
   ```

4. **Add your model file**:
   - Place your trained model pickle file in the root directory
   - Name it `model.pkl` or update the `MODEL_PATH` variable in `app.py`

5. **Create the templates directory**:
   ```
   mkdir templates
   ```

6. **Place the index.html file in the templates directory**

### Directory Structure
```
car_evaluation_app/
├── app.py
├── model.pkl  # Your pre-trained model
├── README.md
└── templates/
    └── index.html
```

## Running the Application

1. **Start the Flask server**:
   ```
   python app.py
   ```

2. **Access the web interface**:
   - Open your browser and navigate to `http://127.0.0.1:5000/`

3. **Use the application**:
   - Select values for each car feature
   - See the encoded values update in real-time
   - Click "Predict Car Class" to get the prediction result

## How to Export Your Model from Jupyter/Anaconda

If you haven't exported your model yet, here's how to do it from your Jupyter notebook:

```python
# In your Jupyter notebook
import pickle

# Assuming 'model' is your trained classifier
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

# This will save the model to the current working directory
```

## Notes
- Make sure the encoding scheme in the app matches exactly with how your model was trained
- The application will display a warning if the model file is not found
- For production use, set `debug=False` in app.py
