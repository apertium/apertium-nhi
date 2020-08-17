cd ..
head=`grep -nH 'LEXICON Root' apertium-nhi.nhi.lexc  | cut -f2 -d':'`

for tag in `cat apertium-nhi.nhi.lexc | grep -o '%<[^>]\+%>' | sort -u`;  do
	found=`head -n $head apertium-nhi.nhi.lexc | grep "$tag" | wc -l`
	if [[ $found -eq 0 ]]; then
		echo "$tag                         !";
	fi
done

for tag in `cat apertium-nhi.nhi.lexc | grep -o '%{[^}]\+%}' | sort -u`;  do
	found=`head -n $head apertium-nhi.nhi.lexc | grep "$tag" | wc -l`
	if [[ $found -eq 0 ]]; then
		echo "$tag                         !";
	fi
done
