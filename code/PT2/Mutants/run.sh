for i in $(seq 0 49)
do
    gcc ./printtokens2_v$i/print_tokens2.c -o ./printtokens2_v$i/print_tokens2
done
