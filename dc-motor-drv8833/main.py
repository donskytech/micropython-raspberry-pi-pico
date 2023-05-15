from robot_car import RobotCar
import utime

# Pico W GPIO Pin
LEFT_MOTOR_PIN_1 = 16
LEFT_MOTOR_PIN_2 = 17
RIGHT_MOTOR_PIN_1 = 18
RIGHT_MOTOR_PIN_2 = 19

motor_pins = [LEFT_MOTOR_PIN_1, LEFT_MOTOR_PIN_2, RIGHT_MOTOR_PIN_1, RIGHT_MOTOR_PIN_2]

# Create an instance of our robot car
robot_car = RobotCar(motor_pins, 20000)

if __name__ == '__main__':
    try:
        # Test forward, reverse, stop, turn left and turn right
        print("*********Testing forward, reverse and loop*********")
        for i in range(2):
            print("Moving forward")
            robot_car.move_forward()
            utime.sleep(2)
            print("Moving backward")
            robot_car.move_backward()
            utime.sleep(2)
            print("stop")
            robot_car.stop()
            utime.sleep(2)
            print("turn left")
            robot_car.turn_left()
            utime.sleep(2)
            print("turn right")
            robot_car.turn_right()
            utime.sleep(2)
            
        print("*********Testing speed*********")
        for i in range(2):
            print("Moving at 100% speed")
            robot_car.change_speed(100);
            robot_car.move_forward()
            utime.sleep(2)
            
            print("Moving at 50% speed")
            robot_car.change_speed(50);
            robot_car.move_forward()
            utime.sleep(2)
            
            print("Moving at 20% of speed")
            robot_car.change_speed(20);
            robot_car.move_forward()
            utime.sleep(2)
            
            print("Moving at 0% of speed or the slowest")
            robot_car.change_speed(0);
            robot_car.move_forward()
            utime.sleep(2)
            
        robot_car.deinit()

    except KeyboardInterrupt:
        robot_car.deinit()