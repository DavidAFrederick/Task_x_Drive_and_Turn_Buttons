import commands2
from commands2 import PrintCommand 
from autodrivexseconds import AutoDriveXSeconds
from autoturnxdegrees import AutoTurnXDegrees
from waitxseconds import WaitXSeconds
from autodrivexwheelcounts import AutoDriveXWheelCounts

from drivetrainsubsys import DriveTrain
from ledsubsystem import LEDSubsystem

from setledred import SetLEDRed
from setledblue import SetLEDBlue


class CommandGroup1(commands2.SequentialCommandGroup):
   def __init__(self, drivetrainsubsys: DriveTrain, ledsubsystem: LEDSubsystem) -> None:
       super().__init__()
       print ("Running Command Group 1")
       wheelCount = 10   # Wheel count for the side of the square
       self.drivetrainsubsys = drivetrainsubsys
       self.ledsubsystem = ledsubsystem


       self.addCommands(SetLEDRed(self.ledsubsystem)) 

       self.addCommands(AutoDriveXWheelCounts(self.drivetrainsubsys, wheelCount, 0.3))  
    #    self.addCommands(WaitXSeconds(self.drivetrainsubsys,1))
    #    self.addCommands(AutoTurnXDegrees(self.drivetrainsubsys,-90, 0.3))  


       self.addCommands(SetLEDBlue(self.ledsubsystem)) 

       self.addCommands(PrintCommand("Done Command Group 1"))