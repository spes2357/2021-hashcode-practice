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
jkDict = defaultdict() ## for modification
naiveAssignDict = defaultdict() ## to store output
skillsDict = defaultdict() ## pool all levels for skills, only take largest
checkLevelDict = defaultdict() ## check to see the levels

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
        checkLevelDict[name] = []
        x += 1
        for s in range(1, int(temp[1])+1):
          cTup = lines[x].split()
          contributorDict[name].append((cTup[0], cTup[1]))
          checkLevelDict[name].append((cTup[0], cTup[1]))
          x += 1
      # print(contributorDict)
      
      # p lines: describe projects
      for pindex in range(P):
        temp = lines[x].split()
        x += 1
        tempList = []
        # print(temp)
        for t in range(1, int(temp[4])+1):
          temp2 = lines[x].split()
        #   print(lines)
        #   print(lines[x])
          tempList.append((temp2[0], temp2[1]))
          x += 1
        projectDict[temp[0]] = project(temp[1], temp[2], temp[3], tempList)
        # print(tempList)
        print(temp[0], projectDict[temp[0]].duration, projectDict[temp[0]].score, projectDict[temp[0]].bestbefore, projectDict[temp[0]].roles)
        # print(projectDict[temp[0]])

        #######################################################################
        ## output -- JK's
        ## taking Brute Force Approach
        ##
        ## P - number of project
        ##       
        ## dictionaries for later use
        jkDict[temp[0]] = projectDict[temp[0]].roles

      ## need to find which projects can go first
      ## fit all dictionary with name first
      for c_name, c_skills in contributorDict.items():            
        c_idx = 0
        for c_skill, c_level in c_skills:

          ## collect skills and levels for mentor guide
          if c_skill not in skillsDict.keys():
            skillsDict[c_skill] = c_level
          else:
            ## keep only large value
            if int(skillsDict[c_skill]) < int(c_level):
              skillsDict[c_skill] = c_level

          ## loop project sections
          for p_name, p_skills in list(jkDict.items()):
            p_idx = 0 ## locate index
            length = len(p_skills)
            # print(p_name, c_name, idx, c_skill, c_level)
            # print(length)
            if length > 0:
              for skill, level in p_skills:
                # check if skill matches
                # check if level matches
                # print(p_name, c_name, idx, skill, c_skill, level, c_level)
                if (skill == c_skill) and (int(level) <= int(c_level)):
                  # print(p_name, c_name, idx)
                  if p_name not in naiveAssignDict.keys():
                    naiveAssignDict[p_name] = [0 for i in range(length)]
                    naiveAssignDict[p_name][p_idx] = c_name
                    ## remove dictionary list
                    del jkDict[p_name][p_idx]
                  else:
                    naiveAssignDict[p_name][p_idx] = c_name
                    ## remove dictionary list
                    del jkDict[p_name][p_idx]
                  
                  ## do level up
                  if int(level) == int(c_level):
                    # print(c_name, c_idx)
                    # print(contributorDict[c_name][c_idx])
                    contributorDict[c_name][c_idx] = (c_skill, str(int(c_level) + 1))
                    # print(contributorDict[c_name][c_idx])

                    ## check the skills dictionary as well
                    if int(skillsDict[c_skill]) < int(c_level):
                      skillsDict[c_skill] = c_level            

                ### mentor can be used for those that have one level less
                elif (skill == c_skill) and (int(skillsDict[skill]) >= int(level)):
                  if int(c_level) + 1 == int(level):
                    if p_name not in naiveAssignDict.keys():
                      naiveAssignDict[p_name] = [0 for i in range(length)]
                      naiveAssignDict[p_name][p_idx] = c_name
                      ## remove dictionary list
                      del jkDict[p_name][p_idx]
                    else:
                      naiveAssignDict[p_name][p_idx] = c_name
                      ## remove dictionary list
                      del jkDict[p_name][p_idx]

                    ## do a level up
                    contributorDict[c_name][c_idx] = (c_skill, str(int(c_level) + 1))

                    ## check the skills dictionary as well
                    if int(skillsDict[c_skill]) < int(c_level):
                      skillsDict[c_skill] = c_level            
                    

                ## ignore if those 2 conditions are not met
                else:
                  pass

                ## iterate indexes
                p_idx += 1

            else:
              del jkDict[p_name] ## remove keys that are finish assigning
              #   # jkDict = jkDict.copy()

          c_idx += 1 ## iterate indexes for contributors

      print(jkDict)
      print(naiveAssignDict)
      print(skillsDict)
      print(contributorDict)
      print(checkLevelDict)

if __name__=="__main__":
    readInput()
    # simulation()