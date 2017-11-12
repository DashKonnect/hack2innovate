from mss import mss
from  PIL import Image

i=0
def getImage():
  with mss() as sct:
    # The screen part to capture
    mon = {'top': 230, 'left': 50, 'width': 950, 'height': 600}
    sct.get_pixels(mon)
    img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
  return img


while(True):
      image_data = getImage()
      image_data.save("marcel/V/"+str(i)+".jpg")
      i += 1
      print(i)