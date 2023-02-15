# Ignore if may warning ibig sabihin lng na hind support ng Cudda ung rig mo or wala kang gamit na GPU
## take note sa LSTM models hindi neccesarry need nang GPU some CPU models support integrated GPU for training
## pero medyo mas matagal nag pag tra-train natin sa mga model na gagwin natin
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

import os
from training_detection import action,actions
from pathfile import DATA_PATH,sequence_length
from Function import np

label_map = {label:num for num, label in enumerate(actions)}
sequences, labels = [], [],
for action in actions:
    for sequence in np.array(os.listdir(os.path.join(DATA_PATH, action))).astype(int):
        window = []
        for frame_num in range(sequence_length):
            res = np.load(os.path.join(DATA_PATH, action, str(sequence), "{}.npy".format(frame_num)))
            window.append(res)
        sequences.append(window)
        labels.append(label_map[action])


# dito convert numpy into sequence para sa training model na ginawa natin then asign label for each model
# and take note na after ma asign ung model into numpy into shape model proceed to building and train LSTM Nueral etwork

np.array(sequences).shape
np.array(labels).shape
X = np.array(sequences)
X.shape
y = to_categorical(labels).astype(int)

# after natin mag asign nang labels i-pasa naman natin to sa training model natin 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)
y_test.shape