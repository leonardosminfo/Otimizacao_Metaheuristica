class Instance:
    def __init__(self, filename):

        with open(f"instances/{filename}") as f:
            data = [line for line in f.readlines()]

        self.num_items = data[0]
        self.num_forfeits_pairs = data[1]
        self.budget = int(data[2][5:-2])
        self.items = data[3]
        self.forfeits_pairs = data[4]
        self.weights = data[5]
        self.profits = data[6]
        self.forfeits_costs = data[7]

    def convert_attributes_to_list(self) -> list:

        self.items = list(eval(self.items[5:-2]))
        self.forfeits_pairs = list(eval(self.forfeits_pairs[5:-2]))
        self.weights = list(eval(self.weights[5:-2]))
        self.profits = list(eval(self.profits[5:-2]))
        self.forfeits_costs = list(eval(self.forfeits_costs[5:-2]))
