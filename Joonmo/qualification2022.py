from collections import defaultdict
from doctest import OutputChecker

# a_dir = '../2021-hashcode-practice/input/a_an_example.in.txt'
a_dir = '../2021-hashcode-practice/input/b_better_start_small.in.txt'

class project:
  def __init__(self, d, s, b, r):
    self.duration = d
    self.score = s
    self.bestbefore = b
    self.roles = r
    self.listOfAssignedContributors = []
    
contributorDict = defaultdict()
projectDict = defaultdict()

C = None
P = None


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
        # temp[0] is project name
        projectDict[temp[0]] = project(temp[1], temp[2], temp[3], tempList)
        print(temp[0], projectDict[temp[0]].duration, projectDict[temp[0]].score, projectDict[temp[0]].bestbefore, projectDict[temp[0]].roles)


def simulationNative():
  from collections import OrderedDict
  listOfWaitingProjectOBJs = list(projectDict.keys())
  listOfWorkingProjectOBJs = []
  listOfWaitingContributors = list(contributorDict.keys())
  listOfWorkingContributors = []
  outputDict = OrderedDict()
  
  # projectCounter = len(listOfWaitingProjectOBJs)
  # while  projectCounter != 0:
  for  P in listOfWaitingProjectOBJs:
    # Look into project
    
    # if contributor's skillset is in project role
    # ex) Bob': [('HTML', '5'), ('CSS', '5')]
    demandRoles = list(projectDict[P].roles)
    print("\n\n")
    print("Project", P)
    print("this project demandRoles: ", demandRoles )
    # print("contributorsDict", contributorDict[C])
    demandRolesCounter = len(demandRoles)
    for demandSkillSet in demandRoles:
      for C in listOfWaitingContributors:
        # print("contributorDict[C]", contributorDict[C])
        # print("demandSkillSet", demandSkillSet)
        # print("\n")
        for skillset in contributorDict[C]:
          if demandSkillSet[0] == skillset[0] and demandSkillSet[1] <= skillset[1]:
            print("HEre")
            print("skillset[C]", skillset)
            print("demandSkillSet", demandSkillSet)
            # demandRoles.remove(demandSkillSet)
            demandRolesCounter -= 1
            listOfWaitingContributors.remove(C)
              #add this contributor into working
            listOfWorkingContributors.append(C)
            projectDict[P].listOfAssignedContributors.append(C)
            
    # print("demandRolesCounter",demandRolesCounter)
    # print("\n\n")
              
    if demandRolesCounter == 0:
      # print("project Ready\n")
      # add as workingProject:
      listOfWorkingProjectOBJs.append(P)
      listOfWaitingProjectOBJs.remove(P)

    # update project
    for P in listOfWorkingProjectOBJs:
      # print("working prject: ", P, " list", projectDict[P].listOfAssignedContributors)
      outputDict[P] = projectDict[P].listOfAssignedContributors
      listOfWorkingProjectOBJs.remove(P)
      listOfWaitingProjectOBJs.append(P)
      
    # update contributor skill level based on project finished
    for C in projectDict[P].listOfAssignedContributors:
      if C in listOfWorkingContributors:
        listOfWorkingContributors.remove(C)
      listOfWaitingContributors.append(C)

  print("output: ")
  print(outputDict.items())
  writeOutput(outputDict)

def writeOutput(outputDict):
  file1 = open("submission.txt", "w")
  file1.write(str(len(outputDict.keys())))
  file1.write("\n")
  for key, values in outputDict.items():
    
    file1.write(key)
    file1.write("\n")
    for v in values:
      file1.write(v)
      file1.write(" ")
    file1.write("\n")
  file1.close()
  
if __name__=="__main__":
    readInput()
    simulationNative()
    # simulation()