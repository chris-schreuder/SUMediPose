import numpy as np
import linalg

def DLT_2_cameras(imgpoints_Origin, imgpoints_Pair1, projMatr_Origin, projMatr_Pair1):
    points_3d_list = []
    for points_origin, points_pair1 in zip(imgpoints_Origin, imgpoints_Pair1):
        point_origin = np.array(points_origin)
        point_pair1 = np.array(points_pair1)

        A = [point_origin[1]*projMatr_Origin[2,:] - projMatr_Origin[1,:],
            projMatr_Origin[0,:] - point_origin[0]*projMatr_Origin[2,:],
            point_pair1[1]*projMatr_Pair1[2,:] - projMatr_Pair1[1,:],
            projMatr_Pair1[0,:] - point_pair1[0]*projMatr_Pair1[2,:],
            ]

        A = np.array(A) 
        B = A.transpose() @ A
        U, s, Vh = linalg.svd(B, full_matrices = False)
        
        points4D_homogeneous = Vh[-1,0:3]/Vh[-1,3]
        points_3d_list.append(points4D_homogeneous[:3].T)

    return points_3d_list

def DLT_3_cameras(imgpoints_Origin, imgpoints_Pair1, imgpoints_Pair2, projMatr_Origin, projMatr_Pair1, projMatr_Pair2):
    points_3d_list = []
    for points_origin, points_pair1, points_pair2 in zip(imgpoints_Origin, imgpoints_Pair1, imgpoints_Pair2):
        point_origin = np.array(points_origin)
        point_pair1 = np.array(points_pair1)
        point_pair2 = np.array(points_pair2)

        A = [point_origin[1]*projMatr_Origin[2,:] - projMatr_Origin[1,:],
            projMatr_Origin[0,:] - point_origin[0]*projMatr_Origin[2,:],
            point_pair1[1]*projMatr_Pair1[2,:] - projMatr_Pair1[1,:],
            projMatr_Pair1[0,:] - point_pair1[0]*projMatr_Pair1[2,:],
            point_pair2[1]*projMatr_Pair2[2,:] - projMatr_Pair2[1,:],
            projMatr_Pair2[0,:] - point_pair2[0]*projMatr_Pair2[2,:]
            ]

        A = np.array(A) 
        B = A.transpose() @ A
        U, s, Vh = linalg.svd(B, full_matrices = False)
        
        points4D_homogeneous = Vh[-1,0:3]/Vh[-1,3]
        points_3d_list.append(points4D_homogeneous[:3].T)

    return points_3d_list

def projectInternal(M, xyz):
    xyz = np.array([[xyz[0], xyz[1], xyz[2], 1]], dtype=object).T
    internal_xyz = M @ xyz
    internal_xyz[:3].flatten()
    internal_xyz = np.squeeze(internal_xyz)
    internal_xyz =np.squeeze(internal_xyz)
    return internal_xyz[:3]

def projectInternal(R, t, xyz):
        a = np.array([[0, 0, 0]])
        b = np.array([[1]])
        xyz = np.array([[xyz[0], xyz[1], xyz[2], 1]], dtype=object).T
        M = np.vstack((np.hstack((R, t)), np.hstack((a, b))))
        internal_xyz = M @ xyz
        internal_xyz[:3].flatten()
        internal_xyz = np.squeeze(internal_xyz)
        internal_xyz =np.squeeze(internal_xyz)
        return internal_xyz[:3]

def projectPixel(M, xyz):
        xyz = np.array([[xyz[0], xyz[1], xyz[2], 1]], dtype=object).T
        image_xy = M @ xyz
        image_xy[:3].flatten()
        image_xy /= image_xy[2]
        image_xy = np.squeeze(image_xy)
        return image_xy[0:2]