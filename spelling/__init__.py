from .spellingcorrector import SpellingModel

# Set up the package interface
import os
import pickle
__modelpath = os.path.join(os.path.dirname(__file__), "spelling.model")

# Load saved spelling dictionary
with open(__modelpath, "rb") as handler:
    __MODEL = pickle.load(handler)

# abstract the model functions
fit = __MODEL.fit
predict = __MODEL.predict

# Provide function to update the package dictionary
def save(model: SpellingModel = None):
    if model is None: model = __MODEL

    with open(__modelpath, "wb") as handler:
        pickle.dump(model, handler)