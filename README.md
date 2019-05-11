RockPaperScissorsQuantum.py README
Creator: John Gers

Initial Steps:
1. 	Run the following command to setup an Anaconda environment:
	
	conda create -n name_of_my_env python=3

	Press y to proceed

2. 	Activate the environment with this command:
	
	source activate name_of_my_env

3. 	Install the necessary package:
	
	pip install qiskit

4. 	Run the program with the following command:
	
	python RockPaperScissorsQuantum.py

POTENTIAL PROBLEM:
If you are not authorized to use the IBM Quantum Computer, then you will have to make an account and acquire the api token. Then you will have to add the following line of code to the python file before line 94 where the account is loaded.

	IBMQ.save_account('MY_API_TOKEN',overwrite=true)

Running it at a later time: 
1. 	Activate the environment with this command:	
	
	source activate name_of_my_env

2. 	Run the program with the following command:	
	
	python RockPaperScissorsQuantum.py

Sample output:

<img width="682" alt="Output" src="https://user-images.githubusercontent.com/45726943/57564519-cd021b00-7361-11e9-85a2-5feed48454a2.png">
