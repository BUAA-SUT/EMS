# Supplementary EXAM Results

To complement the TOP-N analysis reported in the paper, we additionally evaluated the
three metamorphic slicing strategies using the EXAM metric. EXAM measures the percentage
of executable statements that must be inspected before the faulty statement is reached;
therefore, a lower EXAM value indicates better fault-localization effectiveness.

## Results under different weighting strategies

![EXAM results under different weighting strategies](EXAM_results_under_different_weighting_strategies.emf)

**Figure 1. EXAM results under different weighting strategies and weight values.**

The EXAM results are consistent with the TOP-N findings reported in the paper. Across
the investigated weight range, `dms` generally achieves lower EXAM values than both
`ims` and `oms`. This provides additional evidence that emphasizing the symmetric
difference coverage set is more effective than emphasizing the intersection coverage
set for fault localization.

## Results over the expanded weight range

![EXAM results over the expanded weight range](EXAM_results_over_expanded_weight_range.emf)

**Figure 2. EXAM results under `ims` and `dms` over the expanded weight range.**

To examine whether values below the lower bound used in the main experiments reveal
additional behavior, we extended the evaluated weights to include values from 0.02 to
0.48 at intervals of 0.02. These results follow the same overall trend as those obtained
over the original range: no reversal between `ims` and `dms`, new optimum, or
qualitatively different behavior is observed. The expanded analysis therefore supports
the use of 0.50 as the lower bound in the main experiments.
