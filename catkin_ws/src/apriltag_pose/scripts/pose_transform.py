#!/usr/bin/env python

import numpy as np


def cam2_transform(result):
    poses = []
    for i in range(0, len(result), 4):
        # print(f'detection {result[i + 1]}') # list by order
        poses.append(result[i + 1])
    pose_tag02cam = poses[0]
    pose_tag02cam_inv = np.linalg.inv(pose_tag02cam)
    # remove first pose
    del (poses[0])
    pts = []
    for i in range(len(poses)):
        p_cam = poses[i][0:3, 3]
        p_cam = np.append(p_cam, [1])
        pts.append(p_cam)
    trans_tag = []
    for i in range(len(pts)):
        p_tag = np.dot(pose_tag02cam_inv, pts[i])
        trans_tag.append(p_tag)
        # print(p_tag)
    return trans_tag


def cam2marker_transform(result):
    # print(f'len result {len(result)}')
    poses = []
    for i in range(0, len(result), 4):
        # print(f'detection {result[i + 1]}') # list by order
        poses.append(result[i + 1])
    # test pose transform
    # SEtag_cam default is id = 0
    # we get relevant transform
    pose_tag02cam = poses[0]
    pose_cam2tag0 = np.linalg.inv(pose_tag02cam)
    # vali_mat = np.dot(pose_cam2tag0, pose_tag02cam)
    # remove first pose
    del (poses[0])
    pose_tagn2tag0 = []
    for i in range(len(poses)):
        mul_pose = np.dot(pose_cam2tag0, poses[i])
        pose_tagn2tag0.append(mul_pose)

    # get translation result
    trans = []
    for i in range(len(pose_tagn2tag0)):
        # print(pose_tagn2tag0[i])
        tran = pose_tagn2tag0[i][0:3, 3]
        trans.append(tran)
        # print(f'tran - {tran}')

    return trans
    # [detection, pose, e0, e1]
    # pose = result[0]
    # print(f'pose {pose.tostring(indent=2)}')
