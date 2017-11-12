import tensorflow as tf
import sys
from mss import mss
from PIL import Image
import numpy as np
import os


def getImage():
  with mss() as sct:
    # The screen part to capture
    mon = {'top': 230, 'left': 50, 'width': 950, 'height': 600}
    sct.get_pixels(mon)
    img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    return img

# Read in the image_data
#image_data = tf.gfile.FastGFile(image_path, 'rb').read()

# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line 
     in tf.gfile.GFile("retrained_labels_marcel.txt")]

# Unpersists graph from file
with tf.gfile.FastGFile("retrained_graph_marcel_flip.pb", 'rb') as f:
  graph_def = tf.GraphDef()
  graph_def.ParseFromString(f.read())
  _ = tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
  # Feed the image_data as input to the graph and get first prediction
  softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
  for file in os.listdir("cross_validation_data"):
    f = open("cross_validation_data/"+file, 'rb+')
    image_data = Image.open(f)
    image_array = np.array(image_data)[:, :, 0:3]
    predictions = sess.run(softmax_tensor, \
     {'DecodeJpeg:0': image_data})

    filename = "result.csv" 
    with open(filename, 'a+') as f:
      # Sort to show labels of first prediction in order of confidence
      top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
      f.write("{},{}\n".format(file,label_lines[top_k[0]]))



'''
         
  while(True):


  image_data = getImage()
  image_array = np.array(image_data)[:, :, 0:3]
  predictions = sess.run(softmax_tensor, \
   {'DecodeJpeg:0': image_data})
  
  # Sort to show labels of first prediction in order of confidence
  top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
  
  for node_id in top_k:
  human_string = label_lines[node_id]
  score = predictions[0][node_id]
  if score > 0.95:
  print('%s (score = %.5f)' % (human_string, score))
  
  '''
  