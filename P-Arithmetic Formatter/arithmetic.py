def formatter(items, a=None):
  if len(items) > 5:
    return "Error: Too many problems."

  finalString = ""
  fStr = ""
  sStr = ""
  tStr = ""
  foStr = ""

  for x in items:

    if x.split()[1] == "*" or x.split()[1] == "/":
      return "Error: Operator must be '+' or '-'."
      
    if x.split()[0].isdigit() == False or x.split()[2].isdigit() == False:
      return "Error: Numbers must only contain digits."  

    if len(x.split()[0]) > 4 or len(x.split()[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    space = len(x.split()[0]) if len(x.split()[0]) > len(x.split()[2]) else len(x.split()[2])
    fStr += ("{:>1}" + "{}").format(x.split()[0].rjust(space+2), (" ")*4)
    sStr += ("{}" + "{:>1}" + "{}").format(x.split()[1], x.split()[2].rjust(space+1), (" ")*4)
    tStr += ("{}" + "{}").format(("-")*(space+2), (" ")*4)
    total = 0
    if x.split()[1] == "+":
      total = int(x.split()[0]) + int(x.split()[2])
    else:
      total = int(x.split()[0]) - int(x.split()[2])
    foStr += ("{:>1}" + "{}").format(str(total).rjust(space+2), (" ")*4)

  finalString = fStr[:-4] + "\n" + sStr[:-4] + "\n" + tStr[:-4] 

  if a == True:
    finalString += "\n" + foStr[:-4]

  return finalString