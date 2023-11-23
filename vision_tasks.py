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
        bf = cv2.BFMatcher()
        knn_matches = bf.knnMatch(des1, des2, k=10)
        dt_matches=[]
       # for i, match_set in enumerate(knn_matches):
        #    print(f"Matches for descriptor {i}:")
            #for match in match_set:
                #print(f" - QueryIdx: {match.queryIdx}, TrainIdx: {match.trainIdx}, Distance: {match.distance}")
        

        for match_list in knn_matches:
            for fm in match_list:
                if fm.distance<threshold:
                    dt_matches.append(fm)
        # After you have populated dt_matches with the filtered matches

       # print("Filtered Matches:")
       # for match in dt_matches:
          #  print(f" - QueryIdx: {match.queryIdx}, TrainIdx: {match.trainIdx}, Distance: {match.distance}")


        return dt_matches
                


    
        

        


                
        

        

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
        return []

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
        

        
        curr_coords=[]
        distances=[]
        
        prev_kp = kp1[feature_matches.queryIdx]
        prev_coord = (int(prev_kp.pt[0]), int(prev_kp.pt[1]))
        if isinstance(feature_matches, cv2.DMatch):
            feature_matches = [feature_matches]
        for match in feature_matches:

            curr_kp = kp2[match.trainIdx]
            curr_coord = [int(curr_kp.pt[0]), int(curr_kp.pt[1])]
            curr_coords.append(curr_coord)
            distances.append(match.distance)
            print(curr_coords)
            print(distances)


        return prev_coord, curr_coord, distances

        
        
        
   #     for match in feature_matches:
    #        curr_kp=kp2[match.trainIdx]
     #       x_coord_curr, y_coord_curr = int(curr_kp.pt[0]), int(curr_kp.pt[1])
      #      curr_coord.append((x_coord_curr,y_coord_curr))
       #     distances.append(match.distance)
        #    print(prev_coord)
         #   print(curr_coord)
          #  print(distances)






        
        
        return prev_coord, curr_coord, distances
    

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def convert_to_coords(pt):
    # Convert the point to integer coordinates
        return (int(pt[0]), int(pt[1]))
if __name__ == '__main__':
    import run_odometry
    run_odometry.main(sys.argv[1:])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# vim:set et sw=4 ts=4:
