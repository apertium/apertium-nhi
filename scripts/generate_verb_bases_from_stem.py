import re
from typing import List, Union


class VerbalStem(object):
    def __init__(self, stem: str, transitive: bool = False, es: bool = False):
        self.stem = stem
        self.vowels = ["a", "e", "i", "o", "u"]
        self.cons = "bcdfghjklmnpqrstvwxz"
        self.multi_char_cons = ["ch", "tl", "tz"]
        self.rewritable_multi_char_cons = {"qu": "c", "hu": "uh"}

        self.numVPattern = re.compile("|".join(self.vowels))
        self.n_syl = self.count_syllables()
        self.is_spanish = es
        self.trans = transitive

    def count_syllables(self):
        num_syl = 0
        search_stem = self.stem

        def find_next_vowel(s: str) -> Union[str, None]:
            for i, ch in enumerate(s):
                next_ch = s[i + 1] if i+1 < len(s) else ''

                if ch in self.vowels:
                    vowlen = 1
                    if ch == 'u' and next_ch in 'iae':
                        vowlen += 1
                    char_incr = i + vowlen
                    if char_incr <= len(s):
                        return s[char_incr:]
                    else:
                        return ''
            else:
                return None

        while True:
            search_stem = find_next_vowel(search_stem)
            if search_stem is not None:
                num_syl += 1
            else:
                return max([1, num_syl])

    @property
    def present(self) -> str:
        return self.stem

    @property
    def imperfect(self) -> str:
        if self.stem.endswith('ia'):
            return self.stem[:-2] + "a"
        else:
            return self.present

    @property
    def durative_base(self) -> str:
        stem = self.stem
        if stem.endswith('tta'):
            return stem[:-2] + 'z'

        base2 = self.base2
        if base2.endswith('%{i%}%{H%}'):
            return base2[:-10]
        if base2.endswith('t'):
            return base2[:-1]
        else:
            return base2

    @property
    def base2(self) -> str:
        stem = self.stem
        if self.n_syl == 1:
            if stem.endswith('a'):
                return "{}h".format(stem)

            else:
                #
                # for '-i' verbs, the vowel lengthens here, but since neither
                # IDIEZ nor SEP orthographies represent vowel length,
                # this is just an identity.
                #
                return stem

        elif stem.endswith('ia'):
            #
            # In Classical Nahuatl, this verbs' base 2 stem would end in 'ih'.
            # In nhi the preterite they go from "...ih#" -> "...e#". I use
            # the multichar symbols {i} and {H} in order to enable this
            # phonological process.
            #
            return format(stem[:-2]) + "%{i%}%{H%}"

        elif stem.endswith('oa'):
            return stem[:-1] + "h"

        elif stem.endswith('ca'):
            return stem

        elif stem.endswith('hua'):
            if self.trans:
                if stem[-4] in self.vowels:
                    return "{}uh".format(stem[:-3])
                else:
                    return stem[:-3]
            else:
                return stem

        elif stem[-2:] in ('ma', 'mi'):
            return "{}n".format(stem[:-2])

        elif stem.endswith('ya'):
            return "{}x".format(stem[:-2])

        elif stem[-1] in ('a', 'i'):
            #
            # Check it is preceded by a single consonant.
            #
            prev_two_graphemes = stem[-3:-1]
            if prev_two_graphemes in self.multi_char_cons:
                return stem[:-1]

            #
            # Or if the two-char cons needs to be rewritten when the vowel is
            # dropped.
            #
            elif prev_two_graphemes in self.rewritable_multi_char_cons:
                return (stem[:-2] +
                        self.rewritable_multi_char_cons[prev_two_graphemes])

            elif stem[-2] in self.cons and stem[-3] in self.vowels:
                return stem[:-1]

            else:
                return stem

        else:
            return stem

    @property
    def base3(self) -> str:
        stem = self.stem
        if stem[-2:] in ('oa', 'ia'):
            return stem[:-1]
        else:
            return stem


def generate_stem_lexical_entries(canonical: str,
                                  transitivity: str = 'iv') -> List[str]:
    if transitivity not in ('iv', 'tv', 'tv2'):
        raise KeyError("`transitivity` must be either iv (intransitive), tv "
                       "(transitive), or tv2 (bitransitive)")

    stem = VerbalStem(canonical)
    all_stems = [stem.present, stem.imperfect, stem.durative_base, stem.base2,
                 stem.base3]
    cont_lexicons = ["PresentTense", "Imperfect", "Durative", "Base2Suffixes",
                     "Base3Suffixes"]

    lexical_entries = [
        "{}%<v%>%<{}%>:{}%>  {};".format(canonical,
                                         transitivity,
                                         stem,
                                         cont_lexicons[i])
        for i, stem in enumerate(all_stems)
    ]
    return lexical_entries
