

# For UI, I would ultimately want to have a form that accepts two lists (of the same length) of things to match
# and then display another form with those two lists and match rankings.
# Then show the results.

# What the men want
preferences_men = {
    'Ryan' : ['Lizzy', 'Sarah', 'Zoey', 'Danica'],
    'Josh' : ['Sarah', 'Lizzy', 'Danica', 'Zoey'],
    'Blake' : ['Sarah', 'Danica', 'Zoey', 'Lizzy'],
    'Conner' : ['Lizzy', 'Sarah', 'Zoey', 'Danica']
}

# What the women want
preferences_women = {
    'Lizzy' : ['Ryan', 'Blake', 'Josh', 'Conner'],
    'Sarah' : ['Ryan', 'Blake', 'Conner', 'Josh'],
    'Zoey' : ['Conner', 'Josh', 'Ryan', 'Blake'],
    'Danica' : ['Ryan', 'Josh', 'Conner', 'Blake']
}

# (R,L) (J,D) (S,B) (L,Z)
#List of matches [('Ryan', 'Lizzy'), ('Blake', 'Sarah'), ('Josh', 'Danica'), ('Conner', 'Zoey')]

#Current working matches, subject to change
tentative_matches = []

# the men who aren't matched right now.
free_men = []

def init_free_men():
    for man in preferences_men.keys():
        free_men.append(man)

# assign a match for all free men
def stable_matching():
    while len(free_men) > 0:
        for man in free_men:
            begin_matching(man)

# matching algo
def begin_matching(man):
    print('Current Man', man)
    for woman in preferences_men[man]:
        taken_match = [couple for couple in tentative_matches if woman in couple]
        # woman is not taken so match them
        if len(taken_match) == 0:
            tentative_matches.append((man, woman))
            free_men.remove(man)
            print(man, ' is now tentatively matched and engaged to ', woman)
            break
        # woman is taken so now we have to check to see if this current guy is higher up in the list
        elif preferences_women[woman].index(man) < preferences_women[woman].index(taken_match[0][0]):
            print('woman ', woman, ' is taken already, but prefers current man ', man)

            # new guy is engaged
            free_men.remove(man)

            # old guy is now single
            free_men.append(taken_match[0][0])

            # update match to new man
            taken_match[0][0] = man
            break


def main():
    init_free_men()
    stable_matching()
    print('List of matches', tentative_matches)

if __name__ == '__main__':
    main()
