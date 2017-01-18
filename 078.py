# % split -l 2132 sentiment5.txt sentiment5.
#
# % classias-train -tb -a lbfgs.logistic -m sentiment5_abcd.model sentiment5.aa sentiment5.ab sentiment5.ac sentiment5.ad
# % classias-train -tb -a lbfgs.logistic -m sentiment5_abce.model sentiment5.aa sentiment5.ab sentiment5.ac sentiment5.ae
# % classias-train -tb -a lbfgs.logistic -m sentiment5_abde.model sentiment5.aa sentiment5.ab sentiment5.ad sentiment5.ae
# % classias-train -tb -a lbfgs.logistic -m sentiment5_acde.model sentiment5.aa sentiment5.ac sentiment5.ad sentiment5.ae
# % classias-train -tb -a lbfgs.logistic -m sentiment5_bcde.model sentiment5.ab sentiment5.ac sentiment5.ad sentiment5.ae
#
# % cat sentiment5.ae | classias-tag -m sentiment5_abcd.model -qt
# Accuracy: 0.7523 (1604/2132)
# Micro P, R, F1: 0.7632 (809/1060), 0.7449 (809/1086), 0.7540
# % cat sentiment5.ad | classias-tag -m sentiment5_abce.model -qt
# Accuracy: 0.7533 (1606/2132)
# Micro P, R, F1: 0.7560 (784/1037), 0.7417 (784/1057), 0.7488
# % cat sentiment5.ac | classias-tag -m sentiment5_abde.model -qt
# Accuracy: 0.7514 (1602/2132)
# Micro P, R, F1: 0.7402 (789/1066), 0.7572 (789/1042), 0.7486
# % cat sentiment5.ab | classias-tag -m sentiment5_acde.model -qt
# Accuracy: 0.7477 (1594/2132)
# Micro P, R, F1: 0.7507 (810/1079), 0.7507 (810/1079), 0.7507
# % cat sentiment5.aa | classias-tag -m sentiment5_bcde.model -qt
# Accuracy: 0.7533 (1606/2132)
# Micro P, R, F1: 0.7528 (804/1068), 0.7542 (804/1066), 0.7535

# % classias-train -tb -g5 -x sentiment5.txt
