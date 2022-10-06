class Instance:
    def __init__(self, filename):

        
        with open(f"original_instances/{filename}") as f:
            data = [line for line in f.read().splitlines()]


        X = []
        for i in range(int(data[0].split(" ")[0])):
            X.append(i)

        self.num_items = int(data[0].split(" ")[0])
        self.num_forfeits_pairs = int(data[0].split(" ")[1])
        self.budget = int(data[0].split(" ")[2])
        self.profits = data[1]
        self.weights = data[2]
        self.items = X
        
        fp=[]
        fc=[]
        for i in range(3, (len(data)-1),2):
            fc.append(int(data[i].split(" ")[1]))
            fp.append((int(data[i+1].split(" ")[0]),int(data[i+1].split(" ")[1])))
            
        self.forfeits_pairs=fp
        self.forfeits_costs=fc


    def convert_attributes_to_list(self) -> list:
        self.weights =  list(map(int, self.weights.split(" ")))
        self.profits = list(map(int, self.profits.split(" ")))
        