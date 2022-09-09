from flask import Flask, jsonify, render_template, request,redirect, url_for
import config
from project_app.utils import Wine
app = Flask(__name__)

########################################################################

@app.route('/') 
def hello_flask():
    print("Welcome to Flask")
    # return render_template("home.html")
    return 'Hello Python'

#########################################################################


@app.route('/predict')
def get_predicted():

    data = request.get_json()
    Alcohol = eval(data['Alcohol'])
    Malic_acid = eval(data['Malic_acid'])
    Ash = eval(data['Ash'])
    Acl = eval(data['Acl'])
    Mg = eval(data['Mg'])
    Phenols = eval(data['Phenols'])
    Flavanoids = eval(data['Flavanoids'])
    Nonflavanoid_phenols = eval(data['Nonflavanoid_phenols'])
    Proanth = eval(data['Proanth'])
    Color_int = eval(data['Color_int'])
    Hue = eval(data['Hue'])
    OD = eval(data['OD'])
    Proline = eval(data['Proline'])
    
    #print("CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX,PTRATIO, B, LSTAT",CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX,PTRATIO, B, LSTAT)
    wine = Wine(Alcohol ,Malic_acid,Ash,Acl,Mg,Phenols,Flavanoids,Nonflavanoid_phenols,Proanth,Color_int,Hue,OD,Proline)
    wine = wine.get_predicted()
                    
    return jsonify({"Result":f"Predicted wine quality : {wine}"})

if __name__ == "__main__":
    app.run(port=config.PORT_NUMBER)