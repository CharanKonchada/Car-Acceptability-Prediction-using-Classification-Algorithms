from flask import Flask, render_template, request, jsonify
import pickle
import os
import numpy as np

app = Flask(__name__)

# Load model from pickle file
# Note: You'll need to replace this path with your actual model file
# Get absolute path to model file
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")

# Load the model safely
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Feature encoding dictionaries based on legend
FEATURE_ENCODING = {
    'buying': {'low': 0, 'med': 1, 'high': 2, 'vhigh': 3},
    'maint': {'low': 0, 'med': 1, 'high': 2, 'vhigh': 3},
    'doors': {'2': 0, '3': 1, '4': 2, '5more': 3},
    'persons': {'2': 0, '4': 1, 'more': 2},
    'lug_boot': {'small': 0, 'med': 1, 'big': 2},
    'safety': {'low': 0, 'med': 1, 'high': 2}
}

# Reverse encoding for class (for displaying results)
CLASS_DECODING = {0: 'unacceptable', 1: 'acceptable', 2: 'good', 3: 'very good'}

@app.route('/')
def index():
    return render_template('index.html', feature_encoding=FEATURE_ENCODING)

@app.route('/model-info')
def model_info():
    """Debug route to get information about the loaded model"""
    if model is None:
        return jsonify({'error': 'Model not loaded'})
    
    try:
        model_type = str(type(model).__name__)
        
        # Get additional info based on model type
        model_info = {
            'type': model_type,
            'is_classifier': hasattr(model, 'classes_'),
        }
        
        # Try to get common attributes
        if hasattr(model, 'feature_names_in_'):
            model_info['feature_names'] = model.feature_names_in_.tolist()
        
        if hasattr(model, 'n_features_in_'):
            model_info['n_features'] = model.n_features_in_
            
        if hasattr(model, 'classes_'):
            model_info['classes'] = model.classes_.tolist()
            
        return jsonify(model_info)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded. Please ensure model.pkl is in the application directory.'})
    
    try:
        # Get values from form
        buying = request.form.get('buying')
        maint = request.form.get('maint')
        doors = request.form.get('doors')
        persons = request.form.get('persons')
        lug_boot = request.form.get('lug_boot')
        safety = request.form.get('safety')
        
        # Encode values using the encoding legend
        encoded_values = [
            FEATURE_ENCODING['buying'][buying],
            FEATURE_ENCODING['maint'][maint],
            FEATURE_ENCODING['doors'][doors],
            FEATURE_ENCODING['persons'][persons],
            FEATURE_ENCODING['lug_boot'][lug_boot],
            FEATURE_ENCODING['safety'][safety]
        ]
        
        # Convert to numpy array and reshape properly for the model
        X = np.array(encoded_values).reshape(1, -1)
        
        # Make prediction - handle both classifier and other model types
        try:
            # Try predict method (for classifiers)
            prediction = model.predict(X)[0]
        except:
            # If not a classifier, might be a different type of model
            prediction = int(round(model.predict(X)[0]))
        
        # Map the prediction to class
        if prediction in CLASS_DECODING:
            predicted_class = CLASS_DECODING[prediction]
        else:
            predicted_class = f"Unknown Class ({prediction})"
        
        # Return the prediction and encoded values
        return jsonify({
            'prediction': predicted_class,
            'encoded_values': encoded_values,
            'prediction_raw': int(prediction),
            'success': True
        })
    
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"Prediction error: {error_details}")
        return jsonify({'error': str(e), 'details': error_details, 'success': False})

if __name__ == '__main__':
    app.run(debug=True)