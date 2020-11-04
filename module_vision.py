import cv2 as cv2


class module_vision:

    def __init__(self, index):
        self.camera_capture = cv2.VideoCapture(index, cv2.CAP_DSHOW)

    def tracking_color(self, frame):
        self.gray = cv2.cvtColor(frame, cv2.BGR2GRAY)

    def camera_capture_active(self):
        ret, frame = self.camera_capture.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.release()
            cv2.destroyAllWindows()
            return True
