def primary():
  #print("Renamed the primary function")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[13])

if __name__== "__main__":
  primary()
