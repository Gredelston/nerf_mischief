# Nerf mischief

My roommate wants to hit one of his coworkers in the face with a Nerf gun whenever he [the coworker] walks by. This repo contains software to support that project.

### Prerequisites

You'll need to have [Python 3](https://www.python.org/downloads/) installed.

Once you have that, you'll need to [install opencv](https://pypi.python.org/pypi/opencv-python). This can be done easily with pip:
```
pip install opencv-python
```

## Running the code

Currently the only method you need is `facial_distance_calculator.calculate_from_image_file`. You might run the following Python script in this directory:
```
import facial_distance_calculator
print(facial_distance_calculator.calculate_from_image_file('four_people.jpg'))
```
From this you would see a list of coordinates, which represents the relative location (in pixels) of the center of each face detected in the photo.

## Future work

* Can we train this to look only for one individual?
* Need to run this on a raspi. That might be easy, but I've never done it. Is there configuration work to be done?
* There are some magic numbers in the face cascade matching. Are those parameters that can be tweaked/optimized?