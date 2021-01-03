from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, Activation

model = Sequential()

model.add(LSTM(
         input_shape=(50, 15),  # (timestamp, nb_features)
         units=100,
         return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(
          units=50,
          return_sequences=False))
model.add(Dropout(0.2))

model.add(Dense(units=1, activation='sigmoid'))