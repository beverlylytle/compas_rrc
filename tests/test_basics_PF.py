from abb_a042_base_lib import *
from compas.geometry import Frame
from compas_fab.backends.ros import RosClient
import re
import time

if __name__ == '__main__':

    ros = RosClient()

    abb = AbbClient(ros)
    abb.run()
    print('Connected.')

    # abb.send(ProjectInstruction('r_A032_AP1_SpeedUpdate', ['First test'], [3.3]))
    speed = 500

    abb.send_and_wait(MoveAbsJ([90, 45, 0, 1, 10, 20], [28000, -6500, -4500], speed, Zone.Z50, feedback_level=1))
    abb.send(MoveAbsJ([120, 45, 0, 1, 10, 20], [28010, -6500, -4500], speed, Zone.Z50, feedback_level=1))
    abb.send_and_wait(MoveAbsJ([90, 45, 0, 1, 10, 20], [28020, -6500, -4500], speed, Zone.Z50, feedback_level=1))

    print('Finished')

    abb.close()
    abb.terminate()

    time.sleep(3)