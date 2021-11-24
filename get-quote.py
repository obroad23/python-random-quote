import random
def robert():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  n = len(quotes)-1
  rn = random.randint(0,n)
  print(rn,quotes[rn])

if __name__== "__main__":
  robert()
