import wpilib 
import wpilib.drive
from commands2 import Command
from drivetrainsubsys import DriveTrain
from wpilib import SmartDashboard

class AutoDriveXWheelCounts(Command):
   def __init__(self, drivetrain: DriveTrain, targetwheelcounts: float, forwardSpeed: int):
       self.drivetrain = drivetrain
       self.targetwheelcounts = targetwheelcounts
       self.forwardSpeed = forwardSpeed
       self.addRequirements(self.drivetrain)
       self.drivetrain.reset_left_side_encoder_count()
       self.drivetrain.reset_right_side_encoder_count()
       print ("Driving for ", targetwheelcounts,  " Wheel Counts Command Initialized")

       self.printCounter = 0


   def initialize(self):
       super().initialize()
       self.drivetrain.reset_left_side_encoder_count()

       self.printCounter = 0


   def execute(self):
       self.drivetrain.drive_teleop(self.forwardSpeed, 0.0)
       self.printCounter = self.printCounter + 1

       if (self.printCounter > 12) :    
            # print ("Wheel Counts: ", self.drivetrain.get_left_side_encoder_count())
            print("Counter::  L: %6.1f    R: %6.1f " % 
                (self.drivetrain.get_left_side_encoder_count(),
                self.drivetrain.get_right_side_encoder_count()))
            self.printCounter = 0
       SmartDashboard.putNumber ("Left Counter: ", self.drivetrain.get_left_side_encoder_count() )
       SmartDashboard.putNumber ("Right Counter: ", self.drivetrain.get_right_side_encoder_count() )

   def isFinished(self) -> bool:
       if self.drivetrain.get_left_side_encoder_count() >= self.targetwheelcounts:
           return True
       else:
           return False
  
   def end(self, interrupted: bool):
       self.drivetrain.drive_teleop(0,0)


