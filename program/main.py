import random



def main(): # Main

	print("Dobar dan ja sam {ERROR: NO NAME FOUND}.")
	
	run = True
	
	while run:

		chat = input(">>> ").lower()
		
		if chat == "izlaz" or chat == "stop":
			
			print("Jesi li siguran da želiš izaći? (da/ne)")
			chat = input("da/ne >>> ").lower()
			
			if chat == "da":
				
				run = False

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



	quit()



main()