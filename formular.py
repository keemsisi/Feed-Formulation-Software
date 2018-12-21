#This is a feed formulation software developed by NeuralTehx
#Date : 25/09/2018
#Author : Lasisi, Akeem Adeshina (CEO - NeuralTechX)
#Location Developed : Oshodi-Isolo Mafoluku , Lagos
#
######################################################################################################################
# This class below is the animal feed meal Database, which will be enriched with some functions, so as to help      #
# the class access the values in the Dictionary database provided above.
#######################################################################################################################
from scipy.optimize import linprog , minimize

NUTRIENT_REQUIREMENT = {
    "Ether extract":8,
    "Crude protein": 0,
    ""
}

#this below dictionary is for the price list of the ingredient
INGREDIENT_PRICE = {
    "Maize Yellow":,
    ""
}


class AnimalFeedIngredientPriceDBClass():
    def __init__(self):
     return "";


    def add_new_animal_feed_meal(self, feed_payload= {}):
        """

        :param feed_payload:
        :param
        :return returns a boolean value for the success of the addition of the meal to the database:
        """
        return True

    #this method removes the feed meal of the of the animal from the database
    def remove_animal_feed_meal_by_name(self, animal_name =None):
        return

    def get_animal_feed_meal_by_name(self, animal_name = None):
        return  {}; # returns the animal feed meal requirement


    def get_animal_feed_meal_database(self):
        """

        :return: This function returns the database of the animal feed meals
        """
        return; #returns the animal feed meal database store object




class AnimalFeedRequirementDBClass():
    def __init__(self):
        return




#THis class below will be used to interact with the feed ingredients and the Prices of the ingredient
class AnimalFeedMealFormulatorEngine(
    AnimalFeedIngredientPriceDBClass,
    AnimalFeedRequirementDBClass
):
    from PyQt5 import  QtCore , QtWidgets, QtGui
    from PyQt5.QtCore import pyqtSlot
    """
    This class extends the AnimalFeedMealDataBaseStore so for better interactions
    """
    def __init__(self):
        return


    def uptimize_feed_formulation(self):
        self.objective_function_coefficients = [62,148,36,56,42,8,45,600,1600,320] ;
        self.constraints = [[1,1,1,1,1,1,1,1,1,1],
                            [0.41, 0.035, 0.045, 0.035, 0, 0, 0, 0, 0, 0],
                            [0.41, 0.035, 0.045, 0.035, 0, 0, 0, 0, 0, 0],
                            [0.085, 0.43, 0.65, 0.17, 0.504, 0, 0, 0, 0, 0],
                            [3350, 2440, 2820, 1869, 2150, 0, 0,0 ,0 ,0],
                            [0.02, 0.065, 0.01, 0.0865, 0, 0, 0, 0, 0, 0],
                            [0.0001,0.002,0.061,0.001,0.37,0,0.35,0,0,0],
                            [0.0009, 0.006, 0.03, 0.003, 0.15, 0 , 0,0,0,0],
                            [0.0018, 0.0059, 0.018, 0.0025, 0, 0, 0, 0, 1, 0],
                            [0.0025, 0.028, 0.045, 0.009, 0,0,0,1,0,0],
                            [0.04, 0.035, 0.045, 0.035, 0, 0, 0, 0, 0, 0],
                            [0.04, 0.035, 0.045, 0.035, 0, 0, 0, 0, 0, 0],
                            [0.08, 0.43, 0.65, 0.17, 0.504, 0, 0, 0, 0, 0],
                            [3350.0, 2440, 2820, 1869, 2150, 0, 0, 0, 0, 0],
                            [0.02, 0.065, 0.01, 0.0865, 0, 0, 0, 0, 0, 0],
                            [0.0001, 0.002, 0.061, 0.001, 0.37,0,0.35,0,0,0],
                            [0.0009, 0.006, 0.03, 0.003, 0.15, 0, 0, 0, 0, 0],
                            [0.0018, 0.0059, 0.018, 0.0025, 0, 0, 0, 0, 1, 0],
                            [0.0025, 0.028, 0.045, 0.009, 0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]
        self.constraints_left_hand_sides = [1000,40,50,230,3200,35,10,4.5,4.0,10.9,40,50,180,3200,35,8,4.0,4.5,11.2,3];

        #this place is for the constraint boundary
        self.constraints_boundary = (None, None)

        #This is whent the formulation starts to compute
        self.optimized_cost = linprog(self.objective_function_coefficients , A_ub= self.constraints , b_ub= self.constraints_left_hand_sides,
                                      bounds=[self.constraints_boundary]*10)

        print(self.optimized_cost)




obj = AnimalFeedMealFormulatorEngine()
obj.uptimize_feed_formulation()