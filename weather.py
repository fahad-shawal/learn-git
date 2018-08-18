class Node:

    def __init__(self):
        self.header_list = [12]
        self.data_list = {"Year" : "Year"}
        self.print_data()
    
    def print_data(self):
        print(self.header_list)
        print(self.data_list)

class WeatherReadings:
        
    def __init__(self):
        node = Node()
        self.reading_header()
        self.reading_data()
    
    def reading_header(self):
        print("Reading Header here!")
        

    def reading_data(self):
        print("Reading data here!")


# Main Function to Execute the logcic of the program
def main():
    obj = WeatherReadings()
    
    

main()
