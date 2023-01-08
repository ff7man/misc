# converted to python from jbedford128's javascript 
# https://forums.qhimm.com/index.php?topic=21282.0

#probability of succeeding a roll (win, loss)
def prob(w,l):
  return 1/(w+l)*w

def binomial(n, k):
  coeff = 1
  for x in range(n-k+1,n+1):
    coeff *= x
  for x in range(1,k+1):
    coeff /= x
  return coeff

#probability of rolling r number of successes at p probablity with n number of dice
def P(n, r, p):
  return binomial(n,r) * pow(p,r) * pow((1-p),(n-r))

#probability of rolling /at least/ r at p with n
def Pplus(n, r, p):
  out = 0
  for i in range(r,n+1):
    out += P(n, i, p)
  return out

def battler():
  opponents = [
    [120, 62],
    [ 87, 83],
    [ 64,128],
    [ 64,192]
  ]
  rolls = 19
  wins = 10
  stack = 1
  
  for i in range(0,len(opponents)): 
    p = prob(opponents[i][0], opponents[i][1])
    success = Pplus(rolls,wins,p)
    stack *= success
    print(str(success*100)+" "+str(stack*100))
    
battler()
