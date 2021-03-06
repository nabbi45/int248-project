from google.colab import drive

drive.mount('/content/drive')

import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.datasets import cifar10
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
from keras.models import load_model, Model
from keras.layers import Lambda, Conv2D, UpSampling2D, Dropout, Dense, Flatten, Activation, Input
import glob as glob
import matplotlib
from keras.datasets import cifar10
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
from PIL import Image

#!wget www.robots.ox.ac.uk/~vgg/data/flowers/102/102flowers.tgz -P flower_dataset

#import tarfile
#tar = tarfile.open('flower_dataset/102flowers.tgz', "r:gz")
#tar.extractall('drive/My Drive/final_upload/')
#tar.close()

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

from keras import backend as K
K.tensorflow_backend._get_available_gpus()



dataset_final = np.concatenate((x_train,x_test),axis = 0)



colored_folder_path = "drive/My Drive/final_upload/jpg"
coloured_images = glob.glob('drive/My Drive/final_upload/jpg/'+'*.jpg')
coloured_images.sort()

import cv2
bw_images = []
for i in coloured_images:
  image_file =  cv2.imread(i)
  print(i)
  image_file = cv2.resize(image_file,(32,32))
  bw_image = np.array(image_file, dtype = np.float32) 
  bw_image = cv2.cvtColor(bw_image,cv2.COLOR_BGR2GRAY) 
  bw_image = bw_image/255
  bw_images.append(bw_image)
  
bw_images = np.array(bw_images)

import cv2
colored_images = []
for i in coloured_images:
  image_file =  cv2.imread(i)
  image_file = cv2.resize(image_file,(32,32))
  col_image = np.array(image_file, dtype = np.float32) 
  col_image = col_image/255
  colored_images.append(col_image)
  
colored_images = np.array(colored_images)

colored_images.shape

bw_images.shape

bw_images = bw_images.reshape(4624,32,32,1)

bw_images.shape

plt.imshow(bw_images[0].reshape(32,32),cmap='gist_gray')
plt.show()

plt.imshow(colored_images[25]*255)
plt.show()

X_train, X_test, y_train, y_test = train_test_split(bw_images, colored_images, test_size=0.20, random_state=101)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.10, random_state=101)

y_test.shape

X_train.shape

"""<hr>
# A Model
"""

input_layer = Input(shape=(32,32,1))
output = Conv2D(8, (5, 5), activation='relu', padding='same', strides=2)(input_layer)
output = Dropout(0.25)(output)
output = Conv2D(8, (3, 3), activation='relu', padding='same')(output)
output = Conv2D(16, (3, 3), activation='relu', padding='same')(output)
output = Conv2D(16, (3, 3), activation='relu', padding='same', strides = 2)(output)
output = Dropout(0.25)(output)
output = Conv2D(32, (3, 3), activation='relu', padding='same')(output)
output = UpSampling2D((2, 2))(output)
output = Conv2D(32, (3, 3), activation='relu', padding='same')(output)
output = UpSampling2D((2, 2))(output)
output = Conv2D(16, (3, 3), activation='relu', padding='same')(output)
#output = UpSampling2D((3, 3))(output)
output = Dropout(0.5)(output)
final_output = Conv2D(3, (3, 3), activation='sigmoid', padding='same')(output)
model = Model(input = input_layer, output = final_output)
model.compile(optimizer='rmsprop',loss='mse')
model.summary()



"""<hr>
# Training the model
"""

model.fit(x=X_train, y=y_train, batch_size=170, epochs=900,validation_data=(X_val, y_val), verbose=1)

score = model.evaluate(X_test, y_test, verbose=0)

!pip install -U -q PyDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)
model.save('model_alpha.h5')    
model_file = drive.CreateFile({'title' : 'model_alpha.h5'})
model_file.SetContentFile('model_alpha.h5')
model_file.Upload()

# download to google drive
drive.CreateFile({'id': model_file.get('id')})

model.save_weights('model_weights_alpha.h5')
weights_file = drive.CreateFile({'title' : 'model_weights-alpha.h5'})
weights_file.SetContentFile('model_weights_alpha.h5')
weights_file.Upload()
drive.CreateFile({'id': weights_file.get('id')})

test_array = []
test_index = 259
test_image = X_test[test_index]
plt.imshow(test_image.reshape(32,32), cmap='gist_gray')
print("X:")
plt.show()
test_array.append(test_image)
test_array = np.array(test_array)
output = model.predict(test_array)

plt.imshow(output[0])
print("y:")
plt.show()

plt.imshow(y_test[test_index])
print("y_true:")
plt.show()

print("difference:")
diff = abs(output[0] - y_test[test_index])
plt.imshow(diff)
plt.show()



test_array = []
test_index = 199
test_image = X_test[test_index]
plt.imshow(test_image.reshape(32,32), cmap='gist_gray')
print("X:")
plt.show()
test_array.append(test_image)
test_array = np.array(test_array)
output = model.predict(test_array)

plt.imshow(output[0])
print("y:")
plt.show()

plt.imshow(y_test[test_index])
print("y_true:")
plt.show()

print("difference:")
diff = abs(output[0] - y_test[test_index])
plt.imshow(diff)
plt.show()

test_array = []
test_index = 189

test_image = X_test[test_index]
plt.imshow(test_image.reshape(32,32), cmap='gist_gray')
print("X:")
plt.show()
test_array.append(test_image)
test_array = np.array(test_array)
output = model.predict(test_array)

plt.imshow(output[0])
print("y:")
plt.show()

plt.imshow(y_test[test_index])
print("y_true:")
plt.show()

print("difference:")
diff = abs(output[0] - y_test[test_index])
plt.imshow(diff)
plt.show()

model1.fit(x=X_train, y=y_train, batch_size=170, epochs=900,validation_data=(X_val, y_val), verbose=1)
