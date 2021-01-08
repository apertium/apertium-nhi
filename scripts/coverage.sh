#
# Script to calculate basic coverage metrics for the fst morphological analyzer.
# TODO: do all of this in awk
#

cd ..

#"corpus/tiquitini_ACK.txt corpus/omitlan_1.txt corpus/omitlan_2.txt"
PATH_TO_CORPUS=corpus/tiquitini_ACK.txt

NUM_WORDS=$(cat $PATH_TO_CORPUS | wc -w)
NUM_UNIQUE_WORDS=$(for word in $(cat $PATH_TO_CORPUS); do echo "$word"; done | sort -u | wc -w)
MATCHED=$(for word in $(cat $PATH_TO_CORPUS); do echo "$word"; done | apertium -d . nhi-morph | grep -v '*')
NUM_WORDS_PARSED=$(for word in $MATCHED; do echo "$word"; done | wc -w)
NUM_UNIQUE_WORDS_PARSED=$(for word in $MATCHED; do echo "$word"; done | sort -u | wc -w)

TOKEN_COVERAGE=$(awk -v nparsed="$NUM_WORDS_PARSED" -v ntokens="$NUM_WORDS" 'BEGIN { print nparsed / ntokens ; exit 0}')
TYPE_COVERAGE=$(awk -v nparsed="$NUM_UNIQUE_WORDS_PARSED" -v ntokens="$NUM_UNIQUE_WORDS" 'BEGIN { print nparsed / ntokens ; exit 0}')

echo "Num words in corpus:  $NUM_WORDS"
echo "Num unique words: $NUM_UNIQUE_WORDS"
echo "Token coverage:      $TOKEN_COVERAGE"
echo "Type coverage:       $TYPE_COVERAGE"