import numpy as np
import warnings
from tensorflow.keras.models import load_model
from tensorflow.keras.optimizers import Adam
from .datasets import ECGSequence

warnings.filterwarnings("ignore")

def predict(id):
    path_to_hdf5 = r"D:\git_ECG\automatic-ecg-diagnosis-master\data\ecg_data.hdf5"
    path_to_model = r"D:\git_ECG\final_model.hdf5"
    dataset_name = "tracings"
    output_file = "./dnn_output.npy"
    batch_size = 1
    

    # Import data
    seq = ECGSequence(path_to_hdf5, dataset_name, batch_size=batch_size,start_idx=id,end_idx=id+1)

    # Import model
    model = load_model(path_to_model, compile=False)
    model.compile(loss='binary_crossentropy', optimizer=Adam())

    # y_score = model.predict(seq, verbose=1)
    y_score=model.predict(seq)
    y_score_formatted = ["{:.10f}".format(score) for score in y_score[0]]

    # threshold = 0.8
    # y_score_new = [1 if y >= threshold else 0 for y in y_score[0]]
    return y_score_formatted