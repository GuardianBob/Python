class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

class DList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val): # added this line, takes a Value
        new_node = SLNode(val)	# create a new instance of our Node class using the given value        
        current_head = self.head        
        new_node.next = current_head
        new_node.prev = None
        if current_head != None:
            current_head.prev = new_node
        self.head = new_node	# SET the list's head TO the node we created in the last step
        return self	                # return self to allow for chaining
    def print_values(self):
        runner = self.head
        p_runner = None
        while (runner != None):
            print(runner.value)
            runner = runner.next 	# set the runner to its neighbor
        return self	                # once the loop is done, return self to allow for chaining
    def add_to_back(self, val):
            if self.head == None:	# if the list is empty
                self.add_to_front(val)	# run the add_to_front method
                return self	# let's make sure the rest of this function doesn't happen if we add to the front
            new_node = SLNode(val)
            runner = self.head
            while (runner.next != None):
                p_runner = runner
                runner = runner.next
            runner.next = new_node	# increment the runner to the next node in the list
            runner.prev = p_runner
            return self                 # return self to allow for chaining

my_list = DList()	# create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!") # chaining, yeah!
# output should be:
# Linked lists
# are
# fun!

my_list.add_to_front("Doubly").print_values()