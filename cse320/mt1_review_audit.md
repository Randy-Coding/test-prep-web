# CSE320 MT1 review audit — corrected source inventory

The earlier 108-question inventory incorrectly treated explanatory tables, demonstrations, and intermediate solution steps as separate review questions. This inventory counts explicit prompts and concrete worked exercises. It groups subparts of one exercise together and does not count its solution page again.

**Review Audit: 41 questions** — 13 grouped worked exercises, 16 explicit concept prompts, the Assertion definition, and six questions covering exam topics without a close or exact match in the committed bank. Five further questions were retained after individually auditing supplemental practice: independent accumulators, compulsory misses, capacity misses, floating-point rounding, and dead-store elimination. The other 18 definition warm-ups reuse existing questions for the same word. Close matches do not replace the 29 substantive review exercises/prompts.

**Supplemental Practice: 0 questions** — all 72 former items received an individual decision: five retained in Review Audit and 67 removed. See the [72-item decision ledger](supplemental_question_audit.md) for specific matches, subparts, and extra-practice reasons. The original four committed sections retain all 104 questions unchanged. Total bank is 145. HW1, HW2, and GREP lab are deferred.

## Exam-topic coverage missing from the committed bank (6 additional questions)

These are included because the transcript or official topic breakdown identifies the subject as exam material, even though the review does not pose a direct exercise. Matching uses the original 104 committed questions as the baseline.

| Exam topic | Source | Why an additional question is needed | Bank entry |
| --- | --- | --- | --- |
| Increasing set count | Transcript cache-design discussion; official cache tradeoffs topic | Existing questions change associativity or block size; none increases sets with both fixed. | [Question](../question_banks/CSE320.py#L845) |
| Platter by description | Transcript lines 821–827; official HDD component-by-description topic | No committed platter-identification question. | [Question](../question_banks/CSE320.py#L852) |
| Sector by description | Transcript lines 821–827; official HDD component-by-description topic | Committed sector calculations do not ask for the component name. | [Question](../question_banks/CSE320.py#L859) |
| Cylinder by description | Transcript lines 821–827; official HDD component-by-description topic | The committed cylinder application does not ask for the name from its description. | [Question](../question_banks/CSE320.py#L866) |
| Full hierarchy ordering | Transcript lines 830–834; official memory-hierarchy ordering topic | The committed four-tier ordering omits L1/L2/L3 and SSD. | [Question](../question_banks/CSE320.py#L873) |
| SRAM versus DRAM | Transcript lines 825–840 (tentative exam mention) | The volatile-memory definition names both but does not distinguish their roles and refresh requirements. | [Question](../question_banks/CSE320.py#L880) |

The initial broad topic check identified existing coverage of cache lookup/address bits, hit/miss rates, AMAT, HDD access time, SSD/HDD, pointer tracing and aliasing, local accumulation, blocking, optimization safety and loop dependencies, toolchain/tool names, linker behavior, global variables, and the remaining definition terms. That broad check did not establish an individual match for every supplemental question; the subsequent [72-item decision ledger](supplemental_question_audit.md) documents the stricter review and five further additions. HW and lab topics remain deferred.

## Worked exercises (13)

| PDF page | Exercise | Bank entry |
| --- | --- | --- |
| 24 | a[0], a[8], a[16]: hit/miss sequence and loaded block | [Question](../question_banks/CSE320.py#L632) |
| 25 | Cache capacity: 4 sets, 2 lines/set, 8-byte blocks | [Question](../question_banks/CSE320.py#L640) |
| 26 | Cache capacity: 8 sets, 4 lines/set, 32-byte blocks | [Question](../question_banks/CSE320.py#L647) |
| 32 | Cache #1 lookup of 0x1D | [Question](../question_banks/CSE320.py#L654) |
| 33 | Cache #2 lookup of 0x69 | [Question](../question_banks/CSE320.py#L662) |
| 37 | Matrix multiplication: misses per inner iteration and miss rate | [Question](../question_banks/CSE320.py#L670) |
| 42–43 | Three-level average memory access time | [Question](../question_banks/CSE320.py#L677) |
| 48 | Track the {3,5,7} pointer program | [Question](../question_banks/CSE320.py#L684) |
| 49 | Aliased pointers: write 25 through q, read through p | [Question](../question_banks/CSE320.py#L691) |
| 53 | Is replacing y*3 with y<<3 correct? | [Question](../question_banks/CSE320.py#L698) |
| 57–58 | Replace output-pointer accumulation with a local accumulator | [Question](../question_banks/CSE320.py#L705) |
| 57, 59 | Move next_value() outside the loop | [Question](../question_banks/CSE320.py#L712) |
| 81 | HDD access time: 6,000 RPM, 6 ms seek, 500 sectors/track | [Question](../question_banks/CSE320.py#L719) |

## Explicit concept prompts (16)

| PDF page | Source prompt | Bank entry |
| --- | --- | --- |
| 61 | What is the difference between p, *p, and &p when p is a pointer? | [Question](../question_banks/CSE320.py#L726) |
| 62 | How does p++ differ from (*p)++? Does incrementing a pointer always move it forward by one byte? | [Question](../question_banks/CSE320.py#L733) |
| 63 | When a function receives a pointer argument, can it modify the caller data? Can assigning a new address to that parameter change the caller pointer? | [Question](../question_banks/CSE320.py#L740) |
| 64 | Does a pointer being non-NULL guarantee that it is safe to dereference? | [Question](../question_banks/CSE320.py#L747) |
| 65 | What is memory aliasing? Does copying one pointer into another create a separate copy of the pointed-to data? | [Question](../question_banks/CSE320.py#L754) |
| 66 | A program reads through p, writes through q, and then reads through p again. Why might the compiler need to repeat the read? | [Question](../question_banks/CSE320.py#L761) |
| 67 | Why can replacing repeated writes through an output pointer with a local accumulator change a program result? | [Question](../question_banks/CSE320.py#L768) |
| 68 | If an input pointer is declared const int *a, can the compiler assume that the values in the array never change? | [Question](../question_banks/CSE320.py#L775) |
| 69 | What is the difference between spatial locality and temporal locality? | [Question](../question_banks/CSE320.py#L782) |
| 70 | Why does sequential array traversal usually have better spatial locality than linked-list traversal? Does using an array automatically guarantee good locality? | [Question](../question_banks/CSE320.py#L789) |
| 71 | For a C two-dimensional array, why is it usually better for the innermost loop to change the second index? Does the loop variable name matter? | [Question](../question_banks/CSE320.py#L796) |
| 72 | What is cache blocking, and why can it improve performance even when a program performs the same calculations? | [Question](../question_banks/CSE320.py#L803) |
| 73 | Is an unchanged result enough to make moving a calculation outside a loop safe? | [Question](../question_banks/CSE320.py#L810) |
| 74 | Function A performs one addition and is called millions of times inside a loop. Function B performs a lengthy calculation and is called once. Which is generally the stronger candidate for inlining and why? | [Question](../question_banks/CSE320.py#L817) |
| 75 | If a function return value is unused, can the compiler automatically remove the function call? | [Question](../question_banks/CSE320.py#L824) |
| 76 | Does loop unrolling always make a program faster? What limitations can remain after a loop is unrolled? | [Question](../question_banks/CSE320.py#L831) |

## Definition warm-ups (19)

Existing identification questions are reused by answer word; no duplicate definitions were added.

| PDF page | Word | Bank entry |
| --- | --- | --- |
| 3 | Memory Aliasing | [Question](../question_banks/CSE320.py#L452) |
| 4 | Read Only Memory | [Question](../question_banks/CSE320.py#L457) |
| 5 | Interrupt | [Question](../question_banks/CSE320.py#L462) |
| 6 | Eviction | [Question](../question_banks/CSE320.py#L467) |
| 7 | Volatile Memory | [Question](../question_banks/CSE320.py#L472) |
| 8 | IO Bus | [Question](../question_banks/CSE320.py#L477) |
| 9 | Memory Bus | [Question](../question_banks/CSE320.py#L482) |
| 10 | DMA | [Question](../question_banks/CSE320.py#L487) |
| 11 | Assertion | [Question](../question_banks/CSE320.py#L838) |
| 12 | Branch Prediction | [Question](../question_banks/CSE320.py#L497) |
| 13 | Code Motion | [Question](../question_banks/CSE320.py#L394) |
| 14 | Super scalar | [Question](../question_banks/CSE320.py#L520) |
| 15 | Latency | [Question](../question_banks/CSE320.py#L525) |
| 16 | Throughput | [Question](../question_banks/CSE320.py#L530) |
| 17 | Write-Back | [Question](../question_banks/CSE320.py#L545) |
| 18 | Write-Through | [Question](../question_banks/CSE320.py#L550) |
| 19 | Position Independent Code | [Question](../question_banks/CSE320.py#L568) |
| 20 | Symbol Resolution | [Question](../question_banks/CSE320.py#L558) |
| 21 | Relocation | [Question](../question_banks/CSE320.py#L563) |

## Supporting material, not additional review questions

The locality explanations, cache architecture/miss-type/tradeoff tables, address-bit procedure, elements-per-block illustrations, miss-rate table, row/column illustration, blocking explanation, AMAT formulas, pointer table, optimization demonstrations, memory hierarchy, and SSD/HDD comparison support the exercises. Questions previously generated from these were individually reviewed; only the five identified in the [decision ledger](supplemental_question_audit.md) were retained.

In particular, pages 50–51 and 54–56 demonstrate transformations without asking separate exercises; page 57 asks two specific replacement questions. The original program trace and intermediate HDD/AMAT calculations are reasoning within their corresponding exercises, not extra source questions. Page 24's accesses and loaded-block subpart are one grouped exercise. This is a source inventory, not the official exam question-count breakdown.

The inventory was checked against the 82-page review PDF and associated transcript. The cache and program questions retain the source numbers and code, with explicit assumptions where needed for an unambiguous answer.
