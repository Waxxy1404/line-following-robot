import sim
import cv2
import array
import numpy as np
import time
from PIL import Image as I

print('program started')
sim.simxFinish(-1)
clientID=sim.simxStart('127.0.0.1',19997,True,True,5000,5)
print ('Connected to remote API server')
print(clientID)
r, colorCam = sim.simxGetObjectHandle(clientID, "kinect_rgb", sim.simx_opmode_oneshot_wait);
r, leftmotor = sim.simxGetObjectHandle(clientID, "Pioneer_p3dx_leftMotor", sim.simx_opmode_oneshot_wait);
r, rightmotor = sim.simxGetObjectHandle(clientID, "Pioneer_p3dx_rightMotor", sim.simx_opmode_oneshot_wait);

print(rightmotor)
print(leftmotor)
print(colorCam)

sim.simxSetJointTargetVelocity(clientID, leftmotor, 0, sim.simx_opmode_streaming);
sim.simxSetJointTargetVelocity(clientID, rightmotor, 0, sim.simx_opmode_streaming);

r, resolution, image = sim.simxGetVisionSensorImage(clientID, colorCam, 1, sim.simx_opmode_streaming);
time.sleep(0.5)

last_rotation_left = 1
last_rotation_right = 1

while True:
	r, resolution, image = sim.simxGetVisionSensorImage(clientID, colorCam, 1, sim.simx_opmode_buffer);
	mat = np.asarray(image, dtype=np.int8) + 127
	mat2 = mat.reshape(resolution[1], resolution[0], 1)
	
	coord = -1
	numcoords = 0
	
	for x in range(0, resolution[0], 3):
		for k in range(0, resolution[1]-300, 3):
			if mat2[k, x] < 32:
				coord += x
				numcoords += 1
	if numcoords > 0:
		coord = coord/numcoords
		print(coord)

	if coord == -1:
		sim.simxSetJointTargetVelocity(clientID, leftmotor, last_rotation_left, sim.simx_opmode_streaming);
		sim.simxSetJointTargetVelocity(clientID, rightmotor, last_rotation_right, sim.simx_opmode_streaming);
	else:

		last_rotation_left = 1.4*(2*coord/resolution[0])
		last_rotation_right = 1.4*(2*(resolution[0]-coord)/resolution[0])
		sim.simxSetJointTargetVelocity(clientID, leftmotor, 1.4*(2*coord/resolution[0]), sim.simx_opmode_streaming);
		sim.simxSetJointTargetVelocity(clientID, rightmotor, 1.4*(2*(resolution[0]-coord)/resolution[0]), sim.simx_opmode_streaming);
		cv2.imshow('CAMERA DO ROBO SIMULADO', cv2.flip( mat2, 0 ))	
		cv2.waitKey(1)
