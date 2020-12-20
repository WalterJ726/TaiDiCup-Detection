######## Image Object Detection Using Tensorflow-trained Classifier #########
#
# Author: Evan Juras
# Date: 1/15/18
# Description: 
# This program uses a TensorFlow-trained classifier to perform object detection.
# It loads the classifier uses it to perform object detection on an image.
# It draws boxes and scores around the objects of interest in the image.

## Some of the code is copied from Google's example at
## https://github.com/tensorflow/models/blob/master/research/object_detection/object_detection_tutorial.ipynb

## and some is copied from Dat Tran's example at
## https://github.com/datitran/object_detector_app/blob/master/object_detection_app.py

## but I changed it to make it more understandable to me.
def location(kkk):
    # Import packages
    import os
    import cv2
    import numpy as np
    import tensorflow as tf
    import sys
    import random
    import matplotlib as plt
    # This is needed since the notebook is stored in the object_detection folder.
    sys.path.append("..")

    # Import utilites
    from utils import label_map_util
    from utils import visualization_utils as vis_util

    # Name of the directory containing the object detection module we're using
    MODEL_NAME = 'faster_rcnn_loca'
    IMAGE_NAME = kkk


    # Grab path to current working directory
    CWD_PATH = os.getcwd()
    PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')
    PATH_TO_LABELS = os.path.join(CWD_PATH,'faster_rcnn_loca','labelmap.pbtxt')
    PATH_TO_IMAGE = os.path.join(CWD_PATH,IMAGE_NAME)

    # Number of classes the object detector can identify
    NUM_CLASSES = 2
    # Load the label map.
    # Label maps map indices to category names, so that when our convolution
    # network predicts `5`, we know that this corresponds to `king`.
    # Here we use internal utility functions, but anything that returns a
    # dictionary mapping integers to appropriate string labels would be fine
    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)

    # Load the Tensorflow model into memory.
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

        sess = tf.Session(graph=detection_graph)

    # Define input and output tensors (i.e. data) for the object detection classifier

    # Input tensor is the image
    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
    # Output tensors are the detection boxes, scores, and classes
    # Each box represents a part of the image where a particular object was detected
    detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
    # Each score represents level of confidence for each of the objects.
    # The score is shown on the result image, together with the class label.
    detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
    detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
    # Number of objects detected
    num_detections = detection_graph.get_tensor_by_name('num_detections:0')

    # Load image using OpenCV and
    # expand image dimensions to have shape: [1, None, None, 3]
    # i.e. a single-column array, where each item in the column has the pixel RGB value
    image = cv2.imread(PATH_TO_IMAGE)
    image_expanded = np.expand_dims(image, axis=0)

    # Perform the actual detection by running the model with the image as input
    (boxes, scores, classes, num) = sess.run(
        [detection_boxes, detection_scores, detection_classes, num_detections],
        feed_dict={image_tensor: image_expanded})

    # Draw the results of the detection (aka 'visulaize the results')

    vis_util.visualize_boxes_and_labels_on_image_array(
        image,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        category_index,
        use_normalized_coordinates=True,
        line_thickness=10,
        min_score_thresh=0.1)
    out = []
    height, width = image.shape[:2]
    box = np.squeeze(boxes)
    max_boxes_to_draw = box.shape[0]
    scores = np.squeeze(scores)
    min_score_thresh = 0.5
    for i in range(min(max_boxes_to_draw, box.shape[0])):
        if scores[i] > min_score_thresh:
            print(str(i))
            ymin = (int(box[i, 0] * height))
            xmin = (int(box[i, 1] * width))
            ymax = (int(box[i, 2] * height))
            xmax = (int(box[i, 3] * width))
            # print(xmin, ymin, xmax, ymax)
            boxforuse = [xmin,ymin,xmax,ymax]
            out.append(boxforuse)
            # xMiddle = int((xmin + xmax) / 2)
            # yMiddle = int((ymin + ymax) / 2)
            # font = cv2.FONT_HERSHEY_SIMPLEX
            # # 将检测到的距离显示到屏幕上
            # cv2.putText(image, str(random.randint(5000,15000)) + 'cm', (xMiddle, yMiddle), font, 1, (0, 0, 255),
            #                                         2, cv2.LINE_AA)
    return out

# cv2.namedWindow('demo', 0)
# cv2.resizeWindow('demo', 600, 500)
#
# # All the results have been drawn on image. Now display the image.
# cv2.imshow('demo', image)
#
# # Press any key to close the image
# cv2.waitKey(0)
#
# # Clean up
# cv2.destroyAllWindows()
