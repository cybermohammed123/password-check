#CREATE A PASSWORD CHECKER A DETIAL ABOUT HOW STRONG IS YOUR PASSWORD


#THE IMPORTS (WILL EXPLAIN LATER)
from zxcvbn import zxcvbn
from getpass import getpass
import bcrypt

#A MAIN FUNCTION FOR THE DETIAL
def check_how_powerful(passw):
    #NOW HERE IS THE IMPORTANT PART THE FUNCTION (ZXCVBN) IS THE FUNCTION THAT GONNA RETURN THE WHOLE DETIAL ABOUT THE PASSWORD
    #JUST TYPE ZXCVBN(THE PASSWORD THAT YOU WANT TO CHECK) AND ITS GONNA RETURN A WHOLE DETIAL ABOUT EVERYTHING ABOUT THE PASSWORD 
    #SO WHY THE REST OF THE CODE?
    #THE PROBLEM IS THAT IT RETURN WAY TOO MUCH INFORMATION WE DONT WANNA OVERWHELM THE USER WE ONLY WANT THE IMPORTANT RESULT TO SHOW
    resp = zxcvbn(passw)
    #SNICE THE ZXCVBN RETURN A FORMAT OF CSV RESPONSE WE ARE GONNA A CREATE A FUNCTION THAT RETURN THE VALUE OF THE CALLING KEY THIS TIME IS THE SCORE
    score = resp['score']
    #ITS ACTUALLY GONNA RETURN A NUMBERS FROM 0 TO 4 AND DEPENDS ON THE NUMBER IS HOW POWRFULL THE PASSWORD IS
    #3 BASICALLY MEAN GOOD BUT NOT PERFECT
    
    if score == 3:
        #AND ALSO YOU CAN CREATE YOUR OWN RESPONSE YOU DONT HAVE TO COPY THAT RESPONSE
        response = "good enough but you can make it better"
        #4 MEAN THE PASSWORD IS JUST STRONG TO THE POINT NO ONE CAN GUESS IT
    elif score == 4:
        #SAME THING YOU CAN CREATE YOUR OWN RESPONSE
        response = "perfect password no one can guess it"
        #AND ELSE THE SCORE WAS NOT 3 OR 4 THEN WE HAVE A PROPLEM AND THE FUNCTION WILL ADD A FEEDBACK AND WARINING
    else:
        #CREATE A VALUE THE THAT GONNA RETURN THE FEEDBACK RESPONSE
        feedb = resp["feedback"]
        #SAME THING FOR THE WARNINING
        warn = feedb["warning"]
        #AND ONE FOR THE SUGGESTION
        suggestion = feedb["suggestions"]
        #AND SAME THING ABOUT THE RESPONSE IN THE 4 AND 3 RESULT WRITE YOUR OWN BUT HERE IS WHAT I DID
        #CREATE A WARINING + SHOW THE SCORE IN STR ALSO WIRTE A NEWLINE + SHOW THE WARNING
        response = "change it now" + " " + f"\nrating:{str(score)}" + f"\nwarning:{warn}"


        #AND FOR THE SUGGESTION ITS FOR LOOP SINCE ITS TWO VALUE THAT SEPERATED BY COMA ,

        for sug in suggestion:
            response += " " + sug
    return response
    
#THIS NEXT TWO VALUE ABOUT CREATING A SALT (HASH) TO COMPARE IT LATTER WITH THE PASSWORD FOR RECHECK
def hash_pass(passs):
    salt = bcrypt.gensalt()
    has = bcrypt.hashpw(passs.encode(), salt)
    return has
#THIS FOR RECHECK
def verifuy_password(asass, has):
    if bcrypt.checkpw(asass.encode(), has):
        return "check complete"
    else:
        return "try again"
#THIS IS WHILE LOOP THAT WILL NOT END ENLESS YOU WRITE A GOOD PASSWORD
while True:
   #WE ASK THE THE USER TO WRITE HIS PASSWORD BUT WE DIDNT USE THE INPUT FUNCTION INSTEAD A FUNCTION CALLED GETPASS WHY?
   #INPUT RETURN THE PASSWORD OR ANYTHING IN PLAIN TEXT GETPASS IS BETTER IN THESE TYPE OF INPUT
   password_input = getpass("ENTER A PASSWORD AND SEE HOW STRONG IT IS :")
   the_result = check_how_powerful(password_input)
   print(the_result)
   #IF THE FUNCTION START WITH CHANGE OR ANY THING YOU WRITE IN THE RESPONSE UNDER THE ELSE CATEGORY ABOVE
   #THAT MEAN THAT THE PASSWORD IS UNDER THE 2 1 0 SCORE WHICH IS WEAK SO THE LOOP IS NOT FINISHED
   if the_result.startswith("change"):
       print("try a stronger one")
    #ELSE WHICH 3 OR 4 ITS A GOOD PASSWORD SO END THE LOOP
   else:
       break
#THIS FOR CREATING A HASHE
hase = hash_pass(password_input)
print(f"the hash value is {hase}")

#AND THIS FOR CHECKING IF THE HASH MATCH
rewrite = getpass("ENTER THE SAME PASSWORD")
print(verifuy_password(rewrite, hase))


