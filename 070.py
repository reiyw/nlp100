# % cat <(sed "s/^/+1 /" rt-polarity.pos) <(sed "s/^/-1 /" rt-polarity.neg) | sort -R > sentiment.txt
# % grep -c '^+1' sentiment.txt
# 5331
# % grep -c '^-1' sentiment.txt
# 5331
