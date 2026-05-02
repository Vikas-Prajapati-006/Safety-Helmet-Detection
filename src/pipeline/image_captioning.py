from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

class ImageCaptioning:
    def __init__(self):
        
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    def get_caption(self, image_path):
        
        raw_image = Image.open(image_path).convert('RGB')
        
        
        inputs = self.processor(raw_image, return_tensors="pt")

        
        out = self.model.generate(**inputs)
        
        
        caption = self.processor.decode(out[0], skip_special_tokens=True)
        
        return caption