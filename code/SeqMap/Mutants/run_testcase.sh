for i in {0..100}
do
    ./seqmap_v$i/seqmap 2 ./seqmap_v$i/probes.fa ./seqmap_v$i/trans.fa ./seqmap_v$i/output.txt
done
