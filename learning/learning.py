'''モデルを作成し、kerasでモデルを構築し、VGG16をFine-tuningしてモデルの学習を行うプログラム。
Fine-tuningは、学習済モデルを、重みデータを一部再学習して特徴量抽出機として利用する学習方法である。
'''
import os
import tensorflow as tf
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Input, Activation, Dropout, Flatten, Dense
from tensorflow.keras import optimizers
import numpy as np
import time
from tensorflow.keras.utils import to_categorical

print(tf.__version__)
exit()

members = ["松本潤","二宮和也","相葉雅紀","櫻井翔","大野智"]
nb_members = len(members)
img_width, img_height = 150, 150

# トレーニング用とバリデーション用の画像格納先
train_data_dir = './FaceEdited2'
validation_data_dir = './Test'
#トレーニングデータ用の画像数
nb_train_samples = 800
#バリデーション用の画像数
nb_validation_samples = 200
#バッチサイズ
batch_size = 32
#エポック数
nb_epoch = 10


# トレーンング用、バリデーション用データを生成するジェネレータ作成。
#ImageDataGeneratorのrescaleで正規化する。
train_datagen = ImageDataGenerator(rescale=1.0 / 255,)
validation_datagen = ImageDataGenerator(rescale=1.0 / 255)
# トレーンング用データの作成。
train_generator = train_datagen.flow_from_directory(
  train_data_dir,
  target_size=(img_width, img_height),
  color_mode='rgb',
  classes=members,
  class_mode='categorical',
  batch_size=batch_size,
  shuffle=True)
# バリデーション用データの作成。
validation_generator = validation_datagen.flow_from_directory(
  validation_data_dir,
  target_size=(img_width, img_height),
  color_mode='rgb',
  classes=members,
  class_mode='categorical',
  batch_size=batch_size,
  shuffle=True)


from tensorflow.keras.layers import Dense, Dropout, Flatten, Input, BatchNormalization
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras import optimizers
import tensorflow.keras.callbacks
from tensorflow.keras.callbacks import EarlyStopping

input_tensor = Input(shape=(img_width, img_height, 3))
vgg16 = VGG16(include_top=False, weights='imagenet', input_tensor=input_tensor)
# VGG16のFC層の作成
top_model = Sequential()
top_model.add(Flatten(input_shape=vgg16.output_shape[1:]))
top_model.add(Dense(256, activation='relu'))
top_model.add(Dropout(0.5))
top_model.add(Dense(nb_members, activation='softmax'))

# VGG16とFC層を結合してモデルを作成
vgg_model = Model(inputs=vgg16.inputs, outputs=top_model(vgg16.outputs))

# VGG16の一部の層は重みを固定（frozen）
for layer in vgg_model.layers[:15]:
    layer.trainable = False

# 多クラス分類を指定
vgg_model.compile(loss='binary_crossentropy',
          optimizer=optimizers.SGD(lr=1e-3, momentum=0.9),
          metrics=['accuracy'])
          
history = vgg_model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples/batch_size,
    epochs=nb_epoch,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples)

#resultsディレクトリを作成
result_dir = 'results'
if not os.path.exists(result_dir):
    os.mkdir(result_dir)

# 重みを保存
vgg_model.save_weights(os.path.join(result_dir, 'Weight8.h5'))

# 作成したモデルを保存
#vgg_model.save('VGGtake.h5')
                             
# 学習結果を描写
import matplotlib.pyplot as plt

#acc, val_accのプロット
plt.plot(history.history["accuracy"], label="acc", ls="-", marker="o")
plt.plot(history.history["val_accuracy"], label="val_acc", ls="-", marker="x")
plt.ylabel("accuracy")
plt.xlabel("epoch")
plt.legend(loc="best")
#Final.pngという名前で、結果を保存
plt.savefig('Final8.png')
plt.show()