from sematch.semantic.similarity import WordNetSimilarity

wn_sim = WordNetSimilarity()

#('gun', 'fur', 0.32110056437698753)
w1 = 'gun'
lang1 = 'eng'
w2 = "fur"
lang2 = 'eng'
result = []
# for sim_type in ['path','lch','wup','li','res','lin','jcn','wpath','zhou']:

for sim_type in ['path','wup','li','res','lin','jcn','wpath','zhou']:
    sim = wn_sim.crossl_word_similarity(w1, w2, lang1, lang2, sim_type)
    tmp = {'name': sim_type, 'sim': sim}
    result.append(tmp)
    print(tmp)

avg = (result[0]['sim'] + result[1]['sim'] + result[2]['sim'] + result[3]['sim']/10 + result[4]['sim'] + result[5]['sim'] + result[6]['sim'])/7
print("average from other methods: "+str(avg))


# pip install -Iv smart-open==1.10.0


def zhou_noun_simlex_evaluation():
    from sematch.evaluation import WordSimEvaluation
    from sematch.semantic.similarity import WordNetSimilarity
    evaluation = WordSimEvaluation()
    print evaluation.dataset_names()
    wns = WordNetSimilarity()
    # define similarity metrics
    zhou = lambda x, y: wns.word_similarity(x, y, 'zhou')
    # evaluate similarity metrics
    print evaluation.evaluate_metric('zhou', zhou, 'noun_simlex', save_results=True)
    # performa Steiger's Z significance Test
    print evaluation.statistical_test('zhou', 'path', 'noun_simlex')


zhou_noun_simlex_evaluation()