import cv2

class VideoLoader:
    '''
    classdocs
    '''


    def __init__(self, path):
        self.frames=[]
        self.video= cv2.VideoCapture(path)
        self.fps= self.video.get(cv2.CAP_PROP_FPS)
        self.delay=self.__calc_delay(self.fps)
        self.frames_count=int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
        self.__init_frames()
    
    def get_encode_frames(self):
        return self.frames
    
    def get_frames_count(self):
        return self.frames_count
    
    def get_dealy(self):
        return self.delay
    
    def __calc_delay(self,fps):
        return 1000/fps  
    
    
    def __init_frames(self):
        for f in range(0,self.frames_count):
            if not self.video.isOpened():
                print("Error de carga de video")
                break
            else:
                retValue,frame=self.video.read()
                if retValue :
                    data= cv2.imencode('.jpg',frame)[1].tostring()
                    self.frames.append(data)
        self.video.release()