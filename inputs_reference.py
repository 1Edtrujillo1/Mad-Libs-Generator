vars_inputs = [["food", "name", "place", "animals",
                "profession", "things", "cloth", "verb"],
               ["person", "color", "foods", "adjective", "thing",
                "place", "verb", "adverb", "food", "things"]]

inputs1 = ['food'] + ['Enter ' + i for i in ["a", "a place", "an animal",
                                             "a profession", "a thing", "a piece of cloth",
                                             'a verb in ing form: ']]
inputs1[0:-1] = [i + ' name: ' for i in inputs1[0:-1]]

inputs2 = [i + " name: "
           for i in ["Enter " + i
                     for i in ["a person", "a color", "food", "an adjective", "a thing",
                               "a place", "a verb", "an adverb", "a food", "a thing"]]]

inputs = [inputs1, inputs2]


def specific_dic(vars, elements):
    dic = {}
    for i in range(0, len(vars)):
        dic[vars[i]] = input(elements[i])

    dic = list(dic.values())

    return dic


# final_dic = list(map(lambda vars, elements:
#                      specific_dic(vars=vars, elements=elements),
#                      vars_inputs, inputs))