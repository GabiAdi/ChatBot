import random



<<<<<<< HEAD
def main(): # Main

=======
def main():
>>>>>>> e3a1e0f5d530f46dae1087283379c4241625df17
	print("Dobar dan ja sam {ERROR: NO NAME FOUND}.")
	
	run = True
	
	while run:
<<<<<<< HEAD

=======
>>>>>>> e3a1e0f5d530f46dae1087283379c4241625df17
		chat = input(">>> ").lower()
		
		if chat == "izlaz" or chat == "stop":
			
			print("Jesi li siguran da želiš izaći? (da/ne)")
			chat = input("da/ne >>> ").lower()
			
			if chat == "da":
				
				run = False
<<<<<<< HEAD

		else:

			chatSplit = chat.split()

			toWrite = ""

			with open("program/learn","r") as l:

				toWrite += l.read()
				toWrite += "\n"+chat.lower()

				l.close()

			with open("program/learn","w") as l:

				l.write(toWrite)
				l.close()



=======
				
>>>>>>> e3a1e0f5d530f46dae1087283379c4241625df17
	quit()



main()