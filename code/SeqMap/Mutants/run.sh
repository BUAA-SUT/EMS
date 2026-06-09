for i in {0..100}
do
    clang++ -O0 -g -o ./seqmap_v$i/seqmap ./seqmap_v$i/seqmap.cpp
done
