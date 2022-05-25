#!/dev/usr python


#  Dump data into CSV

class Build():

    def __init__(self):
        pass

    def build_data(self,data):
        header:list = []
        new_data:list = []
        for key in data[0].keys():
            header.append(key)
        for record in data:
            new_data.append(record.values())
        #return (header,new_data)
        data = []
        return new_data
        
