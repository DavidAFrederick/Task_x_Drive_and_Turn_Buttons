import wpilib
import wpilib.drive
from commands2 import Command
from drivetrainsubsys import DriveTrain




class AutoDriveXSeconds(Command):
  def __init__(self, drivetrain: DriveTrain, seconds: int, forwardSpeed: float):
       self.drivetrain = drivetrain
       self.seconds = seconds
       self.forwardSpeed = forwardSpeed
       self.counter = 50 * seconds
       self.addRequirements(self.drivetrain)
       print ("Driving for ", seconds,  "  Command Instantiated")


  def initialize(self):
       super().initialize()
       self.countDownCounter = self.counter
       print ("Driving for Command Initialized !!!!")


  def execute(self):
       self.drivetrain.drive_teleop(self.forwardSpeed, 0.0)
       self.countDownCounter = self.countDownCounter - 1




  def isFinished(self) -> bool:
      if self.countDownCounter <= 0:
          return True
      else:
          return False
  def end(self, interrupted: bool):
      self.drivetrain.drive_teleop(0,0)




