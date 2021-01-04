import pandas as pd
from generate_verb_bases_from_stem import generate_stem_lexical_entries

input_file = "../corpus/verbal_stems_to_add.csv"
df = pd.read_csv(input_file)
for _, row in df.iterrows():
    stem = row['stem']
    gloss = row['gloss']
    trans = row['transitivity']

    lexical_entry_lines = generate_stem_lexical_entries(stem,
                                                        gloss=gloss,
                                                        trans=trans)
    print("\n".join(lexical_entry_lines))
    print('\n')