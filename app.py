from flask import Flask
from flask import render_template
from flask import request
from number_plate_detect import save_plate
from get_plate_number import get_number
from get_user_details import user_details


app = Flask("app")
# upload file-------------------------------------
def upload_file():
  file = request.files['file']
  file.save(file.filename)
  print(file)



@app.route("/input")
def home():	
	return render_template("input.html")

@app.route("/get_details", methods = ["POST", "GET"])
def get_details():

   # upload file in working directory
   upload_file()  

   # save the cropped image of number plate
   save_plate()

   # get the numbers from plate
   number_ = get_number()

   print(number_)
   
   user = "Tanvi_Mittal"
   details = user_details(number_, user)

   return render_template(
                 "output.html", 
                 model = details[0],
                 regyear = details[1],
                 engsize = details[2],
                 sea = details[3],
                 idfi = details[4],
                 engnum = details[5],
                 fuelt = details[6],
                 regdate = details[7],
                 loc = details[8]
         )
         

app.run(host = "0.0.0.0", port = "98")

