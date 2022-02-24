from collections import defaultdict

a_dir = '../2021-hashcode-practice/input/a_an_example.in.txt'
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
      print("C, P")
      print(C, P)
      # c lines: descriptions of contributors
      x = 1
      for cindex in range(1, C+1):
        temp = lines[x].split()
        name = temp[0]
        contributorDict[name] = []
        x += 1
        for s in range(1, int(temp[1])+1):
          cTup = lines[x].split()
          contributorDict[name].append((cTup[0], cTup[1]))
          x += 1
      print(contributorDict)
      
      # p lines: describe projects
      for pindex in range(P):
        temp = lines[x].split()
        x += 1
        tempList = []
        for t in range(1, int(temp[4])+1):
          temp2 = lines[x].split()
          tempList.append((temp2[0], temp2[1]))
          x += 1
        projectDict[temp[0]] = project(temp[1], temp[2], temp[3], tempList)
        print(temp[0], projectDict[temp[0]].duration, projectDict[temp[0]].score, projectDict[temp[0]].bestbefore, projectDict[temp[0]].roles)

if __name__=="__main__":
    readInput()
    # simulation()



expected_output = 
# expected_output = ['3',"WebServer","Bob Anna","Logging","Anna","WebChat","Maria"]

for expected_output = 'D:\Hashcode team\2021-hashcode-practice\Park sangeon\output.txt'

complete_flag = True
day = 0
while(complete_flag):
    day +=1
    
