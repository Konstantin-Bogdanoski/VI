my_data=[['slashdot','USA','yes',18,'None'],
        ['google','France','yes',23,'Premium'],
        ['digg','USA','yes',24,'Basic'],
        ['kiwitobes','France','yes',23,'Basic'],
        ['google','UK','no',21,'Premium'],
        ['(direct)','New Zealand','no',12,'None'],
        ['(direct)','UK','no',21,'Basic'],
        ['google','USA','no',24,'Premium'],
        ['slashdot','France','yes',19,'None'],
        ['digg','USA','no',18,'None'],
        ['google','UK','no',18,'None'],
        ['kiwitobes','UK','no',19,'None'],
        ['digg','New Zealand','yes',12,'Basic'],
        ['slashdot','UK','no',21,'None'],
        ['google','UK','yes',18,'Basic'],
        ['kiwitobes','France','yes',19,'Basic']]

test_cases=[['google','MK','no',24,'Unknown'],
            ['google','MK','no',15,'Unknown'],
            ['digg','UK','yes',21,'Unknown'],
            ['digg','UK','no',25,'Unknown']]

# my_data=[line.split('\t') for line in file('decision_tree_example.txt')]

class decisionnode:
      def __init__(self,col=-1,value=None,results=None,tb=None,fb=None):
         self.col=col
         self.value=value
         self.results=results
         self.tb=tb
         self.fb=fb

def sporedi_broj(row,column,value):
  return row[column]>=value

def sporedi_string(row,column,value):
  return row[column]==value

# Divides a set on a specific column. Can handle numeric
# or nominal values
def divideset(rows,column,value):
    # Make a function that tells us if a row is in
    # the first group (true) or the second group (false)
    split_function=None
    if isinstance(value,int) or isinstance(value,float): # ako vrednosta so koja sporeduvame e od tip int ili float
       #split_function=lambda row:row[column]>=value # togas vrati funkcija cij argument e row i vrakja vrednost true ili false
       split_function=sporedi_broj
    else:
       # split_function=lambda row:row[column]==value # ako vrednosta so koja sporeduvame e od drug tip (string)
       split_function=sporedi_string

    # Divide the rows into two sets and return them
    # set1=[row for row in rows if split_function(row)]  # za sekoj row od rows za koj split_function vrakja true
    # set2=[row for row in rows if not split_function(row)] # za sekoj row od rows za koj split_function vrakja false
    set1=[row for row in rows if split_function(row,column,value)]  # za sekoj row od rows za koj split_function vrakja true
    set2=[row for row in rows if not split_function(row,column,value)] # za sekoj row od rows za koj split_function vrakja false
    return (set1,set2)

# Create counts of possible results (the last column of
# each row is the result)
def uniquecounts(rows):
  results={}
  for row in rows:
     # The result is the last column
     r=row[len(row)-1]
     if r not in results: results[r]=0
     results[r]+=1
  return results

# Probability that a randomly placed item will
# be in the wrong category
def giniimpurity(rows):
      total=len(rows)
      counts=uniquecounts(rows)
      imp=0
      for k1 in counts:
            p1=float(counts[k1])/total
            for k2 in counts:
                  if k1==k2: continue
                  p2=float(counts[k2])/total
                  imp+=p1*p2
      return imp


# Entropy is the sum of p(x)log(p(x)) across all
# the different possible results
def entropy(rows):
      from math import log
      log2=lambda x:log(x)/log(2)
      results=uniquecounts(rows)
      # Now calculate the entropy
      ent=0.0
      for r in results.keys():
            p=float(results[r])/len(rows)
            ent=ent-p*log2(p)
      return ent

def buildtree(rows,scoref=entropy):
      if len(rows)==0: return decisionnode()
      current_score=scoref(rows)

      # Set up some variables to track the best criteria
      best_gain=0.0
      best_criteria=None
      best_sets=None
      
      column_count=len(rows[0])-1
      for col in range(0,column_count):
            # Generate the list of different values in
            # this column
            column_values={}
            for row in rows:
                  column_values[row[col]]=1
                  print
            # Now try dividing the rows up for each value
            # in this column
            for value in column_values.keys():
                  (set1,set2)=divideset(rows,col,value)
                  
                  # Information gain
                  p=float(len(set1))/len(rows)
                  gain=current_score-p*scoref(set1)-(1-p)*scoref(set2)
                  if gain>best_gain and len(set1)>0 and len(set2)>0:
                        best_gain=gain
                        best_criteria=(col,value)
                        best_sets=(set1,set2)
      
      # Create the subbranches
      if best_gain>0:
            trueBranch=buildtree(best_sets[0])
            falseBranch=buildtree(best_sets[1])
            return decisionnode(col=best_criteria[0],value=best_criteria[1],
                            tb=trueBranch, fb=falseBranch)
      else:
            return decisionnode(results=uniquecounts(rows))

def printtree(tree,indent=''):
      # Is this a leaf node?
      if tree.results!=None:
            print (str(tree.results))
      else:
            # Print the criteria
            print (str(tree.col)+':'+str(tree.value)+'? ')
            # Print the branches
            print (indent+'T->',)
            printtree(tree.tb,indent+'  ')
            print (indent+'F->',)
            printtree(tree.fb,indent+'  ')


def classify(observation,tree):
    if tree.results!=None:
        return tree.results
    else:
        vrednost=observation[tree.col]
        branch=None

        if isinstance(vrednost,int) or isinstance(vrednost,float):
            if vrednost>=tree.value: branch=tree.tb
            else: branch=tree.fb
        else:
           if vrednost==tree.value: branch=tree.tb
           else: branch=tree.fb

        return classify(observation,branch)

		
(s1,s2)=divideset(my_data,2,'yes') 
(sa1,sa2)=divideset(my_data,0,'google') 
(sb1,sb2)=divideset(my_data,1,'USA') 

#print len(s1),len(s2),uniquecounts(my_data)
#print entropy(my_data),giniimpurity(my_data)
#print entropy(s1),giniimpurity(s1)
#print entropy(s2),giniimpurity(s2)
#t= buildtree(my_data)
# drawtree(t)
#printtree(t)
#for test_case in test_cases:
#    print "Nepoznat slucaj:", test_case, " Klasifikacija: ", classify(test_case,t)