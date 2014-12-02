import matplotlib.pyplot as plt
from recommendations import critics
from itertools
# Returns a distance-based similarity score for person1 and person2
def sim_distance(prefs,person1,person2):
      # Get the list of shared_items
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
      # if they have no ratings in common, return 0
    if len(si)==0: return 0
    # Add up the squares of all the differences
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2)
                        for item in prefs[person1] if item in prefs[person2]])
    return 1/(1+sum_of_squares)
    
#My implementation of how to determine the best distances
comb_dict={}
for k1 in critics.keys():
    for k2 in critics.keys():
        k3 = k1+','+k2
        if k1<>k2 and k3 not in comb_dict:
            comb_dict[k3]= sim_distance(critics,k1,k2)
#print comb_dict
#print range(len(comb_dict))

 # Returns the best matches for person from the prefs dictionary.
     # Number of results and similarity function are optional params
def topMatches(prefs,person,n=5,similarity=sim_distance):
    scores=[(similarity(prefs,person,other),other)
    for other in prefs if other!=person]
# Sort the list so the highest scores appear at the top scores.sort( )
    scores.reverse( )
    return scores[0:n]
    
##print topMatches(critics, 'Toby',10)

plt.bar(range(len(comb_dict)), comb_dict.values(), align='center')
plt.xticks(range(len(comb_dict)), comb_dict.keys())
plt.yscale(u'linear')
plt.show()
