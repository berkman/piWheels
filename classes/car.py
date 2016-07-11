from Adafruit_MotorHAT import Adafruit_MotorHAT
import atexit


class Car(object):
    steering_direction = None
    motor_direction = None
    drive_motor = None
    steer_motor = None

    # create a default object, no changes to I2C address or frequency
    mh = Adafruit_MotorHAT(addr=0x60)

    STEERING_DIRECTIONS = ['LEFT', 'RIGHT', 'RELEASE']
    MOTOR_DIRECTIONS = ['FORWARD', 'BACKWARD', 'RELEASE']

    def __init__(self, steering_direction='NONE', motor_direction='NONE', drive_motor=mh.getMotor(3), steer_motor=mh.getMotor(4)):
        self.steering_direction = steering_direction
        self.motor_direction = motor_direction
        self.drive_motor = drive_motor
        self.steer_motor = steer_motor

    def get_steering_direction(self):
        return self.steering_direction

    def get_motor_direction(self):
        return self.motor_direction

    def set_steering_direction(self, steering_direction):
        if steering_direction in self.STEERING_DIRECTIONS:
            self.steering_direction = steering_direction
        else:
            raise ValueError('Invalid Steering Direction')

    def set_motor_direction(self, motor_direction):
        if motor_direction in self.MOTOR_DIRECTIONS:
            self.motor_direction = motor_direction

            drive_motor.run(Adafruit_MotorHAT[motor_direction])
            drive_motor.setSpeed(255)
        else:
            raise ValueError('Invalid Motor Direction')

    # recommended for auto-disabling motors on shutdown!
    def turn_off_motors(self):
        self.drive_motor.run(Adafruit_MotorHAT.RELEASE)
        self.steer_motor.run(Adafruit_MotorHAT.RELEASE)
