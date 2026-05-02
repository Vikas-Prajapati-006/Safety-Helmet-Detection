from flask import Flask, render_template, request, redirect
import os
import cv2
from ultralytics import YOLO
from src.pipeline.prediction_pipeline import PredictionPipeline # Modular pipeline use kar rahe hain

app = Flask(__name__)


model_path = "best.pt"
model = YOLO(model_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return redirect(request.url)
    
    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)

    
    os.makedirs('static/uploads', exist_ok=True)
    os.makedirs('static/results', exist_ok=True)

    
    img_path = os.path.join('static/uploads', file.filename)
    file.save(img_path)

    
    results = model.predict(img_path, conf=0.4)
    
    
    violation = True
    if len(results[0].boxes) > 0:
        for box in results[0].boxes:
            
            if int(box.cls[0]) == 0: 
                violation = False
                break

    
    res_plotted = results[0].plot()
    output_filename = "result_" + file.filename
    output_path = os.path.join('static/results', output_filename)
    cv2.imwrite(output_path, res_plotted)

    
    caption = "Violation: No Helmet Detected" if violation else "Safe: Helmet Detected"
    plate_no = "Not Detected" 

    return render_template('index.html', 
                           result_image=output_path,
                           caption=caption,
                           number=plate_no)

if __name__ == '__main__':
    
    port = int(os.environ.get("PORT", 8080))
    
    print(f"System starting... Access it locally at http://localhost:{port}")
    
    
    app.run(host='0.0.0.0', port=port, debug=False)