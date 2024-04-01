import cv2
import numpy as np
import matplotlib.pyplot as plt


def apply_homography(image, src_points, dst_points):

    # Convert source and destination points to numpy arrays
    src_pts = np.float32(src_points)
    dst_pts = np.float32(dst_points)

    # Compute the homography matrix
    homography_matrix, _ = cv2.findHomography(src_pts, dst_pts)

    # Apply the homography transformation to the image
    transformed_image = cv2.warpPerspective(
        image, homography_matrix, (image.shape[1], image.shape[0]))

    return transformed_image


def normalize(x):
    """
    Normalize a list of sample image data in the range of 0 to 1
    : x: List of image data.  The image shape is (32, 32, 3)
    : return: Numpy array of normalized data
    """
    return np.array((x - np.min(x)) / (np.max(x) - np.min(x)))


def homography(x, y):

    width = 996
    height = 459
    offsetX=0.1
    offsetY=0.2

    src_points = np.array([[y[0]*width, height-y[1]*height],
                           [y[2]*width, height-y[3]*height],
                           [y[4]*width, height-y[5]*height],
                          [y[6]*width, height-y[7]*height]])
    dst_points= np.array([[(y[8]-offsetX)*width, height-(y[9]-offsetY)*height],
                           [(y[8]+offsetX)*width, height-(y[9]-offsetY)*height],
                           [(y[8]-offsetX)*width, height-(y[9]+offsetY)*height],
                          [(y[8]+offsetX)*width, height-(y[9]+offsetY)*height]])

    return apply_homography(
        x, src_points, dst_points)


def main():
    pass


if __name__ == "__main__":
    main()
