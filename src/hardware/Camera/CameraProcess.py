
import multiprocessing
from multiprocessing import Process

from src.utils.Templates.WorkerProcess import WorkerProcess
from src.hardware.Camera.CameraPublisher import CameraPublisher

class CameraProcess(WorkerProcess):
    #================================ CAMERA PROCESS =====================================
    def __init__(self, inPs, outPs, daemon = True):
        """Process that start the camera streaming.
        
        Arguments:
            inPs {list()}  -- input pipes (leave empty list)
            outPs {list()} -- output pipes (order does not matter, output camera image
                               on all pipes)
        """

        WorkerProcess.__init__(self, inPs, outPs, daemon)

    # ===================================== INIT TH ======================================
    def init_threads(self):
        camTh = CameraPublisher(self.outPs) 
        self.threads.append(camTh)