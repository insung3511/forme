import numpy as np


class signalTools:
    def striper(input_list):
        return_list = []
        for val in input_list:
            return_list.append(val.strip())
        return return_list
    

    def compare_checker(input_list, check_list):
        cflag = False

        for inval in input_list:
            for chval in check_list:
                if inval == chval:
                    cflag == True
                else:
                    cflag == False

        return cflag
    
    def shape_print(first_input, second_input):
        first_shape = []
        second_shape = []
        
        try:
            first_input = np.array(first_input)
            second_input = np.array(second_input)

            for idx in range(len(first_input)):
                first_shape.append(first_input.shape)

            for idx in range(len(second_input)):
                second_shape.append(second_input.shape)

        except IndexError:
            print("U over it. too much.")

        except TypeError:
            print("U picked a wrong type foo.")

    def flatter(input_list):
        try:
            flatList = [item for elem in input_list for item in elem]
            return flatList

        except TypeError:
            print("U pick a wrong type, foo. Please check a input type")
        