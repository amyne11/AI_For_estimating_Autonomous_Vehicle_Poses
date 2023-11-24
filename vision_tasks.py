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
                filtered_list = [match for match in match_list if match.distance < threshold]
                good_matches.append(filtered_list)

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
        filtered_matches = []

        for match_list in knn_matches:
            # Since k=1, each match_list contains a single match
            if match_list:
                closest_match = match_list[0]
                if closest_match and (threshold is None or closest_match.distance < threshold):
                    filtered_matches.append([closest_match])
                else:
                    filtered_matches.append([])  # Append an empty list if no match meets the threshold

        return filtered_matches

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
        bf = cv2.BFMatcher()
        knn_matches = bf.knnMatch(des1, des2, k=2)
        nndr_filtered_matches = []

        for match_pair in knn_matches:
            if len(match_pair) == 2:
                m, n = match_pair
                if m.distance < threshold * n.distance:
                    nndr_filtered_matches.append([m])  # Append as a list
                else:
                    nndr_filtered_matches.append([])  # Append an empty list if the match does not meet the criteria
            else:
                nndr_filtered_matches.append([])  # Append an empty list if there are not enough matches

        return nndr_filtered_matches

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
