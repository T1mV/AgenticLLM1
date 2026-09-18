

# first, training the tokenizer on a vocab-size of 8192
python -m scripts.tok_train --max-chars 500000000 --vocab-size 8192                      

# then we evaluate the tokenizer
python -m scripts.token_eval

# train a new tokenizer on the vocab-size 32768
python -m scripts.tok_train --max-chars 500000000 --vocab-size 32768

# evaluate the tokenizer again
python -m scripts.token_eval

# the script used to answer part ofthe text
python -m scripts.tok_experiment                                                                                                                                  