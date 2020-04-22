from sematch.semantic.similarity import WordNetSimilarity

wn_sim = WordNetSimilarity()

w1 = 'gil'
lang1 = 'pol'
w2 = "sowa"
lang2 = 'pol'
result = []
# for sim_type in ['path','lch','wup','li','res','lin','jcn','wpath','zhou']:

for sim_type in ['path','wup','li','res','lin','jcn','wpath','zhou']:
    sim = wn_sim.crossl_word_similarity(w1, w2, lang1, lang2, sim_type)
    tmp = {'name': sim_type, 'sim': sim}
    result.append(tmp)
    print(tmp)

avg = (result[0]['sim'] + result[1]['sim'] + result[2]['sim'] + result[3]['sim']/10 + result[4]['sim'] + result[5]['sim'] + result[6]['sim'])/7
print("average from other methods: "+str(avg))

