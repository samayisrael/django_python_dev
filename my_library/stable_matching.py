class StableMatching(object):
    def __init__(self):
        # For UI, I would ultimately want to have a form that accepts two lists (of the same length) of things to match
        # and then display another form with those two lists and match rankings.
        # Then show the results.

        # What the men want
        self.preferences_men = {
            'Ryan' : ['Lizzy', 'Sarah', 'Zoey', 'Danica'],
            'Josh' : ['Sarah', 'Lizzy', 'Danica', 'Zoey'],
            'Blake' : ['Sarah', 'Danica', 'Zoey', 'Lizzy'],
            'Conner' : ['Lizzy', 'Sarah', 'Zoey', 'Danica']
        }

        # What the women want
        self.preferences_women = {
            'Lizzy' : ['Ryan', 'Blake', 'Josh', 'Conner'],
            'Sarah' : ['Ryan', 'Blake', 'Conner', 'Josh'],
            'Zoey' : ['Conner', 'Josh', 'Ryan', 'Blake'],
            'Danica' : ['Ryan', 'Josh', 'Conner', 'Blake']
        }


        # (R,L) (J,D) (S,B) (L,Z)
        #List of matches [('Ryan', 'Lizzy'), ('Blake', 'Sarah'), ('Josh', 'Danica'), ('Conner', 'Zoey')]

        #Current working matches, subject to change
        self.tentative_matches = []

        # the men who aren't matched right now.
        self.free_men = []

        self.init_free_men()
        self.the_result = self.stable_matching()


    def init_free_men(self):
        for man in self.preferences_men.keys():
            self.free_men.append(man)

    # assign a match for all free men
    def stable_matching(self):
        ret_string = ''
        while len(self.free_men) > 0:
            for man in self.free_men:
                ret_string = ret_string + self.begin_matching(man)
        return ret_string

    # matching algo
    def begin_matching(self, man):
        ret_string = 'Current Man ' + man
        #print('Current Man', man)
        for woman in self.preferences_men[man]:
            taken_match = [couple for couple in self.tentative_matches if woman in couple]
            # woman is not taken so match them
            if len(taken_match) == 0:
                self.tentative_matches.append([man, woman])
                self.free_men.remove(man)
                ret_string += man + ' is now tentatively matched and engaged to '+ woman
                ret_string += '<br/>'
                #ret_string += ''.join([&#13;, man, ' is now tentatively matched and engaged to ', woman])
                print(man, ' is now tentatively matched and engaged to g', woman)
                break
            # woman is taken so now we have to check to see if this current guy is higher up in the list
            elif self.preferences_women[woman].index(man) < self.preferences_women[woman].index(taken_match[0][0]):
                    print('woman ', woman, ' is taken already, but prefers current man ', man)

                    # new guy is engaged
                    self.free_men.remove(man)

                    # old guy is now single
                    self.free_men.append(taken_match[0][0])

                    # update match to new man
                    taken_match[0][0] = man
                    break
        return ret_string

'''
    def main():
        #init_free_men()
        #more_info = stable_matching()
        #return 'List of matches21', more_info, tentative_matches

        if __name__ == '__main__':
            main()
            print(self.the_result)
'''
