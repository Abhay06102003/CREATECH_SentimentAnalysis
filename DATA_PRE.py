import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer as ST

class transformer:
    def __init__(self):
        self.model_token = 'distilbert-base-nli-mean-tokens'
        self.model = ST(self.model_token)
    def encoder(self,text):
        return self.model.encode(text,show_progress_bar = True)
