# SUMediPose: A 2D-3D Pose Estimation Dataset

![Data Example](extra/data_example.gif)

We introduce a multimodal dataset comprising 3,444 videos, 2,896,943 image frames, and 3,804,413 corresponding 3D and 2D marker-based motion capture keypoint coordinates. The dataset includes 28 participants performing seven strength and conditioning actions at three different speeds. Video and image data were captured using a custom-developed multi-RGB-camera system, while the marker-based 3D data was acquired using the Vicon system and projected into the cameras' 3D and 2D spaces. The multi-RGB-camera system consists of six cameras arranged in a circular formation around the subject, offering a full 360-degree view of the scene from the same height and resulting in a diverse set of viewing angles. The recording setup was designed to allow both capture systems to record participants' movements simultaneously, synchronizing the data to provide ground truth 3D data, which was then back-projected to generate 2D pixel keypoint data for each corresponding image frame. This design enables the dataset to support both 2D and 3D pose estimation tasks. To ensure anatomical accuracy, a professional placed an extensive array of markers on each participant, adhering to industry standards.

The dataset also includes all intrinsic and extrinsic camera parameters, as well as origin axis data, necessary for performing any 3D or 2D projections. This allows the dataset to be adjusted and tailored to meet specific research or application needs.

## How To Use The Dataset
The dataset contains multile files and file types such as images, keypoint coordiates, subject data, etc. The *SUMediPose.csv* file is provided to aid in the use of the various data.
### SUMediPose.csv 
CSV file, which links the each image frame in the dataset to their corrisponding keypoint data, contains the following data:
| Field         | Description                                                                                                           |
|---------------|-----------------------------------------------------------------------------------------------------------------------|
| id            | Unique ID of the image frame within the larger dataset                                                                |
| cam           | Specifies the camera that generated the image, ranging from C1 to C6                                                  |
| subject       | Identifies the subject within the image frame                                                                         |
| action        | Identifies the action being performed by the subject within the image                                                 |
| speed         | Identifies the speed at which the subject is performing an action within the image                                    |
| index         | Index value of the 3D and 2D data that corresponds directly to this specific image frame                              |
| path          | Relative path of the image frame within the main dataset folder                                                       |
| bbx           | List of values representing the bounding box of the detected subject within the image frame: [x, y, width, height]    |
| internal_path | Relative path of the internal 3D and 2D data file within the main dataset folder; points to data relevant to the image |
| wcs_path      | Relative path of the 3D WCS data file within the main dataset folder; points to data relevant to the image            |


## Code

