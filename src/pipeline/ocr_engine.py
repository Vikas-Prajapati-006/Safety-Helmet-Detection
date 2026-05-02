import easyocr
import logging

# Faltu warnings ko ignore karne ke liye
logging.getLogger('easyocr').setLevel(logging.ERROR)

class OCREngine:
    def __init__(self):
        
        print("Initializing EasyOCR on CPU...")
        self.reader = easyocr.Reader(['en'], gpu=False) 

    def extract_text(self, image_path):
        try:
            
            results = self.reader.readtext(image_path, detail=0)
            if not results:
                return "Not Detected"
            
            
            plate_text = " ".join(results).upper().strip()
            return plate_text
        except Exception as e:
            print(f"OCR Error: {e}")
            return "Detection Error"