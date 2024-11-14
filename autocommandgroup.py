import commands2
from commands2 import PrintCommand 
from autodrivexseconds import AutoDriveXSeconds
from autoturnxdegrees import AutoTurnXDegrees
from waitxseconds import WaitXSeconds
from drivetrainsubsys import DriveTrain
from autodrivexwheelcounts import AutoDriveXWheelCounts


class AutonomousCommandGroup(commands2.SequentialCommandGroup):
   def __init__(self, drivetrainsubsys: DriveTrain) -> None:
       super().__init__()
       print ("Within Autonomous SequentialCommand Group")
       wheelCount = 10   # Wheel count for the side of the square
       self.drivetrainsubsys = drivetrainsubsys
       self.addCommands(AutoDriveXWheelCounts(self.drivetrainsubsys, wheelCount, 0.3))  
       self.addCommands(WaitXSeconds(self.drivetrainsubsys,1))
       self.addCommands(AutoTurnXDegrees(self.drivetrainsubsys,-90, 0.3))  


       self.addCommands(AutoDriveXWheelCounts(self.drivetrainsubsys, wheelCount, 0.3))  
       self.addCommands(WaitXSeconds(self.drivetrainsubsys,1))
       self.addCommands(AutoTurnXDegrees(self.drivetrainsubsys,-90, 0.3))


       self.addCommands(AutoDriveXWheelCounts(self.drivetrainsubsys, wheelCount, 0.3))  
       self.addCommands(WaitXSeconds(self.drivetrainsubsys,1))
       self.addCommands(AutoTurnXDegrees(self.drivetrainsubsys,-90, 0.3))


       self.addCommands(AutoDriveXWheelCounts(self.drivetrainsubsys, wheelCount, 0.3))  
       self.addCommands(WaitXSeconds(self.drivetrainsubsys,1))
       self.addCommands(AutoTurnXDegrees(self.drivetrainsubsys,-90, 0.3))


       self.addCommands(PrintCommand("Done"))