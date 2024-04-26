from stack import Stack
from node import Node

class Hanoi_setup():
    def __init__(self):
        self.num_disks = None

    def create_stacks(self):
        #create the empty stacks and list of stacks, set limit for stacks to number of disks
        self.left_stack = Stack("left", self.num_disks)
        self.middle_stack = Stack("middle", self.num_disks)
        self.right_stack = Stack("right", self.num_disks)

        self.stacks = []
        self.stacks.append(self.left_stack)
        self.stacks.append(self.middle_stack)
        self.stacks.append(self.right_stack)

        self.choices = [stack.get_name()[0].upper() for stack in self.stacks]

        #create disks with decreasing values and push onto stack 1
        for i in range(self.num_disks, 0, -1):
            self.left_stack.push(i)

    #get user input for number of disks
    def get_user_disk_input(self):
        while self.num_disks == None:
            user_disk_input = input("\nHow many disks will you play with?\n")
            try:
                if int(user_disk_input) < 3:
                    print("\n\n>>>Please enter a number greater than or equal to three<<<")
                    pass
                else:
                    self.num_disks = int(user_disk_input)
                    break
            except:
                print("\n\n>>>Please enter a number<<<")
                pass
    
    #prints directions for input
    def input_hint(self):
        for i in range(len(self.stacks)):
            print("Enter {l} for the {s} stack.".format(l=self.choices[i], s=self.stacks[i].get_name()))

    #returns number of optimal moves
    def optimal_moves(self):
        self.optimal_moves_num = (2**self.num_disks)-1
        print("\nThe optimal number of moves for {d} disks is {n}.\n".format(d=self.num_disks, n=self.optimal_moves_num))
        return self.optimal_moves_num

    #displays stacks and their contents
    def print_stacks(self):
        for stack in self.stacks:
            stack_display_name = stack.get_name().title()

            items_in_stack = stack.list_all_values()
            items_in_stack.reverse()

            print(stack_display_name + " Stack: " + str(items_in_stack))
    
class Hanoi_play():
    def __init__(self):
        self.board = Hanoi_setup()
        self.num_turns = 0

    # gets stacks from input, checks input is a valid option from list of stacks
    def user_input(self):
        chosen_stack = None
        while chosen_stack == None:
            user_input = input("").upper()
            if user_input not in self.board.choices:
                print("\n>>>Not a valid option.<<<\n")
                self.board.input_hint()
                pass
            else:
                for i in range(len(self.board.stacks)):
                    if user_input == self.board.choices[i]:
                        chosen_stack = self.board.stacks[i]
                        return chosen_stack
    
    def play(self):
        print("\n~~~~~~Towers of Hanoi~~~~~~\n")

        self.board.get_user_disk_input()
        self.board.optimal_moves()
        self.board.create_stacks()
        
        while self.board.right_stack.has_space():
            print("~~~Current Stacks~~~\n")
            self.board.print_stacks()
            print()
            self.board.input_hint()
            stack_from = None
            while stack_from == None:
                print("\nWhich stack should you like to move a disk FROM?")
                candidate_stack_from = self.user_input()
                if candidate_stack_from.is_empty():
                    print("\n>>>This stack has no disks to move<<<\n")
                    self.board.print_stacks()
                    print()
                    self.board.input_hint()
                else: stack_from = candidate_stack_from
            stack_to = None
            while stack_to == None:
                print("\nWhich stack should you like to move a disk TO?")
                candidate_stack_to = self.user_input()
                if (candidate_stack_to.peek() != None) and (stack_from.peek() > candidate_stack_to.peek()):
                    print("\n>>>You can't place a larger disk onto a smaller disk<<<\n")
                else: stack_to = candidate_stack_to
            if stack_from == stack_to:
                print("\n>>>You placed your disk back on the same stack. This turn won't count<<<\n")
            else:
                disk = stack_from.pop()
                stack_to.push(disk)
                self.num_turns +=1
        self.board.optimal_moves()
        print("You won in {} moves. Good job!".format(self.num_turns))

new_game=Hanoi_play()
new_game.play()
    

