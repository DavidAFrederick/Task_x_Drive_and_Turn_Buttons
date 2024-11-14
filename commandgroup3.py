import commands2
from commands2 import PrintCommand 

from autodrivexseconds import AutoDriveXSeconds
from autodrivexwheelcounts import AutoDriveXWheelCounts
from autoturnxdegrees import AutoTurnXDegrees
from waitxseconds import WaitXSeconds
from setledgreen import SetLEDGreen
from setledblue import SetLEDBlue
from setledred import SetLEDRed

from drivetrainsubsys import DriveTrain
from ledsubsystem import LEDSubsystem


class CommandGroup3(commands2.SequentialCommandGroup):
   def __init__(self, drivetrainsubsys: DriveTrain, ledsubsystem: LEDSubsystem) -> None:
       super().__init__()
       print ("Running Command Group 3")
       wheelCount = 10   # Wheel count for the side of the square
       self.drivetrainsubsys = drivetrainsubsys
       self.ledsubsystem = ledsubsystem



      # Turn the LEDs green
       self.addCommands(SetLEDRed(self.ledsubsystem)) 

      #  self.addCommands(AutoDriveXWheelCounts(self.drivetrainsubsys, wheelCount, 0.3))  
       self.addCommands(WaitXSeconds(self.drivetrainsubsys,1))
      #  self.addCommands(AutoTurnXDegrees(self.drivetrainsubsys,-90, 0.3))  

       self.addCommands(SetLEDBlue(self.ledsubsystem)) 
       self.addCommands(PrintCommand("Done Command Group 3"))