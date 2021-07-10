import boto3
import  easyocr
def get_number():

  #calling Textract
  reader = easyocr.Reader(['en'])
  result = reader.readtext("detected_plate.png")
  number = result[0][1]
  
 
  return number
