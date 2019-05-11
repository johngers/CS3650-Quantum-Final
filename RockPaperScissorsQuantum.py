# Import essential libraries for IBMQ
from qiskit import IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit
from qiskit import execute
from qiskit.providers.ibmq import least_busy
import operator
import sys

# Prompts the user for input
def userChoice():
    print("\n------This is a game of Rock, Paper, Scissors------\n")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Enter your choice [1-3]: ")
    if choice == "q":
        print("Good bye.")
        sys.exit('User exited the program.')
    try:
        choice = int(choice)
    except ValueError:
        choice = 4	# Input is not a number
    if choice != 1 and choice != 2 and choice != 3:
        print("\nI said between 1 and 3!") # Input isn't 1,2, or 3.
        userChoice()	# Prompt again

    if choice == 1:
        return("Rock")
    elif choice == 2:
        return("Paper")
    elif choice == 3:
        return("Scissors")
    else:
        print("Choice error")
        return("default")

# Runs a game of rock paper scissors
def RockPaperScissors(state):
    if state == '00':  # Rock
        if choice == "Rock":
            return("draw")
        elif choice == "Paper":
            return("win")
        elif choice == "Scissors":
            return("lose")
        else:
            print("How did this happen?")
    elif state == '01':  # Paper
        if choice == "Rock":
            return("lose")
        elif choice == "Paper":
            return("draw")
        elif choice == "Scissors":
            return("win")
        else:
            print("How did this happen?")
    elif state == '10':  # Scissors
        if choice == "Rock":
            return("win")
        elif choice == "Paper":
            return("lose")
        elif choice == "Scissors":
            return("draw")
        else:
            print("How did this happen?")
    elif state == '11':
        return("lose")
    else:
        print('How did this happen?')

# Outputs the quantum computers choice
def quantum(quantumChoice):
    if quantumChoice == "00":
        print("The Quantum Computer chose: Rock")
    elif quantumChoice == "01":
        print("The Quantum Computer chose: Paper")
    elif quantumChoice == "10":
        print("The Quantum Computer chose: Scissors")
    else:
        print("The Quantum Computer chose: Quantum")



#---------------------Program starts here---------------------
choice = userChoice()
while choice == "default":
    print("Please try again: ")
    choice = userChoice()

print("Loading quantum opponent...")

# load IBM Q account
IBMQ.load_accounts()

# Finds the least busy IBM quantum computer to use as the backend
backend = least_busy(IBMQ.backends(simulator=False))
print("The least busy device:", backend.name())


# set up Quantum Register and Classical Register for 2 qubits
q = QuantumRegister(2)
c = ClassicalRegister(2)
# Create a Quantum Circuit
qc = QuantumCircuit(q, c)
qc.h(q)

print("Please wait...")

# Gives the quantum computer 5 times to win a game of rock paper scissors
for i in range(5):
	# Checks the state of the two qubits 1000 times
    job = execute(qc, backend=backend, shots=1000)
	# MapReduces the counts
    result = job.result().get_counts(qc)
	# Chooses the result that occurred the most times
    result = max(result.items(), key=operator.itemgetter(1))[0]
    quantumChoice = result
    result = RockPaperScissors(result)
	# Breaks if the quantum computer wins
    if result == "lose":
        break

# Game is over
print("You chose: " + choice)
if result == "win":
    quantum(quantumChoice)
    print("Wow! You just beat a quantum computer!")
elif result == "lose":
    quantum(quantumChoice)
    print("You lose")
else:
    quantum(quantumChoice)
    print("After all that all you did was tie")
