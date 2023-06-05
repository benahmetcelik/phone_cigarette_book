import os
import main_funcs as mf


print('Welcome to the main script')
print('Please enter the model name')
model_name = input()
if  os.path.exists(os.path.join(mf.models_dir(), model_name)):
    mf.test_model(model_name)


print('PLease enter the class count')

class_count = int(input())

print('Please enter the class names')

class_names = []

for i in range(class_count):
    class_names.append(input())

ready = input('Are you ready to start? (y/n)')

if ready == 'y':
    mf.create_model(class_count, class_names,model_name)
    print('Model created')
    print('do you want to test the model')
    test = input('y/n')
    if test == 'y':
        mf.test_model(model_name)
        print('Model tested')
    else:
        print('Model not tested')

