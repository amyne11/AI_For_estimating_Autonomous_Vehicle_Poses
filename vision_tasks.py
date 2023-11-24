#!/usr/bin/env python3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""Sample code for Comp24011 SLAM lab solution

NB: The default code in non-functional; it simply avoids type errors
"""

__author__ = "y54754ae"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import cv2
import sys

from vision_tasks_base import VisionTasksBase

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class VisionTasks(VisionTasksBase):
    def __init__(self, *params):
        """Initialise instance by passing arguments to super class"""
        super().__init__(*params)

    def dt(self, des1, des2, threshold):
        """Implements feature matching based on distance thresholding

        :param des1: descriptors for the previous image (query)
        :type des1:  list
        :param des2: descriptors for the current image (train)
        :type des2:  list
        :param threshold: threshold value
        :type threshold:  float

        :return: matches for descriptors
        :rtype:  list
        """
        try:
            # Validate descriptors
            if des1 is None or des2 is None:
                print("Descriptors are None")
                return []

            bf = cv2.BFMatcher()
            knn_matches = bf.knnMatch(des1, des2, k=1500)
            good_matches = []

            for match_list in knn_matches:
                for match in match_list:
                    if match and match.distance <= threshold:
                        good_matches.append(match)

            return good_matches
        except Exception as e:
            print(f"An error occurred in dt method: {e}")
            return []
                


    
        

        


                
        

        

    def nn(self, des1, des2, threshold=None):
        """Implements feature matching based on nearest neighbour

        :param des1: descriptors for the previous image (query)
        :type des1:  list
        :param des2: descriptors for the current image (train)
        :type des2:  list
        :param threshold: threshold value
        :type threshold:  float or None

        :return: matches for descriptors
        :rtype:  list
        """
        bf = cv2.BFMatcher()
        knn_matches = bf.knnMatch(des1, des2, k=1)
        
        nn_matches=[]
        for match_nn in knn_matches:
            if match_nn:
                m=match_nn[0]
                if threshold is None or m.distance<threshold:
                    nn_matches.append(m)
        return nn_matches

    def nndr(self, des1, des2, threshold):
        """Implements feature matching based on nearest neighbour distance ratio

        :param des1: descriptors for the previous image (query)
        :type des1:  list
        :param des2: descriptors for the current image (train)
        :type des2:  list
        :param threshold: threshold value
        :type threshold:  float

        :return: matches for descriptors
        :rtype:  list
        """
        return []

    def matching_info(self, kp1, kp2, feature_matches):
        """Collects information about the matches of some feature

        :param kp1: keypoints for the previous image (query)
        :type kp1:  list
        :param kp2: keypoints for the current image (train)
        :type kp2:  list
        :param feature_matches: matches for the feature
        :type feature_matches:  list

        :return: coordinate of feature in previous image,
                 coordinates for feature matches in current image,
                 distances for feature matches in current image
        :rtype:  tuple, list, list
        """
        if not feature_matches:
            return (0, 0), [], []
        if isinstance(feature_matches, cv2.DMatch):
            feature_matches = [feature_matches]
        

        
        curr_coords=[]
        distances=[]
        prev_coord=None
        
                
        
        
        for match in feature_matches:
            prev_kp = kp1[match.queryIdx]
            if prev_coord is None:
                prev_coord = (int(prev_kp.pt[0]), int(prev_kp.pt[1]))


            
                


            curr_kp = kp2[match.trainIdx]
            curr_coords.append((int(curr_kp.pt[0]), int(curr_kp.pt[1])))
            distances.append(match.distance)
            


        return prev_coord, curr_coords, distances

        
        
        
   
    

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
    import run_odometry
    run_odometry.main(sys.argv[1:])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# vim:set et sw=4 ts=4:
