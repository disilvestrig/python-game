def readfile(fileName):
  out = []
  file = open(fileName)
  r = file.readlines()
  file.close()

  for e in r:
    out.append(e.replace("\n", "#"))
  l = len(out)
  s = ""
  for i in range (l):
    s += out[i]

  return s
def colorprint(stringa):

#Definizione colori background
  BBLACK = "\033[40m"  #NERO
  BRED = "\033[41m"    #ROSSO
  BGREEN = "\033[42m"  #VERDE
  BYELLOW = "\033[43m" #GIALLO
  BBLUE = "\033[44m"   #BLU
  BMAGENTA = "\033[45m"#MAGENTA
  BACQUA = "\033[46m"  #ACQUA
  BWHITE = "\033[47m"    #BIANCO

#Definizione colori foreground
  BLACK = "\033[30m"   #NERO
  RED = "\033[31m"     #ROSSO
  GREEN = "\033[32m"   #VERDE
  YELLOW = "\033[33m"  #GIALLO
  BLUE = "\033[34m"    #BLU
  MAGENTA = "\033[35m" #MAGENTA
  ACQUA = "\033[36m"   #ACQUA
  WHITE = "\033[37m"   #BIANCO

  COL_DEFAULT = "\033[0m"
  BOLD_T = "\E[0;1m"
  if stringa == "[G]":
    print("%s[G]%s" %(ACQUA,COL_DEFAULT),end = "")
  elif stringa == "[ ]":
    print("%s[ ]%s" %(GREEN,COL_DEFAULT),end = "")
  elif stringa == "[=]":
    print("%s[=]%s" %(YELLOW,COL_DEFAULT),end = "")
  elif stringa == "None":
    print()




