from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time
import atexit



class motor():

	def __init__(self):
		self.motorHat = Adafruit_MotorHAT(addr=0x60)

	def release(self):
		for i in range(1,4):
			self.motorHat.getMotor(i).run(Adafruit_MotorHAT.RELEASE)

	def testMotors(self):

		for i in range(1,4):

			print("Testing motor " + i)

			print("Forward, half speed")
			self.motorHat.getMotor(i).setSpeed(128)
			self.motorHat.getMotor(i).run(Adafruit_MotorHAT.FORWARD)
			time.sleep(2)

			print("Forward, full speed")
			self.motorHat.getMotor(i).setSpeed(255)
			self.motorHat.getMotor(i).run(Adafruit_MotorHAT.FORWARD)
			time.sleep(2)

			print("Backwards, half speed")
			self.motorHat.getMotor(i).setSpeed(128)
			self.motorHat.getMotor(i).run(Adafruit_MotorHAT.BACKWARD)
			time.sleep(2)

			print("Backwards, full speed")
			self.motorHat.getMotor(i).setSpeed(255)
			self.motorHat.getMotor(i).run(Adafruit_MotorHAT.BACKWARD)
			time.sleep(2)


		print("Test finalized. Releasing motors")
		self.release
