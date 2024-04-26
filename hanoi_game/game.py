from stack import Stack
from node import Node

### Functions

#returns number of optimal moves
def optimal_moves():
    optimal_moves = (2**num_disks)-1
    print("\nThe optimal number of moves for {d} disks is {n}.\n".format(d=num_disks, n=optimal_moves))

#prints directions for input
def input_hint():
    for i in range(len(stacks)):
        #stack_name = stack.get_name()
        #letter = stack_name[0].upper()
        print("Enter {l} for the {s} stack.".format(l=choices[i], s=stacks[i].get_name()))

#displays stacks and their contents
def print_stacks():
    for stack in stacks:
        stack_display_name = stack.get_name().title()

        items_in_stack = stack.list_all_values()
        items_in_stack.reverse()

        print(stack_display_name + " Stack: " + str(items_in_stack))

# gets stacks from input, checks input is a valid option from list of stacks
def user_input():
    chosen_stack = None
    while not chosen_stack:
        user_input = input("").upper()
        if user_input not in choices:
            print("\n>>>Not a valid option.<<<\n")
            input_hint()
            pass
        else:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    chosen_stack = stacks[i]
                    return chosen_stack


print("\n~~~~~~Towers of Hanoi~~~~~~\n")

#get user input for number of disks
num_disks = None
while not num_disks:
    user_disk_input = input("\nHow many disks will you play with?\n")
    try:
        if int(user_disk_input) < 3:
            print("\n\n>>>Please enter a number greater than or equal to three<<<")
            pass
        else:
            num_disks = int(user_disk_input)
            break
    except:
        print("\n\n>>>Please enter a number<<<")
        pass
optimal_moves()

#create the empty stacks and list of stacks, set limit for stacks to number of disks
left_stack = Stack("left", num_disks)
middle_stack = Stack("middle", num_disks)
right_stack = Stack("right", num_disks)

stacks = []
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

choices = [stack.get_name()[0].upper() for stack in stacks]

#create disks with decreasing values and push onto stack 1
for i in range(num_disks, 0, -1):
    left_stack.push(i)


#Game play
num_turns = 0
while right_stack.has_space():
    print("~~~Current Stacks~~~\n")
    print_stacks()
    print()
    input_hint()
    stack_from = None
    while not stack_from:
        print("\nWhich stack should you like to move a disk FROM?")
        candidate_stack_from = user_input()
        if candidate_stack_from.is_empty():
            print("\n>>>This stack has no disks to move<<<\n")
            print_stacks()
            print()
            input_hint()
        else: stack_from = candidate_stack_from
    stack_to = None
    while not stack_to:
        print("\nWhich stack should you like to move a disk TO?")
        candidate_stack_to = user_input()
        if (candidate_stack_to.peek() != None) and (stack_from.peek() > candidate_stack_to.peek()):
            print("\n>>>You can't place a larger disk onto a smaller disk<<<\n")
        else: stack_to = candidate_stack_to
    if stack_from == stack_to:
        print("\n>>>You placed your disk back on the same stack. This turn won't count<<<\n")
    else:
        disk = stack_from.pop()
        stack_to.push(disk)
        num_turns +=1
optimal_moves()
print("You won in {} moves. Good job!".format(num_turns))


    

