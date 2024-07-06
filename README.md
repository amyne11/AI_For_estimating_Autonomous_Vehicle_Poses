# Features for Estimating Autonomous Vehicle Poses

Welcome to the Features for Estimating Autonomous Vehicle Poses project! This project leverages the power of artificial intelligence and computer vision to estimate the poses of an autonomous vehicle (AV) by matching visual features in a series of images captured during navigation. The project implements a visual odometry algorithm to estimate camera trajectories, a crucial aspect of autonomous navigation.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [AI and Computer Vision](#ai-and-computer-vision)
- [Development](#development)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project explores a monocular (single-camera) visual odometry (VO) solution using the KITTI dataset, widely recognized in the field of autonomous vehicle research. Visual odometry is the process of estimating a vehicle's position and orientation by analyzing the sequence of images captured by its camera. This technique is a subset of odometry and is vital for navigation in environments where GPS signals may not be reliable.

## Features

- Implementation of a visual odometry system using Python and OpenCV.
- Feature detection and matching using the Scale-Invariant Feature Transform (SIFT) algorithm.
- Distance thresholding, nearest neighbor, and nearest neighbor distance ratio feature matching strategies.
- Visualization of camera trajectories and feature matches.
- Comprehensive help messages and command-line tools for running the visual odometry system.

## Installation

1. Clone this repository to your local machine:
    ```sh
    git clone https://github.com/yourusername/autonomous-vehicle-poses.git](https://github.com/amyne11/AI_For_estimating_Autonomous_Vehicle_Poses.git
    ```

2. Install the required Python packages:
    ```sh
    pip install opencv-contrib-python
    ```

3. Download and extract the MyKITTI dataset:
    ```sh
    https://www.dropbox.com/s/w4m0iam8kgqj262/MyKITTI.zip?e=1
    # Assuming you have downloaded MyKITTI.zip
    unzip MyKITTI.zip -d ~/
    ```

## Usage

To start the visual odometry system, use the following command:
```sh
python run_odometry.py -d ~/MyKITTI view_trajectory
```
### The main window provides:

- Visualization of the car's camera view and calculated trajectory.
- Real-time updates of the current frame being processed.
- Options to inspect feature matches and detailed feature information.

### Configuring the System

You can specify different parameters and algorithms using command-line options. Refer to the comprehensive help messages for each subcommand:

```sh
python run_odometry.py -h
```

### AI and Computer Vision

#### Building the AI and Vision System

- **Feature Detection and Matching:** Implement various feature matching strategies to identify correspondences between adjacent images. Use the SIFT algorithm for robust feature detection.
- **Distance Thresholding:** Implement distance-based thresholding to filter out weak matches.
- **Nearest Neighbor Matching:** Identify the closest matches based on feature descriptors.
- **Nearest Neighbor Distance Ratio:** Enhance matching accuracy by comparing distance ratios between the nearest and second-nearest matches.

#### Core Modules and Scripts

- `run_odometry.py`: Command-line tool for running the visual odometry system.
- `visual_odometry.py`: Main module implementing the visual odometry classes and functions.
- `vision_tasks_base.py`: Abstract class defining the signatures of methods to be implemented.
- `vision_tasks.py`: Module to be completed with feature matching algorithms.

### Development

#### Feature Matching Algorithms

**Distance Thresholding (`dt`):**

- Filter matches based on a specified distance threshold.
- Example usage:
    ```sh
    python run_odometry.py get_info -a dt -t 100 150 209
    ```

**Nearest Neighbor (`nn`):**

- Match each feature to its closest neighbor in the descriptor space.
- Example usage:
    ```sh
    python run_odometry.py get_info -a nn 150 209
    ```

**Nearest Neighbor Distance Ratio (`nndr`):**

- Use the ratio of distances to the closest and second-closest matches to filter matches.
- Example usage:
    ```sh
    python run_odometry.py get_info -a nndr -t 0.8 150 209
    ```

### Testing

You can test the implemented algorithms by running the provided subcommands and inspecting the outputs. Use the `view_feature` and `get_info` subcommands to visualize and verify the feature matches.
