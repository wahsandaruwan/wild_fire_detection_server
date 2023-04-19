# -----Imports-----
import pickle as pk
import numpy as np

# -----Generate prediction function-----
def generate_prediction(env_data):
    """Generate wild fire intensity level based on environmental data
    """ 
    # Preprocess   
    env_data_np = np.array(env_data)
    env_data_reshape = np.reshape(env_data_np, (-1, 9))

    # Load the model
    loaded_model = pk.load(open('./Model/model_pickle', 'rb'))

    # Get the prediction
    result = loaded_model.predict(env_data_reshape)

    return str(result[0])

# generate_prediction([94.9, 130.3, 587.1,	14.1, 97.4,	40,	5.8, 0, 1])