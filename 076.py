# ./baseline.sh sentiment.txt | classias-tag -m sentiment5.model -rap | sed 's/[ :]/\t/g' | tail -5
# -1      -1      0.0733991
# -1      -1      0.0316529
# +1      +1      0.959171
# -1      -1      0.0270869
# +1      +1      0.53369

# baseline.sh は 072.py をシェルスクリプトにしたやつ
