###########################################################################################
#This python file is to serve the formulator python file.
#it is a service python file...
#The object here are used in the formulator.py file
############################################################################################
ANIMAL_FEED_REQUIREMENT_DB= {
    "BROILERS": {
    #the  feed meal requirement for a starter broiler
                     "STARTER": {

                     },#end starter feed meal requierments
    #the feed meal for a finisher broiler
                    "FINISHER":{

                     }#end finisher meal
},#end the broilers feed meal group

    #the feed store for pig
    "PIG":{

    },

    #the feed store for goat
    "GOAT":{

    }
}#end the animal feed store database here

INGREDIENT_DB = {
    #categrories
    "CEREALS": {
        "Oats": {
            #this is where we put all the feed composition of oats
            "Dry matter": 87,
            "Crude protein":10.5,
            "Fat" : 5,
            "Crude fiber": 10.5,
            "Ash": 3 ,
            "Nitrogen-free extract": 58,
            "Metabolizable (Poultry)":58 ,
            "Digestible" : 11.01, #[MJ/Kg]
            "Metabolizable": 10.68, #[Mj/kg]
            "Net": 8,# [MJ/kg],
            "Lysine": 0.41,
            "Methionine": 0.17,
            "Methionine+cystine":0.48,
            "Threonine":0.35,
            "Trytophan":0.14,
            "Arginine":0.66,
            "Glycine":0.51,
            "Glycine+Serine":1,
            "Histidine":0.21,
            "Isoleucine":0.75,
            "Leucine":0.75,
            "Phenylalaline":0.52,
            "Phenyl.+Tyrosine":0.88,
            "Valine": 0.56,
            "Dig. energy T.D.N":66 ,#TDN(%),
            "Net energy": 0.87 , #UFI/Kg
            "D.P.":83 ,#g/Kg,
            "P.D.I.N":75,#g/kg
            "P.D.I.E":86,
            "Calcium": 0.09,
            "Total phosphorous":0.34,
            "Available phosphorous":0.08,
            "Sodium":0.06 ,
            "Potassium":0.4,
            "Chloride":0.1,
            "Magnesium": 1.17,
            "Moisture":0,
            "Cellulose":0,
            "Zinc":34.9,
            "Copper":6,#mg/kg
            "Cobalt":0.06,#mg/kg
            "Iron":0.01,#mg/kg
            "Manganese":35.8,#mg/Kg
            "iodine":0.11,#mg/kg
            "Selenium": 0.22 ,#mg/Kg,
            "Vitamin A":0.2,#IU/Kg
            "Vitamin D3":0,#IU/Kg
            "Vitamin E":14.9,#mg/kg
            "Vitamin B12":0, #mg/kg
            "Vitamin B2":14, #mg/kg
            "Starch":0,
            "FEm":0,
            "Vitamin K":0,
            "Thiamin B1":0,
            "Pyridoxin B6":0,
            "Panthotenic acid B5":0,
            "Niacin B3":0,
            "Biotin B7":0,
            "Folacin B9":0,
            "Choline":0,
            "Inositol":0,
            "Vitamin C": 0,
            "Ca/P ratio":0,
            "Natrium":0,
            "Sulfur":0,
            "Fluorine":0
        },

        "Dehulled Oats": {
            #this is where we put all the feed composition of oats
            "Dry matter": 87,
            "Crude protein":14,
            "Fat" : 7.5,
            "Crude fiber": 2,
            "Ash": 2 ,
            "Nitrogen-free extract": 61.5,
            "Metabolizable (Poultry)":13.98 ,#MJ/Kg
            "Digestible" : 15.99, #[MJ/Kg]
            "Metabolizable": 15.45, #[Mj/kg]
            "Net": 11.64,# [MJ/kg],
            "Lysine": 0.55,
            "Methionine": 0.23,
            "Methionine+cystine":0.65,
            "Threonine":0.44,
            "Trytophan":0.2,
            "Arginine":0.64,
            "Glycine":0.68,
            "Glycine+Serine":1.32,
            "Histidine":0.29,
            "Isoleucine":0.57,
            "Leucine":1.03,
            "Phenylalaline":0.73,
            "Phenyl.+Tyrosine":1.26,
            "Valine": 0.77,
            "Dig. energy T.D.N":89 ,#TDN(%),
            "Net engergy":1.33 ,#UFI/Kg
            "D.P.":124 ,#g/Kg,
            "P.D.I.N":0,#g/kg
            "P.D.I.E":0,
            "Calcium": 0.08,
            "Total phosphorous":0.38,
            "Available phosphorous":0.08,
            "Sodium":0.05 ,
            "Potassium":0.35,
            "Chloride":0.05,
            "Magnesium": 0.12,
            "Moisture":0,
            "Cellulose":0,
            "Zinc":139.5,
            "Copper":5.2,#mg/kg
            "Cobalt":0.04,#mg/kg
            "Iron":0.04,#mg/kg
            "Manganese":43.8,#mg/Kg
            "iodine":0,#mg/kg
            "Selenium":0 ,#mg/Kg,
            "Vitamin A":0,#IU/Kg
            "Vitamin D3":0,#IU/Kg
            "Vitamin E":23.7,#mg/kg
            "Vitamin B12":0, #mg/kg
            "Vitamin B2":1.7, #mg/kg
            "Starch":0,
            "FEm":0,
            "Vitamin K":0,
            "Thiamin B1":0,
            "Pyridoxin B6":0,
            "Panthotenic acid B5":0,
            "Niacin B3":0,
            "Biotin B7":0,
            "Folacin B9":0,
            "Choline":0,
            "Inositol":0,
            "Vitamin C": 0,
            "Ca/P ratio":0,
            "Natrium":0,
            "Sulfur":0,
            "Fluorine":0
        },
        "Wheat": {
            #this is where we put all the feed composition of oats
            "Dry matter": 87,
            "Crude protein":11.5,
            "Fat" : 2,
            "Crude fiber": 2,
            "Ash": 1.5 ,
            "Nitrogen-free extract": 70.5,
            "Metabolizable (Poultry)":12.81 ,
            "Digestible" : 14.24, #[MJ/Kg]
            "Metabolizable": 13.77, #[Mj/kg]
            "Net": 10.17,# [MJ/kg],
            "Lysine": 0.33,
            "Methionine": 0.18,
            "Methionine+cystine":0.45,
            "Threonine":0.33,
            "Trytophan":0.13,
            "Arginine":0.55,
            "Glycine":0.45,
            "Glycine+Serine":98,
            "Histidine":0.26,
            "Isoleucine":0.42,
            "Leucine":0.76,
            "Phenylalaline":0.51,
            "Phenyl.+Tyrosine":0.83,
            "Valine": 0.51,
            "Dig. energy T.D.N":80 ,#TDN(%),
            "Net energy": 1.05, #UFI/Kg
            "D.P.":98 ,#g/Kg,
            "P.D.I.N":76,#g/kg
            "P.D.I.E":87,
            "Calcium": 0.05,
            "Total phosphorous":0.33,
            "Available phosphorous":0.18,
            "Sodium":0.05 ,
            "Potassium":0.4,
            "Chloride":0.06,
            "Magnesium": 0.14,
            "Moisture":0,
            "Cellulose":0,
            "Zinc":31.4,
            "Copper":5.8,#mg/kg
            "Cobalt":0.44,#mg/kg
            "Iron":0.01,#mg/kg
            "Manganese":41.5,#mg/Kg
            "iodine":0.09,#mg/kg
            "Selenium": 0.26 ,#mg/Kg,
            "Vitamin A":0,#IU/Kg
            "Vitamin D3":0,#IU/Kg
            "Vitamin E":15.5,#mg/kg
            "Vitamin B12":0.9, #mg/kg
            "Vitamin B2":1.3, #mg/kg
            "Starch":0,
            "FEm":0,
            "Vitamin K":0,
            "Thiamin B1":0,
            "Pyridoxin B6":0,
            "Panthotenic acid B5":0,
            "Niacin B3":0,
            "Biotin B7":0,
            "Folacin B9":0,
            "Choline":0,
            "Inositol":0,
            "Vitamin C": 0,
            "Ca/P ratio":0,
            "Natrium":0,
            "Sulfur":0,
            "Fluorine":0

        },
        "Hard Wheat": {

            #this is where we put all the feed composition of oats
            "Dry matter": 87,
            "Crude protein":14.5,
            "Fat" : 7.5,
            "Crude fiber": 2.5,
            "Ash": 2,
            "Nitrogen-free extract": 66.5,
            "Metabolizable (Poultry)":12.39 ,#MJ/Kg
            "Digestible" : 14.29, #[MJ/Kg]
            "Metabolizable": 13.73, #[Mj/kg]
            "Net": 10.01,# [MJ/kg],
            "Lysine": 0.39,
            "Methionine": 0.24,
            "Methionine+cystine":0.6,
            "Threonine":0.4,
            "Trytophan":0.17,
            "Arginine":0.65,
            "Glycine":0.56,
            "Glycine+Serine":1.22,
            "Histidine":0.32,
            "Isoleucine":0.55,
            "Leucine":8.95,
            "Phenylalaline":0.68,
            "Phenyl.+Tyrosine":1.1,
            "Valine": 0.64,
            "Dig. energy T.D.N":73 ,#TDN(%),
            "Net energy":1.06, #UFI/Kg
            "D.P.":123 ,#g/Kg,
            "P.D.I.N":95,#g/kg
            "P.D.I.E":95,
            "Calcium": 0.04,
            "Total phosphorous":0.37,
            "Available phosphorous":0.19,
            "Sodium":0.03 ,
            "Potassium":0.45,
            "Chloride":0.05,
            "Magnesium": 0.1,
            "Moisture":0,
            "Cellulose":0,
            "Zinc":37.9,
            "Copper":6,#mg/kg
            "Cobalt":0.12,#mg/kg
            "Iron":0.01,#mg/kg
            "Manganese":37,#mg/Kg
            "iodine":0,#mg/kg
            "Selenium":0.26 ,#mg/Kg,
            "Vitamin A":0,#IU/Kg
            "Vitamin D3":0,#IU/Kg
            "Vitamin E":12.7,#mg/kg
            "Vitamin B12":0, #mg/kg
            "Vitamin B2":1.4, #mg/kg
            "Starch":0,
            "FEm":0,
            "Vitamin K":0,
            "Thiamin B1":0,
            "Pyridoxin B6":0,
            "Panthotenic acid B5":0,
            "Niacin B3":0,
            "Biotin B7":0,
            "Folacin B9":0,
            "Choline":0,
            "Inositol":0,
            "Vitamin C": 0,
            "Ca/P ratio":0,
            "Natrium":0,
            "Sulfur":0,
            "Fluorine":0
        },
        "Corn Maize": {
            #this is where we put all the feed composition of oats
            "Dry matter": 87,
            "Crude protein":9,
            "Fat" : 4,
            "Crude fiber": 2,
            "Ash": 1.5 ,
            "Nitrogen-free extract": 70.5,
            "Metabolizable (Poultry)":13.9 ,
            "Digestible" : 14.57, #[MJ/Kg]
            "Metabolizable": 14.24, #[Mj/kg]
            "Net": 10.68,# [MJ/kg],
            "Lysine": 0.26,
            "Methionine": 0.19,
            "Methionine+cystine":0.38,
            "Threonine":0.32,
            "Trytophan":0.07,
            "Arginine":0.41,
            "Glycine":0.33,
            "Glycine+Serine":0.76,
            "Histidine":0.26,
            "Isoleucine":0.34,
            "Leucine":1.13,
            "Phenylalaline":0.45,
            "Phenyl.+Tyrosine":0.81,
            "Valine": 0.45,
            "Dig. energy T.D.N":79 ,#TDN(%),
            "Net energy":1.1 ,#UFI/Kg
            "D.P.":64 ,#g/Kg,
            "P.D.I.N":68,#g/kg
            "P.D.I.E":99,
            "Calcium": 0.01,
            "Total phosphorous":0.25,
            "Available phosphorous":0.03,
            "Sodium":0.03 ,
            "Potassium":0.33,
            "Chloride":0.04,
            "Magnesium": 0.15,
            "Moisture":0,
            "Cellulose":0,
            "Zinc":19.4, #mg/
            "Copper":3.5,     #mg/kg
            "Cobalt":0.38,  #mg/kg
            "Iron":0,    #mg/kg
            "Manganese":5.7,#mg/Kg
            "iodine":0,      #mg/kg
            "Selenium": 0.13 ,  #mg/Kg,
            "Vitamin A":9.5,#IU/Kg
            "Vitamin D3":0,#IU/Kg
            "Vitamin E":20.9,#mg/kg
            "Vitamin B12":0.07, #mg/kg
            "Vitamin B2":6.16, #mg/kg
            "Starch":0,
            "FEm":0,
            "Vitamin K":0,
            "Thiamin B1":0,
            "Pyridoxin B6":0,
            "Panthotenic acid B5":0,
            "Niacin B3":0,
            "Biotin B7":0,
            "Folacin B9":0,
            "Choline":0,
            "Inositol":0,
            "Vitamin C": 0,
            "Ca/P ratio":0,
            "Natrium":0,
            "Sulfur":0,
            "Fluorine":0
        },
        "Millet": {

            # this is where we put all the feed composition of oats
            "Dry matter": 87,
            "Crude protein": 11,
            "Fat": 4,
            "Crude fiber": 8,
            "Ash": 3.5,
            "Nitrogen-free extract": 60.5,
            "Metabolizable (Poultry)": 12.43,
            "Digestible": 12.02,  # [MJ/Kg]
            "Metabolizable": 11.68,  # [Mj/kg]
            "Net": 8.67,  # [MJ/kg],
            "Lysine": 0.21,
            "Methionine": 0.3,
            "Methionine+cystine": 0.48,
            "Threonine": 0.34,
            "Trytophan": 0.15,
            "Arginine": 0.44,
            "Glycine": 0.29,
            "Glycine+Serine": 1.82,
            "Histidine": 0.25,
            "Isoleucine": 0.49,
            "Leucine": 1.34,
            "Phenylalaline": 0.62,
            "Phenyl.+Tyrosine": 1.88,
            "Valine": 0.61,
            "Dig. energy T.D.N": 70,  # TDN(%),
            "Net energy": 0.87, #UFI/Kg
            "D.P.": 77,  # g/Kg,
            "P.D.I.N": 84,  # g/kg
            "P.D.I.E": 99,
            "Calcium": 0.04,
            "Total phosphorous": 0.3,
            "Available phosphorous": 0.08,
            "Sodium": 0.04,
            "Potassium": 0.43,
            "Chloride": 0.03,
            "Magnesium": 0.16,
            "Moisture": 0,
            "Cellulose": 0,
            "Zinc": 0,
            "Copper": 6,  # mg/kg
            "Cobalt": 0.06,  # mg/kg
            "Iron": 0.01,  # mg/kg
            "Manganese": 35.8,  # mg/Kg
            "iodine": 0.11,  # mg/kg
            "Selenium": 0.22,  # mg/Kg,
            "Vitamin A": 0.2,  # IU/Kg
            "Vitamin D3": 0,  # IU/Kg
            "Vitamin E": 14.9,  # mg/kg
            "Vitamin B12": 0,  # mg/kg
            "Vitamin B2": 3.3,  # mg/kg
            "Starch": 0,
            "FEm": 0,
            "Vitamin K": 0,
            "Thiamin B1": 0,
            "Pyridoxin B6": 0,
            "Panthotenic acid B5": 0,
            "Niacin B3": 0,
            "Biotin B7": 0,
            "Folacin B9": 0,
            "Choline": 0,
            "Inositol": 0,
            "Vitamin C": 0,
            "Ca/P ratio": 0,
            "Natrium": 0,
            "Sulfur": 0,
            "Fluorine": 0
        },
        "Barley": {
            # this is where we put all the feed composition of oats
            "Dry matter": 87,
            "Crude protein": 10,
            "Fat": 2,
            "Crude fiber": 5,
            "Ash": 2.5,
            "Nitrogen-free extract": 53,
            "Metabolizable (Poultry)": 11.35,
            "Digestible": 12.77,  # [MJ/Kg]
            "Metabolizable": 12.39,  # [Mj/kg]
            "Net": 9.13,  # [MJ/kg],
            "Lysine": 0.37,
            "Methionine": 0.16,
            "Methionine+cystine": 0.38,
            "Threonine": 0.33,
            "Trytophan": 0.11,
            "Arginine": 0.5,
            "Glycine": 0.48,
            "Glycine+Serine": 0.82,
            "Histidine": 0.21,
            "Isoleucine": 0.37,
            "Leucine": 0.69,
            "Phenylalaline": 0.51,
            "Phenyl.+Tyrosine": 0.82,
            "Valine": 0.56,
            "Dig. energy T.D.N": 72,  # TDN(%),
            "Net energy":1 , #UFI/Kg
            "D.P.": 75,  # g/Kg,
            "P.D.I.N": 70,  # g/kg
            "P.D.I.E": 88,
            "Calcium": 0.69,
            "Total phosphorous": 0.35,
            "Available phosphorous": 0.17,
            "Sodium": 0.05,
            "Potassium": 0.48,
            "Chloride": 0.14,
            "Magnesium": 0.12,
            "Moisture": 0,
            "Cellulose": 0,
            "Zinc": 39.4, #mg/Kg
            "Copper": 7.6,  # mg/kg
            "Cobalt": 0.17,  # mg/kg
            "Iron": 0.01,  # mg/kg
            "Manganese":16,  # mg/Kg
            "iodine": 0.04,  # mg/kg
            "Selenium": 0.16,  # mg/Kg,
            "Vitamin A": 3.4,  # IU/Kg
            "Vitamin D3": 0,  # IU/Kg
            "Vitamin E": 23.2,  # mg/kg
            "Vitamin B12": 0,  # mg/kg
            "Vitamin B2": 1.6,  # mg/kg
            "Starch": 0,
            "FEm": 0,
            "Vitamin K": 0,
            "Thiamin B1": 0,
            "Pyridoxin B6": 0,
            "Panthotenic acid B5": 0,
            "Niacin B3": 0,
            "Biotin B7": 0,
            "Folacin B9": 0,
            "Choline": 0,
            "Inositol": 0,
            "Vitamin C": 0,
            "Ca/P ratio": 0,
            "Natrium": 0,
            "Sulfur": 0,
            "Fluorine": 0
        },

        "Paddy Rice": {
            # this is where we put all the feed composition of oats
            "Dry matter": 87,
            "Crude protein": 8,
            "Fat": 2,
            "Crude fiber": 9,
            "Ash": 4.5,
            "Nitrogen-free extract": 63.5,
            "Metabolizable (Poultry)": 11.1,
            "Digestible": 11.1,  # [MJ/Kg]
            "Metabolizable": 10.8,  # [Mj/kg]
            "Net": 8.04,  # [MJ/kg],
            "Lysine": 0.28,
            "Methionine": 0.14,
            "Methionine+cystine": 0.36,
            "Threonine": 0.28,
            "Trytophan": 0.1,
            "Arginine": 0.61,
            "Glycine": 0.36,
            "Glycine+Serine": 0.76,
            "Histidine": 0.17,
            "Isoleucine": 0.32,
            "Leucine": 0.59,
            "Phenylalaline": 0.39,
            "Phenyl.+Tyrosine": 0.74,
            "Valine": 0.48,
            "Dig. energy T.D.N": 70,  # TDN(%),
            "Net energy":0.93, #UFI/Kg
            "D.P.": 62,  # g/Kg,
            "P.D.I.N": 62,  # g/kg
            "P.D.I.E": 94,
            "Calcium": 0.04,
            "Total phosphorous": 0.26,
            "Available phosphorous": 0.1,
            "Sodium": 0.03,
            "Potassium": 0.34,
            "Chloride": 0.05,
            "Magnesium": 0.14,
            "Moisture": 0,
            "Cellulose": 0,
            "Zinc": 15,
            "Copper": 0,  # mg/kg
            "Cobalt": 0,  # mg/kg
            "Iron": 0,  # mg/kg
            "Manganese": 18,  # mg/Kg
            "iodine": 0,  # mg/kg
            "Selenium": 0,  # mg/Kg,
            "Vitamin A": 0,  # IU/Kg
            "Vitamin D3": 0,  # IU/Kg
            "Vitamin E": 14,  # mg/kg
            "Vitamin B12": 0,  # mg/kg
            "Vitamin B2": 0.7,  # mg/kg
            "Starch": 0,
            "FEm": 0,
            "Vitamin K": 0,
            "Thiamin B1": 0,
            "Pyridoxin B6": 0,
            "Panthotenic acid B5": 0,
            "Niacin B3": 0,
            "Biotin B7": 0,
            "Folacin B9": 0,
            "Choline": 0,
            "Inositol": 0,
            "Vitamin C": 0,
            "Ca/P ratio": 0,
            "Natrium": 0,
            "Sulfur": 0,
            "Fluorine": 0
        },
        "Rye": {
            # this is where we put all the feed composition of oats
            "Dry matter": 87,
            "Crude protein": 10.5,
            "Fat": 5,
            "Crude fiber": 10.5,
            "Ash": 3,
            "Nitrogen-free extract": 58,
            "Metabolizable (Poultry)": 58,
            "Digestible": 11.01,  # [MJ/Kg]
            "Metabolizable": 10.68,  # [Mj/kg]
            "Net": 8,  # [MJ/kg],
            "Lysine": 0.41,
            "Methionine": 0.17,
            "Methionine-cystine": 0.48,
            "Threonine": 0.35,
            "Trytophan": 0.14,
            "Arginine": 0.66,
            "Glycine": 0.51,
            "Glycine-Serine": 1,
            "Histidine": 0.21,
            "Isoleucine": 0.75,
            "Leucine": 0.75,
            "Phenylalaline": 0.52,
            "Phenyl+Tyrosine": 0.88,
            "Valine": 0.56,
            "Dig. energy T.D.N": 66,  # TDN(%),
            "D.P.": 83,  # g/Kg,
            "P.D.I.N": 75,  # g/kg
            "P.D.I.E": 86,
            "Calcium": 0.09,
            "Total phosphorous": 0.34,
            "Available phosphorous": 0.08,
            "Sodium": 0.06,
            "Potassium": 0.4,
            "Chloride": 0.1,
            "Magnesium": 1.17,
            "Moisture": 0,
            "Cellulose": 0,
            "Zinc": 34.9,
            "Copper": 6,  # mg/kg
            "Cobalt": 0.06,  # mg/kg
            "Iron": 0.01,  # mg/kg
            "Manganese": 35.8,  # mg/Kg
            "iodine": 0.11,  # mg/kg
            "Selenium": 0.22,  # mg/Kg,
            "Vitamin A": 0.2,  # IU/Kg
            "Vitamin D3": 0,  # IU/Kg
            "Vitamin E": 14.9,  # mg/kg
            "Vitamin B12": 0,  # mg/kg
            "Vitamin B2": 14,  # mg/kg
            "Starch": 0,
            "FEm": 0,
            "Vitamin K": 0,
            "Thiamin B1": 0,
            "Pyridoxin B6": 0,
            "Panthotenic acid B5": 0,
            "Niacin B3": 0,
            "Biotin B7": 0,
            "Folacin B9": 0,
            "Choline": 0,
            "Inositol": 0,
            "Vitamin C": 0,
            "Ca/P ratio": 0,
            "Natrium": 0,
            "Sulfur": 0,
            "Fluorine": 0
        },
        "Sorghum Milo": {
            # this is where we put all the feed composition of oats
            "Dry matter": 87,
            "Crude protein": 10.5,
            "Fat": 5,
            "Crude fiber": 10.5,
            "Ash": 3,
            "Nitrogen-free extract": 58,
            "Metabolizable (Poultry)": 58,
            "Digestible": 11.01,  # [MJ/Kg]
            "Metabolizable": 10.68,  # [Mj/kg]
            "Net": 8,  # [MJ/kg],
            "Lysine": 0.41,
            "Methionine": 0.17,
            "Methionine-cystine": 0.48,
            "Threonine": 0.35,
            "Trytophan": 0.14,
            "Arginine": 0.66,
            "Glycine": 0.51,
            "Glycine-Serine": 1,
            "Histidine": 0.21,
            "Isoleucine": 0.75,
            "Leucine": 0.75,
            "Phenylalaline": 0.52,
            "Phenyl+Tyrosine": 0.88,
            "Valine": 0.56,
            "Dig. energy T.D.N": 66,  # TDN(%),
            "D.P.": 83,  # g/Kg,
            "P.D.I.N": 75,  # g/kg
            "P.D.I.E": 86,
            "Calcium": 0.09,
            "Total phosphorous": 0.34,
            "Available phosphorous": 0.08,
            "Sodium": 0.06,
            "Potassium": 0.4,
            "Chloride": 0.1,
            "Magnesium": 1.17,
            "Moisture": 0,
            "Cellulose": 0,
            "Zinc": 34.9,
            "Copper": 6,  # mg/kg
            "Cobalt": 0.06,  # mg/kg
            "Iron": 0.01,  # mg/kg
            "Manganese": 35.8,  # mg/Kg
            "iodine": 0.11,  # mg/kg
            "Selenium": 0.22,  # mg/Kg,
            "Vitamin A": 0.2,  # IU/Kg
            "Vitamin D3": 0,  # IU/Kg
            "Vitamin E": 14.9,  # mg/kg
            "Vitamin B12": 0,  # mg/kg
            "Vitamin B2": 14,  # mg/kg
            "Starch": 0,
            "FEm": 0,
            "Vitamin K": 0,
            "Thiamin B1": 0,
            "Pyridoxin B6": 0,
            "Panthotenic acid B5": 0,
            "Niacin B3": 0,
            "Biotin B7": 0,
            "Folacin B9": 0,
            "Choline": 0,
            "Inositol": 0,
            "Vitamin C": 0,
            "Ca/P ratio": 0,
            "Natrium": 0,
            "Sulfur": 0,
            "Fluorine": 0
        },
        "Brewers Dried Grains": {
            # this is where we put all the feed composition of oats
            "Dry matter": 87,
            "Crude protein": 10.5,
            "Fat": 5,
            "Crude fiber": 10.5,
            "Ash": 3,
            "Nitrogen-free extract": 58,
            "Metabolizable (Poultry)": 58,
            "Digestible": 11.01,  # [MJ/Kg]
            "Metabolizable": 10.68,  # [Mj/kg]
            "Net": 8,  # [MJ/kg],
            "Lysine": 0.41,
            "Methionine": 0.17,
            "Methionine-cystine": 0.48,
            "Threonine": 0.35,
            "Trytophan": 0.14,
            "Arginine": 0.66,
            "Glycine": 0.51,
            "Glycine-Serine": 1,
            "Histidine": 0.21,
            "Isoleucine": 0.75,
            "Leucine": 0.75,
            "Phenylalaline": 0.52,
            "Phenyl+Tyrosine": 0.88,
            "Valine": 0.56,
            "Dig. energy T.D.N": 66,  # TDN(%),
            "D.P.": 83,  # g/Kg,
            "P.D.I.N": 75,  # g/kg
            "P.D.I.E": 86,
            "Calcium": 0.09,
            "Total phosphorous": 0.34,
            "Available phosphorous": 0.08,
            "Sodium": 0.06,
            "Potassium": 0.4,
            "Chloride": 0.1,
            "Magnesium": 1.17,
            "Moisture": 0,
            "Cellulose": 0,
            "Zinc": 34.9,
            "Copper": 6,  # mg/kg
            "Cobalt": 0.06,  # mg/kg
            "Iron": 0.01,  # mg/kg
            "Manganese": 35.8,  # mg/Kg
            "iodine": 0.11,  # mg/kg
            "Selenium": 0.22,  # mg/Kg,
            "Vitamin A": 0.2,  # IU/Kg
            "Vitamin D3": 0,  # IU/Kg
            "Vitamin E": 14.9,  # mg/kg
            "Vitamin B12": 0,  # mg/kg
            "Vitamin B2": 14,  # mg/kg
            "Starch": 0,
            "FEm": 0,
            "Vitamin K": 0,
            "Thiamin B1": 0,
            "Pyridoxin B6": 0,
            "Panthotenic acid B5": 0,
            "Niacin B3": 0,
            "Biotin B7": 0,
            "Folacin B9": 0,
            "Choline": 0,
            "Inositol": 0,
            "Vitamin C": 0,
            "Ca/P ratio": 0,
            "Natrium": 0,
            "Sulfur": 0,
            "Fluorine": 0
        },
        "Groundnut Solvent": {
            # this is where we put all the feed composition of oats
            "Dry matter": 87,
            "Crude protein": 10.5,
            "Fat": 5,
            "Crude fiber": 10.5,
            "Ash": 3,
            "Nitrogen-free extract": 58,
            "Metabolizable (Poultry)": 58,
            "Digestible": 11.01,  # [MJ/Kg]
            "Metabolizable": 10.68,  # [Mj/kg]
            "Net": 8,  # [MJ/kg],
            "Lysine": 0.41,
            "Methionine": 0.17,
            "Methionine-cystine": 0.48,
            "Threonine": 0.35,
            "Trytophan": 0.14,
            "Arginine": 0.66,
            "Glycine": 0.51,
            "Glycine-Serine": 1,
            "Histidine": 0.21,
            "Isoleucine": 0.75,
            "Leucine": 0.75,
            "Phenylalaline": 0.52,
            "Phenyl+Tyrosine": 0.88,
            "Valine": 0.56,
            "Dig. energy T.D.N": 66,  # TDN(%),
            "D.P.": 83,  # g/Kg,
            "P.D.I.N": 75,  # g/kg
            "P.D.I.E": 86,
            "Calcium": 0.09,
            "Total phosphorous": 0.34,
            "Available phosphorous": 0.08,
            "Sodium": 0.06,
            "Potassium": 0.4,
            "Chloride": 0.1,
            "Magnesium": 1.17,
            "Moisture": 0,
            "Cellulose": 0,
            "Zinc": 34.9,
            "Copper": 6,  # mg/kg
            "Cobalt": 0.06,  # mg/kg
            "Iron": 0.01,  # mg/kg
            "Manganese": 35.8,  # mg/Kg
            "iodine": 0.11,  # mg/kg
            "Selenium": 0.22,  # mg/Kg,
            "Vitamin A": 0.2,  # IU/Kg
            "Vitamin D3": 0,  # IU/Kg
            "Vitamin E": 14.9,  # mg/kg
            "Vitamin B12": 0,  # mg/kg
            "Vitamin B2": 14,  # mg/kg
            "Starch": 0,
            "FEm": 0,
            "Vitamin K": 0,
            "Thiamin B1": 0,
            "Pyridoxin B6": 0,
            "Panthotenic acid B5": 0,
            "Niacin B3": 0,
            "Biotin B7": 0,
            "Folacin B9": 0,
            "Choline": 0,
            "Inositol": 0,
            "Vitamin C": 0,
            "Ca/P ratio": 0,
            "Natrium": 0,
            "Sulfur": 0,
            "Fluorine": 0
        },
    }
}

#this is where all the prices for the ingredient ia stored...
INGREDIENT_PRICE_DB = {
    #The Prices for each ingredient is in Naira
    "Oats": 23,"Dehulled Oats": 10,"Wheat":12,
    "Hard Wheat": 12,"Corn Maze":12,"Millet": 120,
    "Balley":12,"Paddy Rice":34,"Rye":23,
    "Sorghum Milo":50,"Brewers Dried Grains":45,"Groundnut Solvent":100
}# End the Ingredient price dictionary
