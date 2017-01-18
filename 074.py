# % cat 074.sh
# #!/usr/bin/env bash
#
# ./snowball_stemmer.py <(./rm_stopwords.py <(ruby -ane 'puts $F.select {|w| w =~ /^[a-z\-]{3,}$|\+1|-1/}.join(" ")' <(echo $1)) stopwords.txt) | sed 's/^/_ /' | classias-tag -m sentiment5.model -w
# % ./074.sh 'that was an awful movie'
# -1:-1.10032
