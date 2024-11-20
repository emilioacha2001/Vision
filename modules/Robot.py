from picarx import Picarx
from picamera2 import Picamera2
from time import sleep

class Robot:
    def __init__(self, format="RGB888"):
        self.px = Picarx()
        self.servo_names = ['direction servo', 'camera pan servo', 'camera tilt servo']
        self.motor_names = ['left motor', 'right motor']
        self.camera = Picamera2()

        self.cameraSetup(format)

    def greet(self):
        print('hola como estas')

    def cameraSetup(self, format="RGB888"):
        self.camera.preview_configuration.main.format = format
        self.camera.configure("preview")
        self.camera.start()

    def cameraCapture(self):
        return self.camera.capture_array()

    def servos_test(self):
        self.px.set_dir_servo_angle(-30)
        sleep(0.5)
        self.px.set_dir_servo_angle(30)
        sleep(0.5)
        self.px.set_dir_servo_angle(0)
        sleep(0.5)
        self.px.set_cam_pan_angle(-30)
        sleep(0.5)
        self.px.set_cam_pan_angle(30)
        sleep(0.5)
        self.px.set_cam_pan_angle(0)
        sleep(0.5)
        self.px.set_cam_tilt_angle(-30)
        sleep(0.5)
        self.px.set_cam_tilt_angle(30)
        sleep(0.5)
        self.px.set_cam_tilt_angle(0)
        sleep(0.5)

    def forward(self, speed=30):
        self.px.forward(speed)

    def backward(self, speed=30):
        self.px.backward(speed)

    def turn(self, angle=0):
        self.px.set_dir_servo_angle(angle)

    def pan(self, angle=0):
        self.px.set_cam_pan_angle(angle)

    def tilt(self, angle=0):
        self.px.set_cam_tilt_angle(angle)

    def stop(self):
        self.px.stop()