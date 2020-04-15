from sematch.semantic.similarity import WordNetSimilarity

wn_sim = WordNetSimilarity()

w1 = 'pies'
lang1 = 'pol'
w2 = 'kot'
lang2 = 'pol'
result = []
sim_type = 'zhou'

tmp = {}
tmp['name'] = sim_type
tmp['sim'] = wn_sim.crossl_word_similarity(w1, w2, lang1, lang2, sim_type)
result.append(tmp)

print(tmp)


