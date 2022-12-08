def Choose_Option():
    choices = ['rock', 'paper','scissors','lizard', 'spock']
print ('Enter 0 for rock\n' )
print ('Enter 1 for paper\n')
print ('Enter 2 for scissors\n')
print ('Enter 3 for lizard\n')
print ('Enter 4 for spock\n')
choice = int(input('Enter your choice:'))
if (choice == 0):
    print ("rock")  
if (choice == 1):
    print ("paper")
if (choice == 2):
    print ("scissors")
if (choice == 3):
    print ("lizard")
if (choice == 4):
    print ("spock")