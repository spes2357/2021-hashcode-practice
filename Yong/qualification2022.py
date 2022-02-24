from collections import defaultdict

a_dir = '../2021-hashcode-practice/input/a_an_example.in.txt'
# a_dir = '../2021-hashcode-practice/input/b_better_start_small.in.txt'
class project:
  def __init__(self, d, s, b, r):
    self.duration = d
    self.score = s
    self.bestbefore = b
    self.roles = r

contributorDict = defaultdict()
projectDict = defaultdict()

def readInput():
  with open(a_dir) as f:
      lines = f.readlines()
	  
      # C: contributors
      # P: projects
	  
      C, P = list(int(t) for t in lines[0].split())
      # print("C, P")
      # print(C, P)
      # c lines: descriptions of contributors
      x = 1
      for cindex in range(1, C+1):
        temp = lines[x].split()
        name = temp[0]
        contributorDict[name] = []
        x += 1
        for s in range(1, int(temp[1])+1):
          cTup = lines[x].split()
          contributorDict[name].append((cTup[0], int(cTup[1])))
          x += 1
      # print(contributorDict)
      
      # p lines: describe projects
      for pindex in range(P):
        temp = lines[x].split()
        x += 1
        tempList = []
        for t in range(1, int(temp[4])+1):
          temp2 = lines[x].split()
          tempList.append((temp2[0], int(temp2[1])))
          x += 1
        projectDict[temp[0]] = project(temp[1], temp[2], temp[3], tempList)
        # print(temp[0], projectDict[temp[0]].duration, projectDict[temp[0]].score, projectDict[temp[0]].bestbefore, projectDict[temp[0]].roles)
  return C, P

def simulation(C, P):
  return C
    # tuple tester
    # for pindex, p in enumerate(projectDict.keys()):
    #   print(projectDict[p].roles)
      
    #   for x in projectDict[p].roles:
    #     for cindex, c in enumerate(contributorDict.keys()):
    #       for cs in contributorDict[c]:
    #         if x[0] == cs[0]:
    #           print(x, cs)
    #           sdc = cs[0]
    #           ttest = cs[1]+1
    #           print(ttest)
    #           contributorDict[c].remove(cs)
    #           contributorDict[c].append((sdc, ttest))
    #           print(contributorDict[c])


    # ccc = 0
    # listofproject = []
    # for pindex, p in enumerate(projectDict.keys()):
    #   print(pindex, p, "RQ roles: ", len(projectDict[p].roles))
    #   counter = 0
    #   for cindex, c in enumerate(contributorDict.keys()):
    #     for r in projectDict[p].roles:
    #       for skill in contributorDict[c]:
    #         if r[0] == skill[0] and int(r[1]) <= int(skill[1]):
    #           counter += 1
    #           # print("Project roles: ", r, c, contributorDict[c])
    #   print("Role filled: " ,counter)
    #   if len(projectDict[p].roles) == counter:
    #     ccc += 1
    #     listofproject.append(p)
    # print(len(projectDict.keys()), ccc)
    # print(listofproject)
        
if __name__=="__main__":
    C, P = readInput()
    simulation(C, P)