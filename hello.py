import random 


kekw = """
⠀⠀⠀⠀⠀⢀⣀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢾⣿⣿⣿⣿⣿⣿⣷⡁⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣶⣤⠤⠄⠀⠀⠀⠀⠀⠀
⢀⣀⣀⣀⠀⠀⠉⠙⠿⣷⢬⣦⠀⠀⢺⣿⣿⣿⡛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠿⢿⠟⠛⠛⠓⠀⠀⠀⠀⠁⠁⠀⠀⠀⠀⠙⠓⢐⣶⣿⣿⡿⠿⠿⠿⠿⣶⣦⣄
⠀⠚⠷⠾⠗⠀⢀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠲⠦⠤⣤⣤⡀⠀⠀⠈⠉
⠀⠀⠀⠀⠀⠀⢘⡷⠀⢀⠾⠀⠀⣠⠠⡴⠆⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡀⠀⠀⠀⢀⣴⠟⠁⣰⡏⠀⠀⢠⢷⡻⡇⠀⠀⣌⠓⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀
⣆⠀⠀⢀⣾⠏⣤⣿⣿⣟⣽⣿⣿⣿⣵⣤⣤⣴⣿⢢⢀⠈⠳⠄⠀⠀⠀⠀⠀⠀
⣿⠀⠰⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣤⣷⣦⡀⠢⣄⠀⠀⠀⠀
⡿⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⠁⠀⠀⠀
⡇⢐⠈⢿⣿⣿⣿⣿⡿⠿⣿⣷⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠀⠀⠀
⣿⣌⡄⠈⠛⣟⠛⢻⣧⣤⣼⣿⠿⢿⣿⣿⣿⠿⠿⠿⠿⠿⢿⣿⣿⠋⠉⠀⠀⠀
⣿⣏⠀⠀⠀⠘⠂⠀⢿⣏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡾⠛⠁⠀⠀⠀⠀⠀
⣟⢻⡄⠀⠀⠀⠀⠀⢸⣿⡦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠀⠀⠀⠀⠀⠀⠀⢐
⣧⠘⣷⡀⠀⠀⠀⠀⠀⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

def greatings():
  words = [] 
  file = open('words.txt', 'r')  # this opens word files
  for each in file:  # goes through all of the lines in files 
    each = each.lower()  # this formats the words
    each = each.strip('/n')  # this formats the words
    each = each.strip('\n')  # this formats the words
    words.append(each)  # this store the word back into said array #

  return (words[random.randint(0, len(words))])

