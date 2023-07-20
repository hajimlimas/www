# www
views.py has 3 major functions 
def (matrix) generates random numbers using "secrets" module of python. 
The numbers are validated with an algorithm which returns either "valid" or "invalid". 
If valid, the next function is called, otherwise, new set of random numbers are generated.

def (sincerity) checks whether the match is actually scheduled. An algorithm returns either "sincere" or "Oops! We detected an error ..." 
If sincere, the next function is called, otherwise, user gets a response in frontend "Oops! We detected an error ..."

def determine_winner(home_team, away_team) uses 5 algorithms tagged formula 1, formula 2, ... formula 5. 
A summary of the 5 formulae returns "home team will win", "away team will win", "it will be a draw" or "sorry, we cannot determine match winner". 

These steps make up the function, def process_form (request).
