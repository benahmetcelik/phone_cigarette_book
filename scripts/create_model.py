from keras import models
from keras import layers
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator

import os
import global_variables as globals
from keras.utils import to_categorical


def createModel(model_name):

    os.chdir(globals.input_dir)


    size=128
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(size,size,3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D(2, 2))
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D(2, 2))
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D(2, 2))
    model.add(layers.Conv2D(256, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D(2, 2))
    model.add(layers.Flatten())
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.Dense(3, activation='sigmoid'))

    one_hot_labels = to_categorical([0,1,2], num_classes=3)

    model.compile(optimizer=optimizers.RMSprop(learning_rate=0.0003), loss='categorical_crossentropy', metrics=['acc'])
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
    validation_datagen = ImageDataGenerator(rescale=1.255)

    train_generator = train_datagen.flow_from_directory('data/train',target_size=(size,size),batch_size=64, class_mode='categorical')
    validation_generator = validation_datagen.flow_from_directory('data/valid', target_size=(size,size), batch_size=64, class_mode='categorical')
    model.fit(train_generator, epochs=5, steps_per_epoch=60,validation_data=validation_generator, validation_steps=7, workers=4)
    os.makedirs(globals.output_dir, exist_ok=True)
    os.chdir(globals.output_dir)

    model.save(model_name+'.h5')