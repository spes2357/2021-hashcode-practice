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


def scoring(C,P,expected_output_from_sim):
    expected_output_from_sim = {"WebServer":["Bob" ,"Anna"],"Logging":["Anna"],"WebChat":["Maria"]}
    
    with open('./Park sangeon/output.txt','w') as f:
        f.write(str(P))
        f.write("\n")
        for project,contributors in expected_output_from_sim.items():
            f.write(project)
            f.write("\n")
            temp = ""
            for contributor in contributors:
                # f.write(contributor)
                temp = "".join(contributor)
            f.write(temp)
            f.write("\n")

        
        
        
    project_assigned = dict()
    
    expected_output = './Park sangeon/output.txt'
    with open(expected_output) as fp:
        lines = fp.readlines()
        key = ''
        for index,line in enumerate(lines):
            index +=1
            if index ==1:
                num_project = line
            elif index%2 == 0:
                line = line.split("\n")
                key = line[0]
            elif index%2 ==1:
                line = line.split()
                # print(line)
                project_assigned[key] = line
    print("project assigned : ",project_assigned)
                
            

    complete_flag = True
    RT_day = 0
    totalscore = 0
    for projectname, members in project_assigned.items():

        duration = int(projectDict[projectname].duration)
        full_score = int(projectDict[projectname].score)
        bestbefore = int(projectDict[projectname].bestbefore)
        roles = projectDict[projectname].roles

        # print("roles : ",roles)
        
        RT_day += duration
        
        #scoring
        if RT_day > bestbefore:
            minus_point = RT_day - bestbefore
            if minus_point > full_score:
                score = 0
            else :
                score = full_score - minus_point
            totalscore += score 
        else:# day not pass best before
            totalscore += full_score
        print(totalscore)
    # # level up procedure
    # for role in roles:
    #     print(roles[0][0])
        
    
    # for index,contributor in enumerate(members):
    #     skills = contributorDict[contributor]
    #     print(contributor)
    #     for skill in skills:
    #         skillname = skill[0]
    #         skillLv = skill[1]
    #         if role[index][0] == skillname:
    #             if skillLv < 5:
    #                 skillLv += 1
    #                 contributorDict[contributor][0][1]
    #         break
        
    # break
    
if __name__=="__main__":
    expected_output_from_sim = None
    C, P = readInput()
    scoring(C,P,expected_output_from_sim)