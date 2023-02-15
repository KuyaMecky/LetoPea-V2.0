import os
from Function import np
# Path for exported data, numpy arrays
DATA_PATH = os.path.join('Collection_DS') 

# Actions that we try to detect
# 'kamusta!', 'goodmorning', 'thank you' last trained
actions = np.array(['no detection'
                    ])

# Thirty videos worth of data
no_sequences = 30

# Videos are going to be 30 frames in length
sequence_length = 30

# Folder start
start_folder = 0
for action in actions: 
    for sequence in range(no_sequences):
        try: 
            os.makedirs(os.path.join(DATA_PATH, action, str(sequence)))
        except:
            pass

      