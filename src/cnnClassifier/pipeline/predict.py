import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

# {0: 'Salmonella', 1: 'Coccidiosis', 2: 'New_Castle_Disease', 3: 'Healthy'}

class PredictionPipeline:
    def __init__(self,filename):
        self.filename = filename


    
    def predict(self):
        # load model
        model = load_model(os.path.join("artifacts","training", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 3:
            prediction = 'Healthy'
        elif result[0] == 2:
            prediction = 'New_Castle_Disease'
        elif result[0] == 1:
            prediction = 'Coccidiosis'
        else:
            prediction = 'Salmonella'

        return [{"image": prediction}]
        
    
        

        



