from flask import Flask, render_template, request
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import os

app = Flask(__name__)

# Load your pre-trained model
model = load_model("tumor_detection.h5")

# Configure upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    image_path = None
    
    if request.method == 'POST':
        # Check if file was uploaded
        if 'file' not in request.files:
            return render_template('index.html', error='No file uploaded')
            
        file = request.files['file']
        
        if file.filename == '':
            return render_template('index.html', error='No selected file')
            
        if file and allowed_file(file.filename):
            # Save uploaded file
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Process image
            try:
                input_image = cv2.imread(filepath)
                input_image_reshape = cv2.resize(input_image, (128, 128))
                image_normalized = input_image_reshape / 255.0
                img_reshape = np.reshape(image_normalized, (1, 128, 128, 3))
                
                # Make prediction
                input_prediction = model.predict(img_reshape)
                input_pred_label = np.argmax(input_prediction)
                
                # Get result
                result = 'Tumor Cell' if input_pred_label == 1 else 'Normal Cell'
                confidence = float(np.max(input_prediction))
                
                return render_template('index.html', 
                                     prediction=result,
                                     confidence=confidence,
                                     image_path=filepath)
                
            except Exception as e:
                return render_template('index.html', error=f'Error processing image: {str(e)}')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)