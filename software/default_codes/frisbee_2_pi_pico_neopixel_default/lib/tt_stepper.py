#28byj-48 Library

# stepper.py
import board
import time
import digitalio



class Stepper:
    
    position = 0
    speed = 2
    acceleration = 0

    pin1 = digitalio.DigitalInOut(board.GP0)
    pin2 = digitalio.DigitalInOut(board.GP1)
    pin3 = digitalio.DigitalInOut(board.GP3)
    pin4 = digitalio.DigitalInOut(board.GP4)
    pin1.direction = digitalio.Direction.OUTPUT
    pin2.direction = digitalio.Direction.OUTPUT
    pin3.direction = digitalio.Direction.OUTPUT
    pin4.direction = digitalio.Direction.OUTPUT

    def __init__(self, steps):
        self.steps_per_rotation = steps

    def statefromsteppin(self, pin, step):
        output = (step + pin - 2) % 4 == 1 or (step + pin - 2) % 4 == 2        
        return output

    def move_to(self, target_pos, speed=50, accel=0):
        self.move_relative(target_pos - self.position, speed, accel)

    def move_relative(self, steps, speed=50, accel=0):

        speed = min(speed,100)
        direction = 1 if steps > 0 else -1
        curr_speed = 0.1
        
        for i in range(0, steps, direction):
            self.position += direction
            self.pin1.value = self.statefromsteppin(1, self.position)
            self.pin2.value = self.statefromsteppin(2, self.position)
            self.pin3.value = self.statefromsteppin(3, self.position)
            self.pin4.value = self.statefromsteppin(4, self.position)
            
            if accel == 0:
                time.sleep(60 / (speed * self.steps_per_rotation *0.1))
            else:
                curr_speed += min(accel,100)/200 if i < steps / 2 else -min(accel,100)/200
                curr_speed_limited = min(curr_speed, speed * 0.1) # limit to speed
                time.sleep(60 / (curr_speed_limited * self.steps_per_rotation))
            
    def disable(self):
            self.pin1.value = 0
            self.pin2.value = 0
            self.pin3.value = 0
            self.pin4.value = 0

    def set_position(self, set_pos):
        self.position = set_pos

         
        