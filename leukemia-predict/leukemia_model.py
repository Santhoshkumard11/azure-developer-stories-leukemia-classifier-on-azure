import logging
import numpy as np

# Keras
from keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.models import load_model
from keras.preprocessing import image
from tensorflow.python.keras.backend import set_session

import os
import tensorflow as tf
import keras.backend.tensorflow_backend as tb
tb._SYMBOLIC_SCOPE.value = True


# Model saved with Keras model.save()
MODEL_PATH = 'leukemia-predict/models/200epoch.model'

# Load your trained model
global graph
graph = tf.get_default_graph()

# set the session state for detection
sess = tf.Session()
set_session(sess)
# load the model and get the model running for prediction
model = load_model(MODEL_PATH)
model._make_predict_function()


def model_predict(img_path, model):
    """ Make predictions by loading the image into the session

    Args:
        img_path ([str]): image path url
        model ([object]): loaded model object

    Returns:
        [np.array]: numpy array with the values of each class
    """
    # loading the image with the set target
    img = image.load_img(img_path, target_size=(200, 200))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    x = np.expand_dims(x, axis=0)

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
    x = preprocess_input(x, mode='caffe')
    preds = ""
    # set the default graph again
    with graph.as_default():
        # set the same session for prediction
        set_session(sess)
        preds = model.predict(x)

    logging.info('Predition made successfully!!!')
    return preds


def predict_output(temp_image_name: str):
    """Return the type of leukemia based on the input image

    Args:
        image_name (str): image name
    Returns:
        [str]: return the type of leukemia
    """

    # Make prediction
    preds = model_predict(temp_image_name, model)

    # Process your result for human
    pred_class = preds.argmax(axis=1)            # Simple argmax
    # pred_class = decode_predictions(preds, top=1)   # ImageNet Decode
    # result = str(pred_class[0][0][1])               # Convert to string
    classes = {0: "ALL", 1: "AML", 2: "CLL", 3: "CML"}

    result = str(classes[int(pred_class)])
    return result
