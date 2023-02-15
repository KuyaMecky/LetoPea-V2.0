# take note ung sinabi ko sa post label function not nesarily na need ng i-fix tong warning as long na wala kang GPU na support ng CUDDA
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import TensorBoard
import os
from post_label import actions
from post_label import X_train,y_train,X_test,y_test,np

# gawa tayo ng log directory pra sa callback ng memory para training
log_dir = os.path.join('Logs')
tb_callback = TensorBoard(log_dir=log_dir)
model = Sequential()
model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30,1662)))
model.add(LSTM(128, return_sequences=True, activation='relu'))
model.add(LSTM(64, return_sequences=False, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(actions.shape[0], activation='softmax'))
# initiate natin ung optimizer natin for training
model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
model.fit(X_train, y_train, epochs=10000, callbacks=[tb_callback])
model.summary()

# dito gagwa na natayo ng prediction
res = model.predict(X_test)
actions[np.argmax(res[0])]
actions[np.argmax(y_test[0])]
# save natin ung weights if hindi mo alam ung weight search mo nlng sa google
model.save('action.h5')
model.load_weights('action.h5')
## ung delete optional from itself
#'del model'


# Evaluation using Confusion nang Matrix and Accuracy
from sklearn.metrics import multilabel_confusion_matrix, accuracy_score
yhat = model.predict(X_test)
ytrue = np.argmax(y_test, axis=1).tolist()
yhat = np.argmax(yhat, axis=1).tolist()
multilabel_confusion_matrix(ytrue, yhat)
accuracy_score(ytrue, yhat)
# okay na after nito proceed na tayo sa real time detection 

