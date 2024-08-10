import sim
import time
import sys
import keyboard
def moveFWD(clientID, motorL, motorR, speed):
    errorCode = sim.simxSetJointTargetVelocity(clientID, motorL, speed, sim.simx_opmode_oneshot_wait)
    errorCode = sim.simxSetJointTargetVelocity(clientID, motorR, speed, sim.simx_opmode_oneshot_wait)
    time.sleep(0.1)
    return errorCode
#0.48 speed will bw paired with 1 second time
def turnRight(clientID, motorL, motorR):
    errorCode = sim.simxSetJointTargetVelocity(clientID, motorL, 0.49, sim.simx_opmode_oneshot_wait)
    errorCode = sim.simxSetJointTargetVelocity(clientID, motorR, -0.49, sim.simx_opmode_oneshot_wait)
    time.sleep(0.1)
    return errorCode

def turnLeft(clientID, motorL, motorR):
    errorCode = sim.simxSetJointTargetVelocity(clientID, motorL, -0.49, sim.simx_opmode_oneshot_wait)
    errorCode = sim.simxSetJointTargetVelocity(clientID, motorR, 0.49, sim.simx_opmode_oneshot_wait)
    time.sleep(0.1)
    return errorCode

def moveBWD(clientID, motorL, motorR, speed):
    errorCode = sim.simxSetJointTargetVelocity(clientID, motorL, -speed, sim.simx_opmode_oneshot_wait)
    errorCode = sim.simxSetJointTargetVelocity(clientID, motorR, -speed, sim.simx_opmode_oneshot_wait)
    time.sleep(0.1)
    return errorCode




print("Program Started!")
sim.simxFinish(-1)
clientID = sim.simxStart('127.0.0.1',19999, True, True, 5000, 5)

time.sleep(1)
if(clientID != -1):
    print("Connected Successfully")
else:
    sys.exit('Failed to connect')
errorCode, left_motor_handle = sim.simxGetObjectHandle(clientID, '/PioneerP3DX/leftMotor', sim.simx_opmode_oneshot_wait)
errorCode, right_motor_handle = sim.simxGetObjectHandle(clientID, '/PioneerP3DX/rightMotor', sim.simx_opmode_oneshot_wait)


while True:
    try:
        if keyboard.is_pressed('w'):
            print("forward")
            errorCode = moveFWD(clientID,left_motor_handle,right_motor_handle,1)
        if keyboard.is_pressed('a'):
            print("left")
            errorCode = turnLeft(clientID,left_motor_handle,right_motor_handle)
        if keyboard.is_pressed('s'):
            print("backward")
            errorCode = moveBWD(clientID,left_motor_handle,right_motor_handle,1)
        if keyboard.is_pressed('d'):
            print("right")
            errorCode = turnRight(clientID,left_motor_handle,right_motor_handle)
    except:
        break
