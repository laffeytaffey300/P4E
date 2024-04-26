from stack import Stack
from node import Node

print("\n~~~~~~Towers of Hanoi~~~~~~\n")

#get user input for number of disks
num_disks = None
while True:
    user_disk_input = input("\nHow many disks will you play with?\n")
    try:
        if int(user_disk_input) < 3:
            print("\n\n>>>Please enter a number greater than or equal to three.<<<")
            pass
        else:
            num_disks = int(user_disk_input)
            break
    except:
        print("\n\n>>>Please enter a number.<<<")
        pass

#return number of optimal moves
optimal_moves = (2**num_disks)-1

print("\nThe optimal number of moves for {d} disks is {n}.\n".format(d=num_disks, n=optimal_moves))

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

#print directions for input
def input_hint():
    for i in range(len(stacks)):
        #stack_name = stack.get_name()
        #letter = stack_name[0].upper()
        print("Enter {l} for the {s} stack.".format(l=choices[i], s=stacks[i].get_name()))

#display stacks and their contents
def print_stacks():
    for stack in stacks:
        stack_display_name = stack.get_name().title()

        items_in_stack = stack.list_all_values()
        items_in_stack.reverse()

        print(stack_display_name + " Stack: " + str(items_in_stack))


def user_input():
    # get stack from input, check not empty, check option
    while True:
        user_input = input("").upper()
        if user_input not in choices:
            print("\n>>>Not a valid option.<<<\n")
            input_hint()
            pass
        else:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]

#Game play
num_turns = 0
while right_stack.has_space():
    print("~~~Current Stacks~~~\n")
    print_stacks()
    print()
    input_hint()
    while True:
        print("\nWhich stack should you like to move a disk from?")
        stack_from = user_input()
        if stack_from.is_empty():
            print("\n>>>This stack has no disks to move.<<<\n")
            print_stacks()
            print()
            input_hint()
        else: break
    while True:
        print("\nWhich stack should you like to move a disk to?")
        stack_to = user_input()
        if (stack_to.peek() != None) and (stack_from.peek() > stack_to.peek()):
            print("\n>>>You can't place a larger disk onto a smaller disk.<<<\n")
        else: break
    if stack_from == stack_to:
        print("\n>>>You placed your disk back on the same stack. This turn won't count<<<\n")
    else:
        disk = stack_from.pop()
        stack_to.push(disk)
        num_turns +=1
print("You won in {u} moves. The optimal number of moves is {n}. Good job!".format(u=num_turns, n=optimal_moves))


    

