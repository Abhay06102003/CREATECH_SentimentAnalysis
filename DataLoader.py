import numpy as np
import pandas as pd
from DATA_PRE import transformer
from sklearn.preprocessing import LabelEncoder as le

def load_data(file):
    df = pd.read_csv(file)
    y = df['sentiment']
    x = df['text']
    return x,y
def preprocess(x,y):
    le1 = le()
    labels = le1.fit_transform(y)
    labels = np.array(labels)
    tx = transformer()
    text = tx.encoder(x)
    text = np.array(text)
    return text,labels
