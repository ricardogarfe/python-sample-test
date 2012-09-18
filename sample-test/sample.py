'''
Created on 13/09/2012

@author: ricardo
'''

friends = ['jhon', 'lol', 'tom']

for i, name in enumerate(friends):
    print "iteration {iteration} is {name}".format(iteration=i, name=name)