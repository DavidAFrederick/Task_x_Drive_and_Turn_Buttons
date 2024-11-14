import wpilib
import wpilib.drive
from commands2 import Command
from drivetrainsubsys import DriveTrain


class TeleopDrive(Command):
   def __init__(self, drivetrain: DriveTrain, controller: wpilib.Joystick):
       self.drivetrain = drivetrain
       self.addRequirements(self.drivetrain)
       self.controller = controller
       print ("TeleOpDrive Command Instantiated")


   def initialize(self):
       print ("TeleOpDrive Command Initialized")
    #    self.drivetrain.reset_left_side_encoder_count()
    #    self.drivetrain.reset_right_side_encoder_count()


   def execute(self):
       self.drivetrain.drive_teleop(-self.controller.getRawAxis(1),
                                    -self.controller.getRawAxis(0))

    #    print("Counter:  L: %6.1f    R: %6.1f " % 
    #          (self.drivetrain.get_left_side_encoder_count(),
    #          self.drivetrain.get_right_side_encoder_count()))

   def isFinished(self) -> bool:
       return False
  
   def end(self, interrupted: bool):
       self.drivetrain.drive_teleop(0,0)