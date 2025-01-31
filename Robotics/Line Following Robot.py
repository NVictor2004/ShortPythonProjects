from gpiozero import Robot, LineSensor

robot = Robot(left=(7, 8), right=(9, 10))
left_sensor = LineSensor(17)
right_sensor= LineSensor(27)

def motor_speed():
   while True:
      left_detect  = int(left_sensor.value)
      right_detect = int(right_sensor.value)
      print(left_detect, right_detect)
      ## Stage 1
      if left_detect == 0 and right_detect == 0:
         left_mot = 1
         right_mot = 1
      if left_detect == 0 and right_detect == 1:
         left_mot = -1
      if left_detect == 1 and right_detect == 0:
         right_mot = -1
      print(left_mot, right_mot)
      yield (right_mot, left_mot)

robot.source = motor_speed()
                                                                         
