# Individual supplemental question audit

Completed October 3, 2026. All 72 original Supplemental Practice questions were reviewed individually against the existing bank and the review transcript. Five were retained in Review Audit; 67 were removed from the active bank. Supplemental Practice is empty. Review Audit now contains 41 questions; the bank contains 145 total.

Entry standard: retain a source-supported question when it tests a meaningful missing distinction or a substantially different code-analysis skill. Remove close variants, solution subparts, inverses of existing tradeoffs, and elementary questions generated from explanatory tables. Broad topic overlap alone is not a match: the decisions below identify the corresponding skill, prompt or subpart, or explain why the item is only extra practice. This audit is confined to the 72 supplemental items; it does not reclassify the original sections or the 36 earlier Review Audit questions. HW1, HW2 and GREP remain deferred.

Numbers refer to dictionary insertion order within each named section. Original supplemental numbers below are frozen before removal; retained Review Audit questions are appended as #37–41. Existing source-inventory links remain valid.

| Original supplemental # | Question / skill | Decision and evidence |
| --- | --- | --- |
| 1 | Matrix hit-rate variant (32-byte blocks) | Remove: numerical/block-size variant of Review Audit #6; same method and denominator distinction. |
| 2 | Original analyze program output | Remove: baseline trace is a subpart of Review Audit #11–12; #12 explanation explicitly derives the original output. |
| 3 | Independent versus single accumulators | Keep as Review Audit #37: concrete comparison tests how independent accumulators break a dependency chain. #29 mentions the limitation but does not require identifying the two chains in code; transcript lines 582–598 emphasizes this application. |
| 4 | Unsigned multiply/shift variant | Remove: same arithmetic and failed transformation as Review Audit #10; unsigned type adds no useful distinction for y=10. |
| 5 | Remove overwritten local initialization | Remove: Review Audit #41 (retained item 55) includes this overwritten initialization and its justification. |
| 6 | p, *p, and &p | Remove: close match to Review Audit #14. |
| 7 | Pointer parameter passed by value | Remove: close match to Review Audit #16. |
| 8 | Non-NULL pointer validity | Remove: close match to Review Audit #17. |
| 9 | const input and output aliasing | Remove: close match to Review Audit #21. |
| 10 | Array versus linked-list locality | Remove: close match to Review Audit #23. |
| 11 | Blocking and tile reuse | Remove: close match to Review Audit #25. |
| 12 | Hoisting a printing call | Remove: Review Audit #26 explicitly tests effects and zero-iteration loops. |
| 13 | Inlining candidate comparison | Remove: close match to Review Audit #27. |
| 14 | Unused return with side effects | Remove: close match to Review Audit #28. |
| 15 | Unrolling limitations | Remove: close match to Review Audit #29. |
| 16 | Repeated-address locality | Remove: General Concepts #18 and Review Audit #22 identify temporal locality. |
| 17 | Neighboring-element locality | Remove: General Concepts #17 and Review Audit #22 identify spatial locality. |
| 18 | Elements loaded by a[0] | Remove: explicit loaded-block subpart of Review Audit #1. |
| 19 | Compulsory miss identification | Keep as Review Audit #38: no existing prompt asks students to distinguish first-access compulsory misses from other miss classes. Supported by review p27 and transcript lines 115–117. |
| 20 | Conflict miss identification | Remove: Cache #30 directly tests same-set competition and conflict reduction; its explanation names the conflict. |
| 21 | Capacity miss identification | Keep as Review Audit #39: total working-set overflow is a different cause from Cache #30 placement conflicts; no existing question directly tests that distinction. Supported by review p27 and transcript lines 120 onward. |
| 22 | Direct-mapped architecture | Remove: Cache #12 explicitly identifies direct mapping and one line per set; several existing direct-mapped exercises apply it. |
| 23 | Set-associative architecture | Remove: Cache #12 and #30 apply two-way placement within the selected set; a separate table-label recall adds little. |
| 24 | Fully associative architecture | Remove: Cache #28 explicitly applies fully associative S=1 and zero set-index bits. |
| 25 | Increase associativity | Remove: close match to Cache #12 and #30. |
| 26 | Decrease associativity | Remove: inverse of the associativity change already tested by Cache #12 and #30; no new reasoning. |
| 27 | Increase block size | Remove: close match to Cache #22. |
| 28 | Decrease block size | Remove: inverse of Cache #22; no new reasoning. |
| 29 | Increase set count | Remove: close match to Review Audit #31. |
| 30 | Decrease set count | Remove: inverse of Review Audit #31; no new reasoning. |
| 31 | Tag/index/offset roles | Remove: Cache #10 and #18 require interpreting all three fields. |
| 32 | Cache lookup procedure | Remove: Cache #1–2 and Review Audit #4–5 require selected-set, valid-bit and tag checks. |
| 33 | Doubles per 16-byte block | Remove: elementary block-size division already used in Basic Code #2 and Review Audit #6; parameter variant. |
| 34 | Ints per 64-byte block | Remove: explicit block-size calculation in Review Audit #1. |
| 35 | Sequential rate: 2 elements/block | Remove: Basic Code #2 applies this two-elements-per-block access pattern (with a stride); Basic Code #1 and Review Audit #1 already assess sequential block reuse. Table-row repetition. |
| 36 | Sequential rate: 4 elements/block | Remove: Basic Code #1 directly assesses sequential four-elements-per-block misses/hits. |
| 37 | Sequential rate: 8 elements/block | Remove: per-array sequential rate is a subpart of Review Audit #6. |
| 38 | Sequential rate: 16 elements/block | Remove: same block size and element count as Review Audit #1; extending the sequential pattern adds no skill. |
| 39 | Row versus column traversal | Remove: Basic Code #10–11 and Review Audit #24 already assess changing subscripts and row-major traversal. |
| 40 | Matrix per-array access breakdown | Remove: per-array breakdown is explicitly derived in Review Audit #6 explanation. |
| 41 | Sequential traversal does not guarantee retention | Remove: Review Audit #6 states retention/no-interference assumptions and #25 explains fit-dependent blocking. This caution is supporting explanation rather than another high-value exercise. |
| 42 | Convert hit rate to miss rate | Remove: hit-to-miss conversion is explicit in Review Audit #7 and Cache #20. |
| 43 | Lookup time paid on misses | Remove: Review Audit #7 explicitly states that each reached lookup time is paid, including on misses. |
| 44 | One-level AMAT formula | Remove: Cache #20 applies this formula numerically; formula-only recall adds little. |
| 45 | Two-level AMAT formula | Remove: Cache #11 and #21 apply this conditional two-level formula numerically. |
| 46 | Three-level AMAT formula | Remove: Review Audit #7 applies and displays this nested three-level formula. |
| 47 | Intermediate L3 and L2 AMAT | Remove: the exact L3=70 ns and L2=19 ns intermediate calculations are in Review Audit #7 explanation. |
| 48 | Compiler versus programmer algorithm choice | Remove: review p45 overview of programmer responsibility, with no concrete new code-analysis skill. Existing Review Audit #26 and #28 test behavior preservation. Extra explanatory practice under the strict entry standard. |
| 49 | Four optimization obstacles | Keep, revised as Review Audit #40: replace list memorization with a question about floating-point regrouping and intermediate rounding. Existing aliasing/side-effect questions do not cover this obstacle; transcript lines 462–466 explicitly explains it. |
| 50 | Pointer expression table and write | Remove: Review Audit #14 covers the expressions and #9 tests observing a write through an alias. |
| 51 | Initial p and q targets | Remove: initial-state subpart of Review Audit #8 pointer trace. |
| 52 | Nonaliasing local accumulation | Remove: Basic Code #14 tests the local-accumulator opportunity; Review Audit #11 and #20 cover the aliasing boundary. |
| 53 | Loop-invariant index multiplication | Remove: close match to Basic Code #15. |
| 54 | Multiplication versus equivalent additions | Remove: General Concepts #13 and Basic Code #16 identify strength reduction; Review Audit #10 checks equivalence. Tiny arithmetic example adds little. |
| 55 | Dead-store function simplification | Keep as Review Audit #41: concrete elimination of an overwritten, unobserved local store fills a gap. Removing an effectful call (#28) is a different test. Supported by review p54 and transcript lines 562–573. |
| 56 | Unrolled-loop cleanup | Remove: cleanup requirement is already an explicit correct-choice subpart of Review Audit #29. This illustration does not warrant another item under the strict standard. |
| 57 | Unrolling iteration count | Remove: Basic Code #18 already tests reduced loop-control work per element; counting five iterations adds little. |
| 58 | Single-accumulator dependency | Remove: dependency limitation is in Review Audit #29; retained #37 gives the stronger concrete code comparison. |
| 59 | Persistence across power loss | Remove: Physical Memory #10 and General Concepts #5 already assess nonvolatile storage versus volatile main memory/cache. |
| 60 | Memory hierarchy trends | Remove: hierarchy trends are stated in Review Audit #35 and applied in Physical Memory #10. |
| 61 | HDD access-time components | Remove: component sequence is explicit in Review Audit #13 and Physical Memory #8, #11–12. |
| 62 | Full HDD rotation time | Remove: intermediate rotation calculation within Review Audit #13; also required by Physical Memory #8 and #11. |
| 63 | Average rotational latency | Remove: exact 5 ms rotational-latency subpart of Review Audit #13. |
| 64 | One-sector transfer time | Remove: exact 0.02 ms transfer-time subpart of Review Audit #13. |
| 65 | Seek cannot be inferred from RPM | Remove: Review Audit #13 separately supplies seek; Physical Memory #12 backsolves it. Extra clarification of the same access-time model. |
| 66 | SSD/HDD storage technologies | Remove: Physical Memory #10 explanation distinguishes flash and magnetic disks; #14 applies the physical difference. |
| 67 | SSD/HDD mechanical delays | Remove: close match to Physical Memory #14. |
| 68 | SSD/HDD random-read speed | Remove: same no-moving-parts reasoning as Physical Memory #14. |
| 69 | SSD/HDD cost per byte | Remove: Review Audit #35 explanation already covers the cost-per-byte hierarchy trend. Another SSD/HDD table row has low marginal value. |
| 70 | SSD/HDD shock resistance | Remove: downstream consequence of the no-moving-parts distinction in Physical Memory #14; table-row recall adds no separate mechanism. |
| 71 | SSD/HDD wear concerns | Remove: Physical Memory #15 explicitly tests finite flash endurance. HDD mechanical wear is supporting comparison, not another needed exercise. |
| 72 | SSD/HDD persistence | Remove: close match to Physical Memory #10 and supplemental item 59. |

The removed questions are no longer loaded by the app. This ledger records their subjects and decisions without creating another selectable practice pool. The supplied course files remain available. The five retained records keep their source references; item 49 was rewritten to test understanding rather than memorization of an obstacle list.
