import random



def main():
	print("Dobar dan ja sam {ERROR: NO NAME FOUND}.")
	
	run = True
	
	while run:
		chat = input(">>> ").lower()
		
		if chat == "izlaz" or chat == "stop":
			
			print("Jesi li siguran da želiš izaći? (da/ne)")
			chat = input("da/ne >>> ").lower()
			
			if chat == "da":
				
				run = False
				
	quit()



main()