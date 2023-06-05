import sys
import os
import cv2
from PIL import Image
import global_variables as globals


def getDataFromCam(folder,filename,imagecount):


        '''
        folder = sys.argv[1]
        filename = sys.argv[2]
        imagecount = int(sys.argv[3])
        '''

        if imagecount < 1:
                print("Image count should be greater than 0")
                sys.exit()

        path=globals.input_dir
        os.chdir(r"C:\\")
        video_path = globals.videoPath(filename+'.mp4')
        directory=os.path.join(path, folder, filename)


        os.makedirs(directory, exist_ok=True)
        video = cv2.VideoCapture(video_path)
        filename = len(os.listdir(directory))
        count = 0

        video_frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

        if video_frame_count < imagecount:
                print("Video frame count is less than image count")
                print("Video frame count: ", video_frame_count)
                imagecount = video_frame_count


        while True and count < imagecount:
                filename += 1
                count += 1
                _, frame = video.read()
                #im = Image.fromarray(frame, 'RGB')
                im = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                im = im.resize((256,256))
                im.save(os.path.join(directory, str(filename)+".jpg"), "JPEG")

                cv2.imshow("Capturing", frame)
                key=cv2.waitKey(1)
                if key == ord('q'):
                        break
        video.release()
        cv2.destroyAllWindows()