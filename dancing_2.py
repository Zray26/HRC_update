#!/usr/bin/env python
import rospy
import sys
import copy
import tf
from hrclib_client_v6 import odyssey_Interface
import geometry_msgs.msg 
import math
import moveit_commander
from movo_action_clients.gripper_action_client import GripperActionClient
from moveit_msgs.msg import PlaceLocation, MoveItErrorCodes
from moveit_python import MoveGroupInterface, PlanningSceneInterface
import time
# import zl_ods_contact

_upper_body_joints = ["right_shoulder_pan_joint",
                      "right_shoulder_lift_joint",
                      "right_arm_half_joint",
                      "right_elbow_joint",
                      "right_wrist_spherical_1_joint",
                      "right_wrist_spherical_2_joint",
                      "right_wrist_3_joint",
                      "left_shoulder_pan_joint",
                      "left_shoulder_lift_joint",
                      "left_arm_half_joint",
                      "left_elbow_joint",
                      "left_wrist_spherical_1_joint",
                      "left_wrist_spherical_2_joint",
                      "left_wrist_3_joint",
                      "linear_joint",
                      "pan_joint",
                      "tilt_joint"]
                      
# Head looking straight
default_pose_tucked = [-1.595, -1.5, 0.1, -2.612, 0.0, 0.496, -1.69,
                       1.595, 1.5, -0.1, 2.612, 0.0, -0.496, 1.69,
                       0.25, 0, 0]
pose1 = [0, -1.5, 0.1, -1.57, 0.0, 1.57, -1.69,
                       0, 1.5, -0.1, 1.57, 0.0, -1.57, 1.69,
                       0.25, 0, 0]

class move_to_tuck(object):
    def __init__(self):
        _upper_body_joints = ["right_shoulder_pan_joint",
                      "right_shoulder_lift_joint",
                      "right_arm_half_joint",
                      "right_elbow_joint",
                      "right_wrist_spherical_1_joint",
                      "right_wrist_spherical_2_joint",
                      "right_wrist_3_joint",
                      "left_shoulder_pan_joint",
                      "left_shoulder_lift_joint",
                      "left_arm_half_joint",
                      "left_elbow_joint",
                      "left_wrist_spherical_1_joint",
                      "left_wrist_spherical_2_joint",
                      "left_wrist_3_joint",
                      "linear_joint",
                      "pan_joint",
                      "tilt_joint"]
                      
# Head looking straight
        default_pose_tucked = [-1.595, -1.5, 0.1, -2.612, 0.0, 0.496, -1.69,
                            1.595, 1.5, -0.1, 2.612, 0.0, -0.496, 1.69,
                            0.25, 0, 0]
        lgripper = GripperActionClient('left')
        rgripper = GripperActionClient('right')
        gripper_closed = 0.00
        gripper_open = 0.165
        
        larm_group = moveit_commander.MoveGroupCommander("left_arm")
        rarm_group = moveit_commander.MoveGroupCommander("right_arm")
        upper_body = moveit_commander.MoveGroupCommander("upper_body")

        move_group = MoveGroupInterface("upper_body", "base_link")
        lmove_group = MoveGroupInterface("left_arm", "base_link")
        rmove_group = MoveGroupInterface("right_arm", "base_link")
        self._upper_body_joints=_upper_body_joints
        self.default_pose_tucked=default_pose_tucked
        self.move_group=move_group

    def move_to_initial_pose(self):


        print("Done spinning up MoveIt!")

        
        while not rospy.is_shutdown():
            print("doing L0_goto_upper_body_joints")
            result = self.move_group.moveToJointPosition(self._upper_body_joints, self.default_pose_tucked, 0.005, wait=True)

            print("error code: ", result.error_code.val)
            if result.error_code.val == MoveItErrorCodes.SUCCESS:
                break

        print("successful")

    def __del__(self):
        pass
#temp_pickbolt_client.marker_CallBack()

if __name__=="__main__":
    rospy.init_node("Test_all",
                    anonymous=False)
    moveit_commander.roscpp_initialize(sys.argv)
    scene = moveit_commander.PlanningSceneInterface()
    # tuck = move_to_tuck()
    # tuck.move_to_initial_pose()
    # del tuck
    moveit_commander.roscpp_initialize(sys.argv)

    scene = moveit_commander.PlanningSceneInterface()

    lgripper = GripperActionClient('left')
    rgripper = GripperActionClient('right')
    gripper_closed = 0.00
    gripper_open = 0.165
    
    larm_group = moveit_commander.MoveGroupCommander("left_arm")
    rarm_group = moveit_commander.MoveGroupCommander("right_arm")
    upper_body = moveit_commander.MoveGroupCommander("upper_body")

    move_group = MoveGroupInterface("upper_body", "base_link")
    lmove_group = MoveGroupInterface("left_arm", "base_link")
    rmove_group = MoveGroupInterface("right_arm", "base_link")

    print("Done spinning up MoveIt!")
    # upper_body.go(joints=[])
    # larm_group.
#pose move to tuck
    while not rospy.is_shutdown():
        print("doing L0_goto_upper_body_joints")
        result = move_group.moveToJointPosition(_upper_body_joints, default_pose_tucked, 0.005, wait=True)


        print("error code: ", result.error_code.val)
        if result.error_code.val == MoveItErrorCodes.SUCCESS:
            break
    raw_input()
#pose 1
    while not rospy.is_shutdown():
        print("doing L0_goto_upper_body_joints")
        result = move_group.moveToJointPosition(_upper_body_joints, pose1, 0.005, wait=True)


        print("error code: ", result.error_code.val)
        if result.error_code.val == MoveItErrorCodes.SUCCESS:
            break

    # print("successful")
    # time.sleep(3)
    ods = odyssey_Interface()
    # ods._L0_dual_jp_move_safe_relate(
    #     jp_r=[0, 0, 0, 0, 0, 0, 0], rmaxforce=[20, 20, 20, 20, 20, 20],
    #     jp_l=[0, 0, 0, 0, 0, 0, 0], lmaxforce=[20, 20, 20, 20, 20, 20],
    #     duration=1000)

    # ods._L0_dual_jp_move_safe_relate(
    #     jp_r=[0.2, 0, 0, 0.1, 0, 0, 0], rmaxforce=[20, 20, 20, 20, 20, 20],
    #     jp_l=[-0.2, 0, 0, -0.1, 0, 0, 0], lmaxforce=[20, 20, 20, 20, 20, 20],
    #     duration=2) #p1
    # raw_input()
    # #####original#####
    # ods._L0_dual_jp_move_safe_relate(
    #     jp_r=[0.495, 0, 0, 0.515, 0, 0.104, 0], rmaxforce=[20, 20, 20, 20, 20, 20],
    #     jp_l=[-0.495, 0, 0, -0.515, 0, -0.104, 0], lmaxforce=[20, 20, 20, 20, 20, 20],
    #     duration=1.5) #p1
        #####original#####
    raw_input()
    ods._L0_dual_jp_move_safe_relate(
        jp_r=[0, 0, 0, 0, -2.5 * math.pi,0, 0], rmaxforce=[20, 20, 20, 20, 20, 20],
        jp_l=[0, 0, 0, 0, 2.5 * math.pi, 0, 0], lmaxforce=[20, 20, 20, 20, 20, 20],
        duration=12) #p1
    raw_input()
    ods._L0_dual_jp_move_safe_relate(
        jp_r=[0, 0, 0, 0, 0,0, -2 * math.pi], rmaxforce=[20, 20, 20, 20, 20, 20],
        jp_l=[0, 0, 0, 0, 0, 0, 2 * math.pi], lmaxforce=[20, 20, 20, 20, 20, 20],
        duration=5) #p1
    raw_input()
    ods._L0_dual_jp_move_safe_relate(
        jp_r=[0, 0, 0, 0, 0.5 * math.pi,0, 0], rmaxforce=[20, 20, 20, 20, 20, 20],
        jp_l=[0, 0, 0, 0, -0.5 * math.pi, 0, 0], lmaxforce=[20, 20, 20, 20, 20, 20],
        duration=5) #p1
    raw_input()
    ods._L0_dual_jp_move_safe_relate(
        jp_r=[- 0.35 * math.pi, 0, -0.12 *math.pi, 0, 0 ,0, 0], rmaxforce=[20, 20, 20, 20, 20, 20],
        jp_l=[0.35 *math.pi, 0, 0.12 *math.pi, 0, 0, 0, 0], lmaxforce=[20, 20, 20, 20, 20, 20],
        duration=5) #p1
    # time.sleep(5)
    raw_input()
    ods._L0_dual_jp_move_safe_relate(
        jp_r=[0, 0, 0, 0, 2.8 * math.pi,0, 0], rmaxforce=[20, 20, 20, 20, 20, 20],
        jp_l=[0, 0, 0, 0, -2.8 * math.pi, 0, 0], lmaxforce=[20, 20, 20, 20, 20, 20],
        duration=12) #p1

        # for left arm #
    raw_input()
    ods._L0_dual_jp_move_safe_relate(
        jp_r=[0, 0, 0.35 * math.pi, 0, 0, - 0.5 * math.pi, 0], rmaxforce=[20, 20, 20, 20, 20, 20],
        jp_l=[0, 0, 0, 0, 0, 0, 0], lmaxforce=[20, 20, 20, 20, 20, 20],
        duration=6) #p1
    raw_input()
    ods._L0_dual_jp_move_safe_relate(
        jp_r=[0.35 * math.pi, 0, 0, 0, 0, 0, 0], rmaxforce=[20, 20, 20, 20, 20, 20],
        jp_l=[0, 0, 0, 0, 0, 0, 0], lmaxforce=[20, 20, 20, 20, 20, 20],
        duration=12) #p1
    raw_input()
    ods._L0_dual_jp_move_safe_relate(
        jp_r=[0, 0, -0.35 *math.pi, 0, 0, 0, 0], rmaxforce=[20, 20, 20, 20, 20, 20],
        jp_l=[0, 0, 0, 0, 0, 0, 0], lmaxforce=[20, 20, 20, 20, 20, 20],
        duration=6) #p1
    raw_input()
    ods._L0_dual_jp_move_safe_relate(
        jp_r=[0.1 * math.pi, 0, 0.12 *math.pi, 0, 0, 0, 0], rmaxforce=[20, 20, 20, 20, 20, 20],
        jp_l=[0, 0, 0, 0, 0, 0, 0], lmaxforce=[20, 20, 20, 20, 20, 20],
        duration=12) #p1
    raw_input()
    ods._L0_dual_jp_move_safe_relate(
        jp_r=[-0.1 * math.pi, 0, -0.5 *math.pi, 0, 0, 0, 0], rmaxforce=[20, 20, 20, 20, 20, 20],
        jp_l=[0, 0, 0, 0, 0, 0, 0], lmaxforce=[20, 20, 20, 20, 20, 20],
        duration=12) #p1

        # for right arm #
    raw_input()
    ods._L0_dual_jp_move_safe_relate(
        jp_r=[0, 0,0,0,0,0,0], rmaxforce=[20, 20, 20, 20, 20, 20],
        jp_l=[0, 0, -0.35 * math.pi, 0, 0, 0.5 * math.pi, 0], lmaxforce=[20, 20, 20, 20, 20, 20],
        duration=6) #p1
    raw_input()
    ods._L0_dual_jp_move_safe_relate(
        jp_r=[0,0,0,0,0,0,0], rmaxforce=[20, 20, 20, 20, 20, 20],
        jp_l=[-0.35 * math.pi, 0, 0, 0, 0, 0, 0], lmaxforce=[20, 20, 20, 20, 20, 20],
        duration=12) #p1
    raw_input()
    ods._L0_dual_jp_move_safe_relate(
        jp_r=[0,0,0,0,0,0,0], rmaxforce=[20, 20, 20, 20, 20, 20],
        jp_l=[0, 0, 0.35 *math.pi, 0, 0, 0, 0], lmaxforce=[20, 20, 20, 20, 20, 20],
        duration=6) #p1
    raw_input()
    ods._L0_dual_jp_move_safe_relate(
        jp_r=[0,0,0,0,0,0,0], rmaxforce=[20, 20, 20, 20, 20, 20],
        jp_l=[-0.1 * math.pi, 0, -0.12 *math.pi, 0, 0, 0, 0], lmaxforce=[20, 20, 20, 20, 20, 20],
        duration=12) #p1
    raw_input()
    ods._L0_dual_jp_move_safe_relate(
        jp_r=[0,0,0,0,0,0,0], rmaxforce=[20, 20, 20, 20, 20, 20],
        jp_l=[0.1 * math.pi, 0, 0.5 *math.pi, 0, 0, 0, 0], lmaxforce=[20, 20, 20, 20, 20, 20],
        duration=12) #p1

        #inverse
    ods._L0_dual_jp_move_safe_relate(
        jp_r=[0.1 * math.pi, 0, 0.5 *math.pi, 0, 0, 0, 0], rmaxforce=[20, 20, 20, 20, 20, 20],
        jp_l=[-0.1 * math.pi, 0, -0.5 *math.pi, 0, 0, 0, 0], lmaxforce=[20, 20, 20, 20, 20, 20],
        duration=12) #p1
    raw_input()
    ods._L0_dual_jp_move_safe_relate(
        jp_r=[-0.1 * math.pi, 0, -0.12 *math.pi, 0, 0, 0, 0], rmaxforce=[20, 20, 20, 20, 20, 20],
        jp_l=[0.1 * math.pi, 0, 0.12 *math.pi, 0, 0, 0, 0], lmaxforce=[20, 20, 20, 20, 20, 20],
        duration=12) #p1
    raw_input()
    ods._L0_dual_jp_move_safe_relate(
        jp_r=[0, 0, 0.35 *math.pi, 0, 0, 0, 0], rmaxforce=[20, 20, 20, 20, 20, 20],
        jp_l=[0, 0, -0.35 *math.pi, 0, 0, 0, 0], lmaxforce=[20, 20, 20, 20, 20, 20],
        duration=6) #p1
    raw_input()
    ods._L0_dual_jp_move_safe_relate(
        jp_r=[-0.35 * math.pi, 0, -0.35 * math.pi, 0, 0, 0.5 * math.pi, 0], rmaxforce=[20, 20, 20, 20, 20, 20],
        jp_l=[0.35 * math.pi, 0, 0.35 * math.pi, 0, 0, -0.5 * math.pi, 0], lmaxforce=[20, 20, 20, 20, 20, 20],
        duration=12) #p1