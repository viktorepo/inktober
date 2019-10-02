import time
import sys
def print_slow(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.1)

print_slow("Day 2: Mindless\n")
print_slow("What sould we call you?\n")
players_name = raw_input("")
print_slow("Okay, "+players_name+", here we go.\nTranscript:\n\n")
file=open("mindless.txt","r")
text=file.read()
neo_text=text.replace("PLAYERNAME",players_name)
print_slow(neo_text)
print("\n")
