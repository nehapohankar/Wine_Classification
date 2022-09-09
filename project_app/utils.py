
import pickle
import json
import numpy as np
import config 

class Wine():
    def __init__(self,Alcohol ,Malic_acid,Ash,Acl,Mg,Phenols,Flavanoids,Nonflavanoid_phenols,Proanth,Color_int,Hue,OD,Proline):
        self.Alcohol = Alcohol
        self.Malic_acid = Malic_acid
        self.Ash = Ash
        self.Acl = Acl
        self.Mg = Mg
        self.Phenols = Phenols
        self.Flavanoids = Flavanoids
        self.Nonflavanoid_phenols = Nonflavanoid_phenols
        self.Proanth = Proanth
        self.Color_int = Color_int
        self.Hue = Hue
        self.OD = OD
        self.Proline = Proline
        

    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)
            
    def get_predicted(self):
        self.load_model()
        
        
        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.Alcohol
        test_array[1] = self.Malic_acid
        test_array[2] = self.Ash
        test_array[3] = self.Acl
        test_array[4] = self.Mg
        test_array[5] = self.Phenols
        test_array[6] = self.Flavanoids
        test_array[7] = self.Nonflavanoid_phenols
        test_array[8] = self.Proanth
        test_array[9] = self.Color_int
        test_array[10] = self.Hue
        test_array[11] = self.OD
        test_array[12] = self.Proline
        predicted = self.model.predict([test_array])
        return predicted
    
        print("Test array :",test_array)
        
if __name__ == "__main__":
    Alcohol                  =12.79000
    Malic_acid               = 2.67000
    Ash                      = 2.48000
    Acl                      =22.00000
    Mg                     = 112.00000
    Phenols                  = 1.48000
    Flavanoids               = 1.36000
    Nonflavanoid_phenols     = 0.24000
    Proanth                  = 1.26000
    Color_int                = 5.05809
    Hue                      = 0.48000
    OD                       = 1.47000
    Proline                = 480.00000

    wine = Wine(Alcohol ,Malic_acid,Ash,Acl,Mg,Phenols,Flavanoids,Nonflavanoid_phenols,Proanth,Color_int,Hue,OD,Proline)
    wine.get_predicted()
                    