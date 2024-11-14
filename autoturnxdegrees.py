import wpilib
import wpilib.drive
from commands2 import Command
from drivetrainsubsys import DriveTrain
import math


class AutoTurnXDegrees(Command):
   def __init__(self, drivetrain: DriveTrain, targetHeading: int, turnSpeed: float):
       self.drivetrain = drivetrain
       self.targetHeading = targetHeading
       self.turnSpeed = turnSpeed
       self.differenceBetweenTargetAndCurrent = 0
       self.addRequirements(self.drivetrain)
       self.drivetrain.reset_gyro()
       self.current_heading = self.drivetrain.get_gyro_heading()
       print ("Heading Change of ", self.targetHeading,  "  Command Initialized")


   def initialize(self):
       super().initialize()
       self.drivetrain.reset_gyro()
       self.current_heading = self.drivetrain.get_gyro_heading()


   def execute(self):
       self.currentHeading = self.drivetrain.get_gyro_heading()
       self.differenceBetweenTargetAndCurrent = self.targetHeading - self.currentHeading


       print ("Gyro Heading (Clockwise turn is negative: ", self.currentHeading,
              "   Target heading: ", self.targetHeading,
              "    Difference: ", self.differenceBetweenTargetAndCurrent )
       if self.differenceBetweenTargetAndCurrent > 0:     
           # Would like to turn Clockwise
           self.drivetrain.drive_teleop(0.0, self.turnSpeed)
       else:
           self.drivetrain.drive_teleop(0.0, -self.turnSpeed)  
           # Positive turn value moves robot counter clockwise


   def isFinished(self) -> bool:
       if (math.fabs(self.differenceBetweenTargetAndCurrent) < 5):
           return True
       else:
           return False


   def end(self, interrupted: bool):
       self.drivetrain.drive_teleop(0,0)