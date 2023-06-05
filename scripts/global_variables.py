import os
parent_dir = os.path.dirname(os.getcwd())
input_dir = os.path.join(parent_dir, 'input')
output_dir = os.path.join(parent_dir, 'output')
video_path = os.path.join(input_dir, 'videos')


def videoPath(videoName):
    return os.path.join(video_path, videoName)