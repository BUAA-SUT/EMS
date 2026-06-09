for i in $(seq 0 16)
do
    gcc ./grep_v$i/grep.c -o ./grep_v$i/grep
done
