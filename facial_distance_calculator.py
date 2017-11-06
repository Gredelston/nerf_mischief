import math
import sys

import cv2

# Haar Cascade files are like templates for what faces look like.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

###############################################################################
# calculate_from_image_file
#
# Description:
#		Finds all faces in an image, and tells where their centers are.
#
# Parameters:
#		img_location: The file location of the image. (string, required)
#		show_images: Whether or not to display the image, with bounding boxes
#				for each face, and lines to the image center.
#				If not specified, defaults to false. (boolean, optional)
#
# Return value:
#		A list of (dx, dy) tuples, each representing the distance (in pixels)
#		from the center of the image to the center of a face found.
###############################################################################
def calculate_from_image_file(img_location, show_images=False):
	img = load_image(img_location)
	faces = find_faces(img)
	face_centers = calculate_bounding_box_centers(faces)
	face_distances = calculate_distances_from_center(img, face_centers)

	if (show_images):
		draw_bounding_boxes(img, faces)
		draw_lines_to_center(img, face_centers)
		show_image(img)

	return face_distances

###############################################################################
# load_image
#
# Description:
#		Attempts to load an image file.
#		The program halts if image cannot be found.
#
# Parameters:
#		img_location: The file location of the image. (string, required)
#
# Return value:
#		A cv2.Image object containing the supplied image.
###############################################################################
def load_image(img_location):
	img = cv2.imread(img_location)
	if img is None:
		sys.exit('Failed to load image ' + img_location) 
	return img

###############################################################################
# find_faces
#
# Description:
#		Given an opencv image file, finds bounding boxes for all faces.
#
# Parameters:
#		img: the opencv image file (cv2.Image, required)
#
# Return value:
# 		A list of tuples (x,y,w,h) representing bounding boxes for each face.
#		x and y refer to the top-left corner of the face's bounding box,
#			in pixels.
#			(Note: (0,0) is at the top-left corner of the image.)
#		w and h refer to the width and height of the bounding box, in pixels.
###############################################################################
def find_faces(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	return face_cascade.detectMultiScale(gray, 1.3, 5)

###############################################################################
# calculate_bounding_box_centers
#
# Description:
#		Finds the centers of a list of bounding boxes.
#
# Parameters:
#		bounding_boxes: A list of (x,y,w,h) tuples, such as is returned by
#			find_faces(). (list, required)
#
# Return value:
#		A list of tuples (x,y) representing the centers of each of those
#		bounding boxes.
###############################################################################
def calculate_bounding_box_centers(bounding_boxes):
	return [(int(x+(w/2)), int(y+(h/2))) for (x,y,w,h) in bounding_boxes]

###############################################################################
# calculate_distances_from_center
#
# Description:
#		Finds the distances from a bunch of points to the center of an image.
#
# Parameters:
#		img: An opencv image. (cv2.Image, required)
#		points: A list of (x,y) coordinates. (list, required)
#
# Return value:
#		A list of tuples (dx,dy) representing the distance from the center
#		of the image for each submitted coordinate.
###############################################################################
def calculate_distances_from_center(img, points):
	(img_height, img_width) = img.shape[:2]
	(img_center_x, img_center_y) = ( int(img_width / 2), int(img_height / 2) )
	return [(img_center_x - x, img_center_y - y) for (x, y) in points]

###############################################################################
# draw_bounding_boxes
#
# Description:
#		Draws a list of bounding boxes.
#
# Parameters:
#		bounding_boxes: A list of (x,y,w,h) tuples defining bounding boxes,
#		such as is returned by find_faces(). (list of tuples, required)
#
# Return value:
#		Not meaningful.
###############################################################################
def draw_bounding_boxes(img, bounding_boxes):
	for (x,y,w,h) in bounding_boxes:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

###############################################################################
# draw_lines_to_center
#
# Description:
#		Draws lines from the center of an image to a list of points.
#
# Parameters:
#		img: An opencv image. (cv2.Image, required)
#		bounding_boxes: A list of (x,y) coordinates. (list of tuples, required)
#
# Return value:
#		Not meaningful.
###############################################################################
def draw_lines_to_center(img, points):
	(img_height, img_width) = img.shape[:2]
	(img_center_x, img_center_y) = (int(img_width/2), int(img_height/2))
	for (x, y) in points:
		cv2.line(img, (x, y), (img_center_x, img_center_y), (0,0,255), 2)

###############################################################################
# show_image
#
# Description:
#		Displays an image, waits until you press a button, and then clears it.
#
# Parameters:
#		img: An opencv image. (cv2.Image, required)
#
# Return value:
#		Not meaningful.
###############################################################################
def show_image(img):
	cv2.imshow('img',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

# test it out if we're running this file directly (not importing)
if __name__ == '__main__':
	print(calculate_from_image_file('four_people.jpg'))