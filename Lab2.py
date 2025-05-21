#I want this program to do a few things including asking the user their name, age, and birthplace.
#First, I want it to ask the user for their name "What's your name?", then for it to say, "Hi, NAME" back where NAME is the user's actual name
#Second, I want it to ask the user for their age "What's your age?", then for it to say, "Congratulations for being AGE, you are so old!" back where AGE is the user's actual age
#Third, I want it to ask the user for their birthplace, "Where were you born?", then for it to say, "Damn you were born in BIRTHPLACE, I am so sorry!" back where BIRTHPLACE is the user's actual birthplace
#Step 1, ask user what their name is
print("What's your name?")
#Step 2, input user's name on the keyboard
username = input()
#Step 3, say "Hi" back using the user's name
print("Hi "+ username)
#Step 4, ask user what their age is
print("What's your age?")
#Step 5, input user's age on the keyboard
userage = input()
#Step 6, set age as userage with integer value and say "Congratulations for being , you are so old!" back using the user's age
age = userage
print("Congratulation for being " + str(age) + " , you are so old!")
#Step 7, ask user what their birthplace is
print("Where were you born?")
#Step 8, input user's birthplace on the keyboard
userbirthplace = input()
#Step 9, say "Damn you were born in, I am so sorry!" back using the user's birthplace
print("Damn you were born in " + userbirthplace + " , I am so sorry!")