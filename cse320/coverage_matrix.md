# CSE 320 Midterm 1 Phase 1 source map and coverage matrix

**Status:** Phases 2–5 are complete in `question_banks/CSE320.py`: 30 Cache, 16 Physical Memory, 25 Basic Code, and 34 General Concepts questions. The latter covers 28 of 29 official definition terms; the user directed us to skip `Assertion` because its definition/example is absent from the supplied course sources. Twenty-one Cache, four Physical Memory, and two General Concepts questions use images; label-reading prompts were replaced with application questions. HW questions have not been written. The official `MT1 Topics/Questions List` in `FULL CSE 320 Notes (1).docx` paragraphs 302–308 controls exam scope; its duplicate in `CSE 320 Notes.docx` paragraphs 26–32 agrees. Professor comments in the full notes guide weighting. Slides and the supplied PNGs guide technical details and visual structure.

## Exact exam structure and proposed bank coverage

| Exam category | Real exam | Proposed bank | Primary source | Emphasis and question approach |
| --- | ---: | ---: | --- | --- |
| Physical Memory: HDD component by description | 2 | 4 | `6. Physical Memory.pptx` slides 10–13, 19; `hdd_multi_platter_cylinder_surfaces.png` | The official list says *by description*. The full notes P286 say apparently no labeling question. Practice component roles and movement without relying on a bare label recall question. |
| Physical Memory: hierarchy ordering | 1 | 4 | Physical Memory slides 2–4, 38–40; labeled and user-provided unlabeled hierarchy images | Practice level order, caching, locality, and persistence. Three questions use different variants: unlabeled tiers for level ordering, unlabeled category names for the secondary-storage boundary plus persistence, and the labeled figure's cycle values for cache-fill arithmetic. |
| Physical Memory: HDD access time | 1 | 3 | Physical Memory slides 17–18; full notes P103, P148–153, P284 | Seek + average half rotation + transfer, including one backsolve. All three qualify for the exact mock-exam access-time slot. |
| Physical Memory: HDD capacity practice | 0 | 2 | Physical Memory slide 14; full notes P103, P143–144, P284 | Supplemental mastery questions on the full capacity formula and the alternate sectors/cylinder form. These do **not** fill the real exam's access-time slot. |
| Physical Memory: SSD versus HDD | 1 | 3 | Physical Memory slides 23–25; full notes P258 | Moving parts, access behavior, erase/write and wear, and defragmentation. Avoid NAND/NOR detail. |
| Cache: address mapping | 5 | 17 | `Cache Diagram.png`; `6.1 Caches.pptx` slides 6–16; `cache_direct_mapped_blank_table.png`; `cache_2way_set_associative_blank_table.png`; `cache_2way_set_associative_structure.png` | Highest practice volume. Include hex decomposition, valid bit, tag and set checks, sequential accesses, fills, and replacement. Full notes P159, P197–204 say lecture-like diagrams with changed numbers are likely. |
| Cache: address-field interpretation | 2 | 6 | Cache slides 7–14; `cache_general_organization_and_address_fields.png`; `Cache read and address breakdown.png`; `General cache organization.png`; `cache_set_line_structure.png` | Derive S, E, B, tag/set/offset widths and explain where an address is checked. |
| Cache: average access time | 1 | 4 | Cache slides 18–20 | Hit time + miss rate × additional miss penalty; at least one conditional multi-level calculation. |
| Cache: design tradeoffs | 1 | 3 | Cache slides 6, 12–17, 19–21 | Associativity, set count, conflict misses, block size, hit time, and replacement complexity. |
| General Concepts: pointers, aliasing, locality, optimization/toolchain | 4 | 6 | `5. Optimizations and Profiling.pptx` slides 20–24 and later optimization examples; Physical Memory slides 5–8; `7. Compiler Toolchains.pptx` slides 2–8 | Reason from short situations and code. Full notes P139 emphasizes actual-code aliasing, optimization terms and benefits, and possible profiling. |
| General Concepts: definitions | 11 | 28 | Official term list, full notes P304; topic-specific slides listed below | One source-grounded, open-response `What is [term]?` entry per supported term. The bank requires definition recall instead of term recognition. `Assertion` is omitted at the user's direction because no defining course source was found. |
| HW1 implementation functions | 6 | 9 reserved | **Awaiting HW1 implementation** | No behavior or purpose questions until code is supplied. |
| HW2 Part B approach | 2 | 4 reserved | **Awaiting HW2 Part B materials** | Do not infer the approach. |
| GREP lab CLI | 1 | 2 reserved | **Awaiting GREP lab materials** | Do not infer which CLI tools were taught. |
| Basic Code: cache hit/miss from a program | 2 | 3 | Cache slides 9–14, 21; Physical Memory slides 5–8 | Short C access traces with explicit alignment, element size, cache state, block size, and capacity where needed. |
| Basic Code: pointers, aliasing, locality, optimization | 7 | 17 | Optimization slides 20–24 and examples; Physical Memory slides 5–8 | Pointer writes and arithmetic; aliasing blockers; local accumulation; row-major traversal; code motion, strength reduction, common subexpressions, unrolling, inlining, and call effects. |
| Basic Code: globals | 1 | 5 | Toolchains slides 11, 13, 15–19; `ELF Diagram.png` | Include at least two multi-file examples, static locals, `extern`, and the lecture's strong/weak rules. Keep these few relative to cache questions, per full notes P300. |

**Revised total:** 120 questions: 16 Physical Memory, 30 Cache, 34 General Concepts, 25 Basic Code, and 15 reserved HW questions. The four authored sections currently contain 105 questions. The 15 HW entries remain empty until source materials arrive. Each mock exam must draw exactly 5/9/15/9/10 in that category order and obey the listed subcategory quotas. A complete 48-question mock cannot be generated before the HW sources arrive.

## Definition pool source map

The official list contains 29 terms. The bank covers 28 with source-backed questions. The user directed us to skip `Assertion` because no definition or example was found in the supplied course files.

| Terms | Course support |
| --- | --- |
| Memory Aliasing; Loop Unrolling; Branch Prediction; Inlining; Code Motion; Reduction in Strength; Super scalar; Latency; Throughput; Profiler | Optimization slides 5–6, 14–15, 20–24, and later processor-performance examples. Branch prediction is also mentioned in `Copy of 320 midterm 1 notes.docx` P82. |
| Spatial Locality; Temporal Locality; Volatile Memory | Physical Memory slides 5–8, 27, 36–37. The official list misspells Spatial as “Spacial”; use the standard spelling in questions. |
| Interrupt; DMA; IO Bus; Memory Bus | Physical Memory slides 20–22 and associated figures. Confirm the two bus distinctions against the actual diagram before an identification question. |
| Eviction; Write-Back; Write-Through | Cache slides 15–17. |
| Symbol Resolution; Relocation; Position Independent Code; Compiler; Linker; Assembler | Toolchains slides 2–8, 16–20, and later PIC slides. Stage tool names explicitly given in slide 2: `cpp`, `cc`, `as`, `ld`. |
| Read Only Memory; Debugger | ROM appears among the nonvolatile memory categories in `Copy of CSE 320 Notes.docx` P113. The full notes name GDB as a debugger (P2, P46). Questions stay within those supported descriptions. |
| Assertion | Official pool, full notes P304; no definition or example located. Omitted by user direction. |

## Formulas and course conventions to verify while writing

- Disk capacity, Physical Memory slide 14: `(bytes/sector) × (sectors/track) × (tracks/surface) × (surfaces/platter) × (platters/disk)`. If given sectors per cylinder, do not multiply surfaces a second time. Full notes P143–144 specifically mention unit cancellation and that alternate form.
- Average HDD access, Physical Memory slides 17–18: `seek + half-rotation + sector transfer`. Half-rotation is `(60/RPM)/2` seconds; one-sector transfer is `(60/RPM)/(sectors/track)` seconds. Full notes P148–152 stress the component times.
- Cache, Cache slides 7–14: `C = S × E × B` data bytes; `b = log2(B)`, `s = log2(S)`, `t = address width − s − b`. A hit needs a selected set, a valid line, and matching tag. State-transition questions must state the replacement rule if multiple occupied ways qualify.
- Average memory access, Cache slides 19–20: `hit time + miss rate × additional miss penalty`. Multi-level examples must say whether each hit time is additional and whether the lower-level miss rate is conditional.
- Linker, Toolchains slides 16–18: initialized globals and procedures are strong; uninitialized globals are weak; two strong definitions conflict; strong wins over weak. Questions should explicitly invoke this lecture model because modern compiler/linker defaults may differ.

**Source conflict:** Physical Memory slide 18 rounds the average half rotation at 7,200 RPM to **4 ms**, whereas slide 17's formula yields approximately **4.17 ms**. Future numerical items should use exact, manageable values or state the rounding convention. The official exam breakdown reserves one HDD access-time question even though full notes P103 suggests one of each calculation type may appear; the exact list takes precedence for mock composition.

## Visual inventory and intended use

| Image | Planned role |
| --- | --- |
| `Cache Diagram.png` | Supplied exam-style valid/tag tables, direct mapped and two-way set associative. Mapping, hit/miss, and replacement questions. |
| `cache_direct_mapped_blank_table.png` | Lecture-style empty state for traces; numerical states must be supplied in question data or an adapted image. |
| `cache_2way_set_associative_blank_table.png` | Two-way traces and replacement. Numerical states must be supplied. |
| `cache_2way_set_associative_structure.png` | Interpret sets, lines, and ways. |
| `General cache organization.png`; `cache_set_line_structure.png`; `cache_general_organization_and_address_fields.png`; `Cache read and address breakdown.png` | Derive and interpret S/E/B, valid/tag/data layout, and address fields. Two address diagrams appear visually identical; reuse only where the figure contributes to the reasoning. |
| `hdd_single_platter_tracks_sectors_geometry.png`; `hdd_multi_platter_cylinder_surfaces.png` | The single-platter figure remains a source reference but has no current question. The multi-platter figure supports an applied component question. |
| `Physical Memory Hierachy.png`; `Physical Memory Hierachy_NO_LABELS.png`; `Physical Memory Hierachy_NO_CPU_AND_STORAGE_CATEGORIES.png` | The labeled source supplies cycle costs for a cache-fill scenario. The unlabeled tiers test level ordering; the hidden category labels support boundary identification plus persistence. |
| `ELF Diagram.png` | Interpret `.text`, `.data`, `.bss`, symbol table, and relocation sections within official linker/global scope. |
| `io_memory_bus_diagram.png`; `io_memory_bus_diagram_UNLABELED.png` | The first is the labeled slide-20 source. The second is the user-provided unlabeled variant used by the I/O and memory bus questions; students trace the DMA path and identify each bus by its role. |

The target is **at least 20 questions whose answer truly depends on reading a figure**. Proposed allocation: 10 cache mapping tables, 3 address/organization figures, 2 HDD figures, 2 hierarchy figures, 2 toolchain/ELF figures, and 1 additional cache structure figure. An attached decorative figure does not count. Some supplied figures are labeled or blank, so numerical exercises will need a carefully adapted figure or an adjacent structured state table. Do not alter the original PNGs.

## Existing website format and proposed image contract

`question_banks/*.py` exports `questions = {topic: {question_text: answer_record}}`. `server.py` converts each record for the UI, serves supported CSE 320 images, and `build_static.py` copies those images into the static build. The UI reveals the answer and asks the student to self-grade.

**Agreed question record:** Keep the outer `questions` dictionary. The five headings in `question_banks/CSE320.py` are **Physical Memory**, **Cache**, **General Concepts**, **HW Questions**, and **Basic Code**. Multiple-choice records contain `subcategory`, `choices` (`A`–`D`), `correct_answer`, `explanation`, and one compact `source` reference. Definition-recall records contain `subcategory`, `answer`, and `source`, with no choices. Add `image` only when the question uses a figure. The question text remains the dictionary key. The loader accepts legacy answer strings and both structured record types. The UI hides choices for open-response definitions and reveals the supplied definition during self-grading.

No website changes or CSE 320 question entries are part of Phase 1.

## Phase gates

1. **This file:** review source map, images, quotas, and format proposal. Stop before question authoring.
2. Cache batches of about 10–15, then numerical, state-trace, visual, distractor, and duplicate audits.
3. Physical Memory batches, then independent disk arithmetic and source checks.
4. Basic Code batches, then C behavior, aliasing, and linker-model checks.
5. General Concepts batches, with every definition-pool term audited against source support.
6. HW batches only after the implementation and lab materials arrive.
7. Integrate the approved question record and images into the website, then sample and verify full mock exams when HW is complete.
