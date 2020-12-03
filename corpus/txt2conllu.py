import sys, re

sent_id = 1 
prefix = sys.argv[1]

def categorise(token):
	if token.lower() in ['neh', 'yeh']:
			# form, lemma, upos, deprel
		return (token, token.lower(), 'PRON', '_')
	if token in '—.,:;()[]?!¡¿"“”':
		return (token, token, 'PUNCT', 'punct')
	if token.lower() in ['huan', 'pero']:
		return (token, token.lower(), 'CCONJ', '_')
	if token.lower() in ['porque']:
		return (token, token.lower(), 'SCONJ', '_')
	if token.lower() in ['pues', 'entonces', 'bueno']:
		return (token, token.lower(), 'ADV', '_')

	return (token, '_', '_', '_')

def clean(line):
	o = re.sub(' ([,\.?!])', '\g<1>', line)
	return o

# Maybe better to do this another way?
perfective_exclusion = ['omitlán', 'occiqui', 'occe', 'oc', 'o', 'ohcon', 'ohcón', 'ome', 'ompa']

for line in sys.stdin.readlines():
	line = line.strip()
	print('# sent_id = %s:%d' % (prefix, sent_id))
	print('# text = %s' % clean(line))
	print('# text[spa] = ')
	print('# labels = partial')
	idx = 0
	for token in line.split(' '):
		if token.strip() == '':
			continue
		upos = xpos = '_'
		feats = deprels = '_'
		head = deprel = '_'
		misc = lemma = '_'

		(token, lemma, upos, deprel) = categorise(token)

		if token[0].lower() == 'o' and token.lower() not in perfective_exclusion:
			print('%d-%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_' % (idx+1, idx+2, token))
			print('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (idx+1, token[0], 'o', 'AUX', xpos, feats, head, 'aux', deprels, misc))
			print('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (idx+2, token[1:], lemma, 'VERB', xpos, feats, head, deprel, deprels, misc))
			idx += 2
		else:	
			print('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (idx+1, token, lemma, upos, xpos, feats, head, deprel, deprels, misc))
			idx += 1
	print()
	sent_id += 1
