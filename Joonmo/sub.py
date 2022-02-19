from collections import defaultdict

a_dir = './OkieBTS-HashCode2022/input_2021_qualification/a.txt'

class street:
  def __init__(self, s, e, l):
    self.intersectionStart = s
    self.intersectionEnd = e
    self.timeCost = l

class car:
  def __init__(self, l, t):
    self.streetList = l
    self.timeLeftCurrentStreet = t

streetDict = defaultdict()
carDict = defaultdict()

def readInput():
  with open(a_dir) as f:
      lines = f.readlines()
      # d: duration of the simulation
      # i: the number of intersections
      # s: the number of streets
      # v: the number of cars
      # f: - the bonus points for each car that reaches its destination before time D

      D, I, S, V, F = list(int(t) for t in lines[0].split())
      print("D I S V F")
      print(D, I, S, V, F)

      # s lines: descriptions of streets
      for sindex in range(S):
        temp = lines[sindex+1].split()
        streetDict[temp[2]] = street(int(temp[0]), int(temp[1]), int(temp[3]))
      
      print("\nStreets")
      for s in streetDict.keys():
        print(streetDict[s].intersectionStart, streetDict[s].intersectionEnd, s, streetDict[s].timeCost)
      print("\n")

      # v lines: describe the paths of each cars
      for vindex in range(V):
        carDict[vindex] = car(lines[S+vindex+1].split()[1:], None)
      
      print("Cars")
      for cc in carDict.keys():
        print(cc, carDict[cc].streetList, carDict[cc].timeLeftCurrentStreet)
      print("\n")
      # car1 (0, [0, 1, 4, 3]), 4 rue-de-londres => rue-d-amsterdam => rue-de-moscou => rue-de-rome
      # car2 (1, [2, 4, 0]),    3 rue-d-athenes => rue-de-moscou => rue-de-londres





if __name__=="__main__":
    readInput()
    
    