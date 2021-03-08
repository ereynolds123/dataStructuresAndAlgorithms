# A program to determine what to do in a shoulder dystocia (where a babies body gets stuck after the head is delivered)

#Get input of how long the baby has been stuck
timeFromHeadBorn = int(input("How long has the body been stuck? (in seconds): "))

#Control Flow for decision of what to do
def main():
    if timeFromHeadBorn > 150:
        print("The baby has permanent brain damage. Do whatever is necessary to deliver the body.")
    
    elif timeFromHeadBorn >120:
        print("Break the clavicle.")
    
    elif timeFromHeadBorn > 90:
        print("Rotate the shoulder via Rubin maneuver")
    
    elif timeFromHeadBorn > 60:
        print("Do the Gaskins maneuver. ")
    
    elif timeFromHeadBorn > 45:
        print("Hyperflex mother's legs in McRoberts position.")

    else:
        print("Wait patiently.")
main()