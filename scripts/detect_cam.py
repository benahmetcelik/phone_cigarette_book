import cv2
import numpy as np
from PIL import Image
from keras import models
import os
import global_variables as globals



def detectCam(model_name):
    
        os.chdir(globals.output_dir)

        # Load the saved model
        model = models.load_model(model_name+'.h5')
        video = cv2.VideoCapture(1)

        while True:
                _, frame = video.read()
                text = 'Bilinmiyor'
                
                # Convert the captured frame into RGB
                im = Image.fromarray(frame, 'RGB')

                # Resizing into 128x128 because we trained the model with this image size
                im = im.resize((128, 128))
                img_array = np.array(im)

                # Our keras model used a 4D tensor, (images x height x width x channel)
                # So changing dimension 128x128x3 into 1x128x128x3
                img_array = np.expand_dims(img_array, axis=0)

                # Calling the predict method on model to predict the object on the image
                prediction = int(model.predict(img_array)[0][0])

                if prediction == 0:
                        text = 'Peçete'
                elif prediction == 1:
                        text = 'Sigara'
                elif prediction == 2:
                        text = 'Şişe'

                # Frame reversed
                frame = cv2.flip(frame, 1)

                # Add text to the frame
                bottom_right_corner = (frame.shape[1] - 800, frame.shape[0] - 10)
                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 1
                font_color = (255, 255, 255)
                line_type = 2
                cv2.putText(frame, text, bottom_right_corner, font, font_scale, font_color, line_type)

                cv2.imshow("Capturing", frame)
                key = cv2.waitKey(1)
                if key == ord('q'):
                        break

        video.release()
        cv2.destroyAllWindows()
