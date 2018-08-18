
class Day:
    def __inti__(self,days,attributes):
        self.days = days
        self.attributes = attributes

class Month:
    
    def __inti__(self):
        self.month = 0
        self.days = {}


class Year:
    
    def __inti__(self):
        self.year = 0
        self.months = {}

class Node:

    def __init__(self):
        self.header_list = []
        self.years = []    
    
    def setHeaderList(self,comma_sep_list):
        self.header_list = comma_sep_list.split(',')
        #print(self.header_list)
    
    def readWholeFile(self):

        # open & read all the file and strip into line by line
        lines = [line.rstrip('\n') for line in open('/home/fahad/Downloads/' +
                                                    'weatherfiles/weatherfiles/Murree_weather_2004_Aug.txt')]
        #print(len(lines))
        #setting the header of the Data structure
        self.setHeaderList(lines[0])

        for i in range(1,31):
            list_of_data = lines[i].split(',')
            year,month,day = list_of_data[0].split('-')

            list_of_attributes = list_of_data[1:len(list_of_data)]
            
            # Making Dictionary from the attributes and tha values 
            dictionary = {}
            for i in range(0,len(list_of_attributes)):
                dictionary.update({self.header_list[i]:list_of_attributes[i]})
            
            #print(str(dictionary))
            single_day = Day(day,dictionary)
        
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
    #obj = WeatherReadings()
    obj = Node()
    obj.readWholeFile()
    

main()
