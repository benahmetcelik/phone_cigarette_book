import os
import global_variables as globals
def test_model(model_name):
    import detect_cam
    detect_cam.detectCam(model_name)

    print('Model tested')


def models_dir():
    models_dir = globals.output_dir
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)   
    return models_dir     

def create_model(class_count, class_names, model_name):
    import get_data_from_cam
    print('Model training started')
    for i in range(class_count):
        get_data_from_cam.getDataFromCam('data/train',class_names[i],1000)
        get_data_from_cam.getDataFromCam('data/valid',class_names[i],200)
    print('Model Trained')
    import create_model as create_model_py
    create_model_py.createModel(model_name)        