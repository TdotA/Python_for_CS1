##########################################################################
# Box blur 
#
# Box blur is one of filters which can be used to blur an image. Such
# filters can be found in programs for manipulating images (Photoshop,
# GIMP, Inkscape, etc.).
# 
# Here, we will only deal with grayscale images. The image will be given
# as a matrix. Each element of the matrix will be a float between
# 0.0 (black) and 1.0 (white). This number is the color of the corresponding
# pixel. Example of a grayscale image:
# 
#     image_example = [
#         [1.00, 0.72, 0.56, 0.45],
#         [0.92, 0.64, 0.48, 0.32],
#         [0.80, 0.57, 0.42, 0.25],
#         [0.73, 0.49, 0.35, 0.21]
#     ]
##########################################################################



##########################################################################
# Write a function average_color(image, r, c) that gets a matrix which
# represents an image (see above) and numbers r and c. The function should
# return the average value of those elements of the matrix whose row number
# differs from r by at most 1 and whose column number differs from c by
# at most 1.
#
# Example (image_example is defined above):
# 
#     >>> average_color(image_example, 1, 2)
#     0.49
#     >>> average_color(image_example, 3, 0)
#     0.6475
##########################################################################



##########################################################################
# Write a function box_blur(image) which returns the new image which can
# be obtained from the given one by applying the box blur filter. The new
# image is a matrix of the same size whose element in the $i$-th row and
# $j$-th column is average_color(image, i, j).
# 
# Example (image_example is defined above):
# 
#     >>> box_blur(image_example)
#     [[0.82, 0.72, 0.5283333333333333, 0.4525],
#      [0.775, 0.6788888888888889, 0.49, 0.41333333333333333],
#      [0.6916666666666668, 0.6, 0.41444444444444445, 0.3383333333333333],
#      [0.6475, 0.56, 0.38166666666666665, 0.3075]]
##########################################################################



##########################################################################
# Write a function load_image(file_name) that reads an image from a file
# named file_name and returns it. The file has the following format:
#
# 1.00 0.72 0.56 0.45
# 0.92 0.64 0.48 0.32
# 0.80 0.57 0.42 0.25
# 0.73 0.49 0.35 0.21
#
# Example (suppose that file image.txt contains the above example):
#
#     >>> load_image('image.txt')
#     [[1.00, 0.72, 0.56, 0.45], [0.92, 0.64, 0.48, 0.32],
#      [0.80, 0.57, 0.42, 0.25], [0.73, 0.49, 0.35, 0.21]]
##########################################################################



##########################################################################
# Write a function save_image(file_name, image) that saves an image to
# a file named file_name.
#
# Example (image_example is defined above):
#
#     >>> save_image('image.txt', image_example)
#
# After this function call a file named image.txt should be created and
# it should have the following content:
#
# 1.00 0.72 0.56 0.45
# 0.92 0.64 0.48 0.32
# 0.80 0.57 0.42 0.25
# 0.73 0.49 0.35 0.21
##########################################################################


