import wpilib
from drivetrainsubsys import DriveTrain
from teleopdrivecmd import TeleopDrive
from commands2 import Command, RunCommand, TimedCommandRobot, button
# from autodrivexseconds import AutoDriveXSeconds
from autodrivexwheelcounts import AutoDriveXWheelCounts
from autoturnxdegrees import AutoTurnXDegrees
from autocommandgroup import AutonomousCommandGroup


from typing import Tuple, List


class MyRobot(TimedCommandRobot):
   def robotInit(self):
       """
       This function is called upon program startup and
       should be used for any initialization code.
       """


       # Instantiate (create) subsystems
       self.drivetrainSubSys: DriveTrain = DriveTrain()
       self.controller = wpilib.Joystick(0)


       self.__configure_button_bindings()


       # Configure commands
       self.configure_default_commands()


       print ("Robot Initialization (robotInit) Completed ")


   def __configure_button_bindings(self) -> None:
       button.JoystickButton(self.controller,1).onTrue(
           AutoDriveXWheelCounts(self.drivetrainSubSys, 1, 0.3)
           )


       button.JoystickButton(self.controller,2).onTrue(
           AutoTurnXDegrees(self.drivetrainSubSys, 30, 0.3)
           )


   def configure_default_commands(self) -> None:
       self.drivetrainSubSys.setDefaultCommand(
           TeleopDrive(self.drivetrainSubSys, self.controller)
           )


   def getAutonomousCommand(self) -> Command:
       return AutonomousCommandGroup(self.drivetrainSubSys)


   def autonomousInit(self):
       """This function is run once each time the robot enters autonomous mode."""


       self._auto_command = self.getAutonomousCommand()


       if self._auto_command is not None:
           self._auto_command.schedule()


       print ("Autonomous Initialization (autonomousInit) Completed ")


   def autonomousPeriodic(self):
       """This function is called periodically during autonomous."""


   def teleopInit(self):
       """This function is called once each time the robot enters teleoperated mode."""
       print ("TeleOpInit Initialization (teleopInit) Completed ")


   def teleopPeriodic(self):
       """This function is called periodically during teleoperated mode."""
       # Xaxis = self.controller.getRawAxis(0)
       # Yaxis = self.controller.getRawAxis(1)
       # print("Joystick: Forward Motion Axis: ", Yaxis, "   Turning Motion Axis: ", Xaxis )
     
