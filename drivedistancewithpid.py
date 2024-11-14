import wpilib 
import wpilib.drive
from commands2 import Command
from drivetrainsubsys import DriveTrain
from wpilib import SmartDashboard

import wpimath.controller
import wpimath.filter


class DriveDistanceWithPID(Command):
   def __init__(self, drivetrain: DriveTrain, targetwheelcounts: float, forwardSpeed: int):
       self.drivetrain = drivetrain
       self.targetwheelcounts = targetwheelcounts
       self.forwardSpeed = forwardSpeed
       self.addRequirements(self.drivetrain)
       self.drivetrain.reset_left_side_encoder_count()
       self.drivetrain.reset_right_side_encoder_count()
       print ("Driving for ", targetwheelcounts,  " Wheel Counts Command Initialized")

       self.printCounter = 0

       # proportional speed constant
       # negative because applying positive voltage will bring us closer to the target
       self.kP = -0.001
        # integral speed constant
       self.kI = 0.0
        # derivative speed constant
       self.kD = 0.0
       self.pidController = wpimath.controller.PIDController(self.kP, self.kI, self.kD)


   def initialize(self):
       super().initialize()
       self.drivetrain.reset_left_side_encoder_count()

       self.printCounter = 0

       self.pidController.setSetpoint(5)



   def execute(self):
    #    self.drivetrain.drive_teleop(self.forwardSpeed, 0.0)
       self.printCounter = self.printCounter + 1

       if (self.printCounter > 12) :    
            # print ("Wheel Counts: ", self.drivetrain.get_left_side_encoder_count())
            print("Counter::  L: %6.1f    R: %6.1f " % 
                (self.drivetrain.get_left_side_encoder_count(),
                self.drivetrain.get_right_side_encoder_count()))
            self.printCounter = 0
       SmartDashboard.putNumber ("Left Counter: ", self.drivetrain.get_left_side_encoder_count() )
       SmartDashboard.putNumber ("Right Counter: ", self.drivetrain.get_right_side_encoder_count() )

       pidOutput = self.pidController.calculate(self.drivetrain.get_left_side_encoder_count())
       print ("pidOutput: ", pidOutput)
    #    self.robotDrive.arcadeDrive(pidOutput, 0, False)
       self.drivetrain.drive_teleop(pidOutput, 0.0)



   def isFinished(self) -> bool:
       if self.drivetrain.get_left_side_encoder_count() >= self.targetwheelcounts:
           return True
       else:
           return False
  
   def end(self, interrupted: bool):
       self.drivetrain.drive_teleop(0,0)


