class CacheSimulatorConfiguration:
    def __init__(self, block_size: int, l1_size: int, l1_assoc: int, l2_size: int, l2_assoc: int, 
                 replacement_policy: int, inclusion_property: int, trace_file: str):
        self.block_size = self.to_int(block_size)
        self.l1_size = self.to_int(l1_size)
        self.l1_assoc = self.to_int(l1_assoc)
        self.l2_size = self.to_int(l2_size)
        self.l2_assoc = self.to_int(l2_assoc)
        self.replacement_policy = self.to_int(replacement_policy)
        self.inclusion_property = self.to_int(inclusion_property)
        self.trace_file = trace_file

    @staticmethod
    def to_int(value):
        try:
            return int(value)
        except (ValueError, TypeError):
            return None


    def display_configuration(self):
        print("\n===== Simulator configuration =====")
        print(f'Block Size:            {self.block_size}')
        print(f'L1 Size:               {self.l1_size}')
        print(f'L1 Associativity:      {self.l1_assoc}')
        print(f'L2 Size:               {self.l2_size}')
        print(f'L2 Associativity:      {self.l2_assoc}')
        if self.replacement_policy == 0:
            print('Replacement Policy:    LRU')
        elif self.replacement_policy == 1:
            print('Replacement Policy:    FIFO')
        if self.inclusion_property == 1:
            print('Inclusion Property:    Inclusive')
        else:
            print('Inclusion Property:    Non-inclusive')
        print('Trace File:            ' + self.trace_file)
