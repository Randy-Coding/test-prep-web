"""CSE 320 Midterm 1 questions. Add audited sections to this topic dictionary."""

questions = {
    "Cache": {
        'Use Cache #1 in the image. For the 6-bit byte address 0x14, which result follows?': {
            'subcategory': 'Address mapping',
            'choices': {'A': 'Miss; set 1 has tag 1 but the requested tag is 2', 'B': 'Hit in set 1, block number 1', 'C': 'Hit in set 0, block number 0', 'D': "Miss; set 1's valid bit is 0"},
            'correct_answer': 'B',
            'explanation': '0x14 = 01 01 00₂: tag 1, set 1, offset 0. Cache #1 has valid=1 and tag=1 in set 1, so the access hits.',
            'source': 'Cache Diagram.png; Cache #1; Caches slides 9–11',
            'image': 'cse320/Cache Diagram.png',
        },
        'Use Cache #1 in the image. A read of 6-bit byte address 0x20 checks a line whose stored tag matches the address tag. What happens?': {
            'subcategory': 'Address mapping',
            'choices': {'A': 'It hits because matching tags are sufficient', 'B': 'It misses in set 2 because 0x20 has set bits 10', 'C': 'It misses in set 0 because that line is invalid', 'D': 'It hits in set 0 and returns byte offset 2'},
            'correct_answer': 'C',
            'explanation': '0x20 = 10 00 00₂: tag 2, set 0, offset 0. The stored tag is 2, but valid=0. A tag match on an invalid line is a miss.',
            'source': 'Cache Diagram.png; Cache #1; Caches slides 9–10',
            'image': 'cse320/Cache Diagram.png',
        },
        'Start with Cache #1 exactly as shown. Read 0x14, then 0x34, then 0x14. Each miss loads its block. What is the hit/miss sequence?': {
            'subcategory': 'Address mapping',
            'choices': {'A': 'Hit, miss, miss', 'B': 'Hit, miss, hit', 'C': 'Miss, miss, miss', 'D': 'Hit, hit, hit'},
            'correct_answer': 'A',
            'explanation': 'All three addresses select set 1. Initially it holds valid tag 1, so 0x14 hits. Address 0x34 has tag 3 and replaces it on a miss. The final 0x14 has tag 1 again and misses.',
            'source': 'Cache Diagram.png; Cache #1; Caches slides 9–11',
            'image': 'cse320/Cache Diagram.png',
        },
        'Use Cache #2 in the image. A read of 7-bit byte address 0x5C misses. Which block number can receive it without evicting a valid block?': {
            'subcategory': 'Address mapping',
            'choices': {'A': 'Block number 7 in set 3', 'B': 'Block number 5 in set 2', 'C': 'Block number 0 in set 0', 'D': 'Block number 6 in set 3'},
            'correct_answer': 'D',
            'explanation': '0x5C = 101 11 00₂: tag 5, set 3. In set 3, block number 6 has tag 5 but is invalid, while block number 7 is valid. Fill block number 6; no valid block needs eviction.',
            'source': 'Cache Diagram.png; Cache #2; Caches slides 12–14',
            'image': 'cse320/Cache Diagram.png',
        },
        'Use Cache #2 in the image. For 7-bit byte address 0x6A, which set, block number, and byte offset are selected on a hit?': {
            'subcategory': 'Address mapping',
            'choices': {'A': 'Set 2, block number 4, offset 2', 'B': 'Set 2, block number 5, offset 2', 'C': 'Set 1, block number 2, offset 2', 'D': 'Set 2, block number 5, offset 0'},
            'correct_answer': 'B',
            'explanation': '0x6A = 110 10 10₂: tag 6, set 2, offset 2. Block number 5 in set 2 is valid and has tag 6.',
            'source': 'Cache Diagram.png; Cache #2; Caches slides 12–14',
            'image': 'cse320/Cache Diagram.png',
        },
        'Start with Cache #2 exactly as shown. Read 0x30, then 0x70, then 0x30, loading blocks on misses. Which sequence occurs?': {
            'subcategory': 'Address mapping',
            'choices': {'A': 'Hit, miss, miss', 'B': 'Miss, miss, hit', 'C': 'Hit, miss, hit', 'D': 'Hit, hit, hit'},
            'correct_answer': 'C',
            'explanation': '0x30 is tag 3/set 0 and hits valid block number 1. 0x70 is tag 7/set 0; block number 0 stores tag 7 but is invalid, so it misses and fills there. Block number 1 still holds tag 3, so 0x30 hits again.',
            'source': 'Cache Diagram.png; Cache #2; Caches slides 12–14',
            'image': 'cse320/Cache Diagram.png',
        },
        'Use the address-field widths and the four empty sets in the image. Start with every valid bit 0. Read byte addresses 0, 1, 8, 0 in that order; each miss fills its selected line. Which hit/miss sequence results?': {
            'subcategory': 'Address mapping',
            'choices': {'A': 'Miss, hit, hit, hit', 'B': 'Miss, miss, miss, hit', 'C': 'Miss, hit, miss, hit', 'D': 'Miss, hit, miss, miss'},
            'correct_answer': 'D',
            'explanation': 'The diagram has b=1 and s=2. Addresses 0 and 1 share tag 0/set 0: miss then hit. Address 8 has tag 1/set 0 and replaces that line. The last 0 has tag 0/set 0 and misses.',
            'source': '6.1 Caches.pptx; slide 11; cache_direct_mapped_blank_table.png',
            'image': 'cse320/cache_direct_mapped_blank_table.png',
        },
        'Use the address fields and empty two-way sets shown in the image. Start cold, use LRU when a full set needs replacement, and read byte addresses 0, 4, 8, 0. Which tags occupy set 0 at the end?': {
            'subcategory': 'Address mapping',
            'choices': {'A': 'Tags 0 and 2', 'B': 'Tags 0 and 1', 'C': 'Tags 1 and 2', 'D': 'Only tag 0'},
            'correct_answer': 'A',
            'explanation': 'The diagram has t=2, s=1, b=1. Each address maps to set 0 with tags 0, 1, 2, 0. The first two fill both ways; tag 2 evicts LRU tag 0; final tag 0 evicts LRU tag 1. Tags 0 and 2 remain.',
            'source': '6.1 Caches.pptx; slide 14; cache_2way_set_associative_blank_table.png',
            'image': 'cse320/cache_2way_set_associative_blank_table.png',
        },
        'Use the pictured S/E/B organization and tag–set–offset field order. A 16-bit byte-addressed cache has 512 data bytes, 4 lines per set, and 32 data bytes per line. Which field widths fit the diagram?': {
            'subcategory': 'Address-field interpretation',
            'choices': {'A': 'Tag 9, set 2, offset 5', 'B': 'Tag 8, set 3, offset 5', 'C': 'Tag 10, set 1, offset 5', 'D': 'Tag 9, set 5, offset 2'},
            'correct_answer': 'A',
            'explanation': 'The diagram gives C=S×E×B: S=512/(4×32)=4 sets. Thus s=2, b=5, and t=16−2−5=9.',
            'source': '6.1 Caches.pptx; slide 7; cache_general_organization_and_address_fields.png',
            'image': 'cse320/cache_general_organization_and_address_fields.png',
        },
        'An address has tag bits 1011, set bits 010, and offset bits 110. Which set and tag does the cache check, and which byte offset applies on a hit?': {
            'subcategory': 'Address-field interpretation',
            'choices': {'A': 'Set 6, tag 3, byte offset 11', 'B': 'Set 2, tag 11, byte offset 6', 'C': 'Set 3, tag 2, byte offset 6', 'D': 'Set 2, tag 6, byte offset 11'},
            'correct_answer': 'B',
            'explanation': 'Binary 010 selects set 2, binary 1011 is tag 11, and binary 110 selects byte offset 6. The access hits only if set 2 contains a valid matching tag; cache contents are not given.',
            'source': '6.1 Caches.pptx; slide 8; Cache read and address breakdown.png',
        },
        'L1 hit time is 2 cycles and its miss rate is 10%. On an L1 miss, L2 adds 8 cycles. L2 misses 25% of those L1 misses, and main memory then adds 80 cycles. What is average access time?': {
            'subcategory': 'Average access time',
            'choices': {'A': '2.8 cycles', 'B': '10.8 cycles', 'C': '4.8 cycles', 'D': '22.8 cycles'},
            'correct_answer': 'C',
            'explanation': '2 + 0.10×(8 + 0.25×80) = 2 + 2.8 = 4.8 cycles. The 25% L2 miss rate is conditional on an L1 miss.',
            'source': '6.1 Caches.pptx; slides 18–20',
        },
        'A direct-mapped cache has 128 data bytes and 8-byte blocks. It is redesigned as two-way set associative with the same data capacity and block size. Which change and tradeoff follow?': {
            'subcategory': 'Design tradeoff',
            'choices': {'A': 'Sets rise to 32; conflicts increase as each set holds one block', 'B': 'Offset falls to 2 bits; each block holds fewer bytes', 'C': 'Tag bits disappear; either way can hold any memory block', 'D': 'Sets fall to 8; conflicts may drop, but replacement is needed'},
            'correct_answer': 'D',
            'explanation': 'S=C/(E×B). Direct-mapped S=128/(1×8)=16; two-way S=128/(2×8)=8. Each selected set now has two candidates, which can reduce conflicts but adds way comparison and replacement decisions.',
            'source': '6.1 Caches.pptx; slides 6, 12–17',
        },
        'Use the pictured 8-bit cache diagram. A byte read uses address 0xAC. Which outcome follows?': {
            'subcategory': 'Address mapping',
            'choices': {'A': 'Hit in set 3 because tag A appears somewhere in the cache', 'B': 'Miss in set 3; its valid tag is C rather than A', 'C': 'Hit in set 0 with offset 0', 'D': 'Miss in set 2 because the low two bits are 00'},
            'correct_answer': 'B',
            'explanation': '0xAC = 1010 11 00₂, so tag A, set 3, offset 0. Set 3 has valid tag C, so the read misses; tag A in set 0 is irrelevant.',
            'source': '6.1 Caches.pptx; slides 9–11; numerical variant of Cache Diagram.png',
            'image': 'cse320/cache_variant_direct_8bit.svg',
        },
        'Use the pictured 8-bit cache diagram. For address 0x37, what is the result and which byte offset is used?': {
            'subcategory': 'Address mapping',
            'choices': {'A': 'Hit in set 1, offset 3', 'B': 'Hit in set 3, offset 1', 'C': 'Miss in set 1, offset 3', 'D': 'Miss in set 3, offset 1'},
            'correct_answer': 'A',
            'explanation': '0x37 = 0011 01 11₂: tag 3, set 1, offset 3. Set 1 has valid tag 3.',
            'source': '6.1 Caches.pptx; slides 9–11; numerical variant of Cache Diagram.png',
            'image': 'cse320/cache_variant_direct_8bit.svg',
        },
        'Start with the pictured 8-bit cache diagram. Read 0x28 and then 0x2B; a miss loads the entire block. Which result occurs?': {
            'subcategory': 'Address mapping',
            'choices': {'A': 'Two hits because the stored tag in set 2 is 5', 'B': 'Two misses because the offsets differ', 'C': 'Miss, then hit; both addresses use one block', 'D': 'Hit, then miss because the second access changes the tag'},
            'correct_answer': 'C',
            'explanation': 'Both addresses split to tag 2/set 2, with offsets 0 and 3. Set 2 starts invalid, so 0x28 misses and fills its four-byte block; 0x2B then hits it.',
            'source': '6.1 Caches.pptx; slides 9–11, 21; numerical variant of Cache Diagram.png',
            'image': 'cse320/cache_variant_direct_8bit.svg',
        },
        'In Cache #2, address 0x48 misses. The replacement policy is unspecified. Which block numbers are possible eviction choices?': {
            'subcategory': 'Address mapping',
            'choices': {'A': 'Only block number 4', 'B': 'Only block number 5', 'C': 'Either block number 2 or 3', 'D': 'Either block number 4 or 5'},
            'correct_answer': 'D',
            'explanation': '0x48 = tag 4/set 2/offset 0. Both ways of set 2, block numbers 4 and 5, are valid. Either may be selected when the policy is unspecified; no block in another set can be chosen.',
            'source': 'Cache Diagram.png; Cache #2; Caches slides 12–17',
            'image': 'cse320/Cache Diagram.png',
        },
        'In Cache #2, read address 0x14. After handling the access, which statement about set 1 is correct?': {
            'subcategory': 'Address mapping',
            'choices': {'A': 'It hits in block number 2 and leaves set 1 unchanged', 'B': 'It misses and fills block number 3 without eviction', 'C': 'It misses and must evict valid block number 2', 'D': 'It hits because tag 1 is present in set 2'},
            'correct_answer': 'B',
            'explanation': '0x14 = tag 1/set 1/offset 0. Set 1 has valid tag 3 in block number 2 and an invalid block number 3. Tag 1 misses; block number 3 can be filled without removing block number 2.',
            'source': 'Cache Diagram.png; Cache #2; Caches slides 12–14',
            'image': 'cse320/Cache Diagram.png',
        },
        'Using the pictured 8-bit cache diagram, what set, tag, and byte offset does address 0xB6 select?': {
            'subcategory': 'Address-field interpretation',
            'choices': {'A': 'Set 2, tag B, offset 1', 'B': 'Set 1, tag B, offset 2', 'C': 'Set 1, tag 3, offset 2', 'D': 'Set 2, tag B, offset 2'},
            'correct_answer': 'B',
            'explanation': '0xB6 = 1011 01 10₂. The diagram assigns four high bits to the tag, two middle bits to set, and two low bits to offset: tag B, set 1, offset 2.',
            'source': '6.1 Caches.pptx; slides 7, 9–11; numerical variant of Cache Diagram.png',
            'image': 'cse320/cache_variant_direct_8bit.svg',
        },
        'Apply the cache-size relationship printed in the image to a 32-bit byte-addressed cache with 4 KiB of data, 4 ways per set, and 64 bytes per block. Which address-field widths result?': {
            'subcategory': 'Address-field interpretation',
            'choices': {'A': 'Tag 22, set 4, offset 6', 'B': 'Tag 20, set 6, offset 6', 'C': 'Tag 24, set 2, offset 6', 'D': 'Tag 22, set 6, offset 4'},
            'correct_answer': 'A',
            'explanation': 'S=4096/(4×64)=16, so s=4. B=64 gives b=6. The remaining 32−4−6=22 bits form the tag.',
            'source': '6.1 Caches.pptx; slide 7; General cache organization.png',
            'image': 'cse320/General cache organization.png',
        },
        'A cache has a 1-cycle hit time, a 97% hit rate, and a 100-cycle additional miss penalty. What is its average access time?': {
            'subcategory': 'Average access time',
            'choices': {'A': '3 cycles', 'B': '4 cycles', 'C': '98 cycles', 'D': '101 cycles'},
            'correct_answer': 'B',
            'explanation': 'Miss rate is 3%, so average access is 1 + 0.03×100 = 4 cycles. This is the numerical convention used on slide 20.',
            'source': '6.1 Caches.pptx; slides 19–20',
        },
        'An L1 access takes 4 cycles and misses 5% of the time. Each L1 miss adds a 10-cycle L2 lookup. L2 misses 20% of those lookups, and main memory adds 100 cycles on an L2 miss. What is the average access time?': {
            'subcategory': 'Average access time',
            'choices': {'A': '5.5 cycles', 'B': '4.5 cycles', 'C': '9 cycles', 'D': '24 cycles'},
            'correct_answer': 'A',
            'explanation': '4 + 0.05×(10 + 0.20×100) = 4 + 1.5 = 5.5 cycles. The L2 miss rate applies only after an L1 miss.',
            'source': '6.1 Caches.pptx; slides 18–20',
        },
        'A 128-byte direct-mapped cache changes from 8-byte blocks to 16-byte blocks while total data capacity stays fixed. Larger blocks may help spatial locality. Which other changes follow?': {
            'subcategory': 'Design tradeoff',
            'choices': {'A': 'Sets rise to 32; offset falls to 2 bits; conflicts may drop', 'B': 'Sets stay at 16; offset rises to 4 bits; conflicts stay fixed', 'C': 'Sets fall to 8; offset rises to 4 bits; conflicts may rise', 'D': 'Sets fall to 8; offset stays at 3 bits; associativity rises'},
            'correct_answer': 'C',
            'explanation': 'At E=1, S=C/B. Sets fall from 128/8=16 to 128/16=8; log2(B) rises from 3 to 4. Larger blocks bring more nearby bytes, which may help spatial locality, but fewer sets can make more blocks compete for the same set.',
            'source': '6.1 Caches.pptx; slides 7, 19–21',
        },
        'Cache #2 starts as pictured. In set 2, block number 4 was used less recently than block number 5. Read 0x48, 0x6A, 0x18, replacing the least recently used block when the set is full. Which tags occupy set 2 at the end?': {
            'subcategory': 'Address mapping',
            'choices': {'A': 'Tags 1 and 6', 'B': 'Tags 4 and 6', 'C': 'Tags 1 and 4', 'D': 'Only tag 1'},
            'correct_answer': 'A',
            'explanation': 'The diagram shows set 2 contains block number 4 with tag 1 and block number 5 with tag 6. All three accesses select set 2. Tag 4 misses and replaces block number 4; tag 6 hits in block number 5; tag 1 then misses and replaces block number 4. Tags 1 and 6 remain.',
            'source': 'Cache Diagram.png; Cache #2; Caches slides 12–17',
            'image': 'cse320/Cache Diagram.png',
        },
        'Use the pictured 8-bit direct-mapped cache diagram. Read 0xA0, 0xA3, 0xB0, 0xA0 in order, loading a block on each miss. What is the hit/miss sequence?': {
            'subcategory': 'Address mapping',
            'choices': {'A': 'Hit, hit, hit, miss', 'B': 'Miss, hit, miss, hit', 'C': 'Hit, miss, miss, miss', 'D': 'Hit, hit, miss, miss'},
            'correct_answer': 'D',
            'explanation': 'Set 0 initially has valid tag A. 0xA0 and 0xA3 hit the same four-byte block. 0xB0 has tag B/set 0 and replaces A. The last 0xA0 misses.',
            'source': '6.1 Caches.pptx; slides 9–11; numerical variant of Cache Diagram.png',
            'image': 'cse320/cache_variant_direct_8bit.svg',
        },
        'Start cold with the pictured two-way cache and use LRU replacement. Read byte addresses 0, 4, 0, 8, 4. What is the hit/miss sequence?': {
            'subcategory': 'Address mapping',
            'choices': {'A': 'Miss, miss, hit, miss, miss', 'B': 'Miss, miss, hit, miss, hit', 'C': 'Miss, miss, miss, miss, hit', 'D': 'Miss, hit, hit, miss, miss'},
            'correct_answer': 'A',
            'explanation': 'All addresses select set 0, with tags 0, 1, 0, 2, 1. The first two fill its two ways. The next 0 hits, making tag 1 least recently used. Reading 8 misses and evicts tag 1, so the final 4 misses despite having appeared earlier.',
            'source': '6.1 Caches.pptx; slide 14; cache_2way_set_associative_blank_table.png',
            'image': 'cse320/cache_2way_set_associative_blank_table.png',
        },
        'Start with Cache #1 as shown. Read 0x00, 0x04, 0x10, 0x04, 0x00 in order; each miss loads its block. What is the hit/miss sequence?': {
            'subcategory': 'Address mapping',
            'choices': {'A': 'Miss, miss, miss, hit, miss', 'B': 'Miss, miss, miss, miss, hit', 'C': 'Miss, hit, miss, hit, miss', 'D': 'Hit, miss, miss, hit, miss'},
            'correct_answer': 'A',
            'explanation': '0x00 misses in invalid set 0 and loads tag 0. 0x04 misses in set 1 and loads tag 0 there. 0x10 misses in set 0 and replaces tag 0 with tag 1. The next 0x04 hits in set 1, which was unaffected by the set 0 replacement. The final 0x00 misses because set 0 now holds tag 1.',
            'source': 'Cache Diagram.png; Cache #1; Caches slides 9–11',
            'image': 'cse320/Cache Diagram.png',
        },
        'Apply the pictured S/E/B cache organization. A 12-bit byte-addressed cache contains 256 data bytes, 2 ways per set, and 8 bytes per block. What are the tag, set, and offset widths?': {
            'subcategory': 'Address-field interpretation',
            'choices': {'A': 'Tag 4, set 5, offset 3', 'B': 'Tag 6, set 3, offset 3', 'C': 'Tag 5, set 3, offset 4', 'D': 'Tag 5, set 4, offset 3'},
            'correct_answer': 'D',
            'explanation': 'S=256/(2×8)=16 sets. Thus s=4, b=3, and t=12−4−3=5.',
            'source': '6.1 Caches.pptx; slide 7; cache_general_organization_and_address_fields.png',
            'image': 'cse320/cache_general_organization_and_address_fields.png',
        },
        'Suppose all eight cache lines belong to one set and each block has 8 bytes. For a 16-bit byte address, what are the tag, set-index, and offset widths?': {
            'subcategory': 'Address-field interpretation',
            'choices': {'A': 'Tag 13, set 0, offset 3', 'B': 'Tag 10, set 3, offset 3', 'C': 'Tag 13, set 3, offset 0', 'D': 'Tag 16, set 0, offset 0'},
            'correct_answer': 'A',
            'explanation': 'Fully associative means S=1, so the set index uses zero bits. B=8 gives a 3-bit offset, leaving 16−3=13 tag bits.',
            'source': '6.1 Caches.pptx; slides 6–7',
        },
        'A cache has a 1-cycle hit time and a 100-cycle additional miss penalty. Its hit rate improves from 97% to 99%. How does average access time change?': {
            'subcategory': 'Average access time',
            'choices': {'A': 'From 4 to 3 cycles', 'B': 'From 4 to 2 cycles', 'C': 'From 97 to 99 cycles', 'D': 'From 3 to 1 cycles'},
            'correct_answer': 'B',
            'explanation': 'At 97% hits, 1+0.03×100=4 cycles. At 99% hits, 1+0.01×100=2 cycles. The miss-rate change halves average access time here.',
            'source': '6.1 Caches.pptx; slide 20',
        },
        'A workload repeatedly alternates between two blocks that map to the same set. Capacity and block size remain fixed. Which cache change most directly reduces these conflict misses, and what cost may follow?': {
            'subcategory': 'Design tradeoff',
            'choices': {'A': 'Use fewer ways; comparisons drop but conflicts increase', 'B': 'Use write-through; writes update memory but conflicts remain', 'C': 'Use two ways; conflicts may drop but replacement is needed', 'D': 'Use larger blocks; fewer sets may increase conflicts'},
            'correct_answer': 'C',
            'explanation': 'Two ways give both conflicting blocks candidate lines in their selected set, reducing this conflict. Associative lookup and replacement require more work than direct mapping.',
            'source': '6.1 Caches.pptx; slides 6, 12–17',
        },
    },
}

questions["Physical Memory"] = {
    "On the pictured multi-platter drive, a read moves from a track on Surface 0 to the same-radius track on Surface 5. Assuming each surface has a head, which positioning cost can this avoid?": {
        "subcategory": "HDD component", "choices": {"A": "A radial seek to a different cylinder", "B": "All rotational waiting", "C": "Reading the target sector's bits", "D": "Selecting the head for the new surface"},
        "correct_answer": "A", "explanation": "Same-radius tracks lie in one cylinder. The heads move together radially, so switching to another surface at that radius need not seek to a different cylinder. Rotation and head selection may still take time.",
        "source": "6. Physical Memory.pptx slides 12–13, 17 — hdd_multi_platter_cylinder_surfaces.png", "image": "cse320/hdd_multi_platter_cylinder_surfaces.png",
    },
    "A program requests logical disk block 17 without naming a surface, track, or sector. Which component maps that request to its physical disk location?": {
        "subcategory": "HDD component", "choices": {"A": "Read/write head", "B": "Disk controller", "C": "Spindle", "D": "Sector gap"},
        "correct_answer": "B", "explanation": "The disk controller's firmware maps logical blocks to physical (surface, track, sector) locations. The head reads or writes once the location has been selected.",
        "source": "6. Physical Memory.pptx slide 19",
    },
    "On a disk surface, what is the concentric circular path that can be subdivided into sectors?": {
        "subcategory": "HDD component", "choices": {"A": "Platter", "B": "Track", "C": "Cylinder", "D": "Read/write head"},
        "correct_answer": "B", "explanation": "A surface contains concentric tracks. A track is divided into sectors; aligned tracks across surfaces form a cylinder.",
        "source": "6. Physical Memory.pptx slide 11",
    },
    "Which disk component moves in unison with its counterparts from one cylinder to another to read or write a selected surface?": {
        "subcategory": "HDD component", "choices": {"A": "Sector", "B": "Platter", "C": "Read/write head", "D": "Track"},
        "correct_answer": "C", "explanation": "The disk-operation slide says read/write heads move together between cylinders. A sector or track is a storage region, not a moving read/write component.",
        "source": "6. Physical Memory.pptx slide 13",
    },
    "Which storage levels match the approximately 10 million, 100, 10, and 1-cycle tiers, in that order?": {
        "subcategory": "Memory hierarchy", "choices": {"A": "Traditional Disk, Main Memory, Cache, Registers", "B": "Flash Disk, Main Memory, Cache, Registers", "C": "Traditional Disk, Cache, Main Memory, Registers", "D": "Traditional Disk, Main Memory, Registers, Cache"},
        "correct_answer": "A", "explanation": "The approximate latencies identify Traditional Disk, Main Memory, Cache, and Registers in that order. The pyramid ranks storage levels; it does not require every individual access to pass through every level.",
        "source": "6. Physical Memory.pptx slides 3, 38–40 — Physical Memory Hierachy_NO_LABELS.png", "image": "cse320/Physical Memory Hierachy_NO_LABELS.png",
    },
    "Cache starts empty and holds one block. A program makes 100 reads. In case A, every read accesses the same word. In case B, reads alternate between words in two different blocks. Using the diagram's approximate times of 100 cycles per miss and 10 cycles per hit, which case is faster, and why?": {
        "subcategory": "Memory hierarchy", "choices": {"A": "Case A: one miss followed by 99 hits; case B misses on every read", "B": "Case B: alternating blocks lets both remain in Cache", "C": "Both cases take the same time because they make 100 reads", "D": "Case A: every read misses because Cache holds only one block"},
        "correct_answer": "A", "explanation": "In case A, the first read brings the block into Cache and the 99 later reads hit: 100 + 99 × 10 = 1,090 cycles. In case B, each read replaces the other block in the one-block Cache, so all 100 reads miss: 100 × 100 = 10,000 cycles. Reusing the same block gives case A temporal locality.",
        "source": "6. Physical Memory.pptx slides 3, 5, 38–40 — Physical Memory Hierachy.png", "image": "cse320/Physical Memory Hierachy.png",
    },
    "Model Main Memory as a two-block, fully associative cache for Flash Disk. It starts empty and uses LRU replacement. Two programs read the same blocks in different orders: P reads A, B, C, A, B, C; Q reads A, B, A, B, C, C. How many Flash Disk fetches does each order cause?": {
        "subcategory": "Memory hierarchy", "choices": {"A": "P: 6; Q: 3", "B": "P: 3; Q: 3", "C": "P: 6; Q: 6", "D": "P: 3; Q: 6"},
        "correct_answer": "A", "explanation": "P's three-block cycle exceeds the two-block Main Memory cache, so every read misses: 6 Flash Disk fetches. In Q, the second A and B hit before C replaces a block, and the second C hits, giving only 3 fetches. Both orders read each block twice; their temporal locality differs.",
        "source": "6. Physical Memory.pptx slides 5, 38–42; 6.1 Caches.pptx slides 15–17",
    },
    "A disk rotates at 6,000 RPM, has 100 sectors per track, and has a 5 ms average seek. Using the lecture's average-access formula, what is the average time to access one sector?": {
        "subcategory": "HDD access time", "choices": {"A": "5.1 ms", "B": "10.1 ms", "C": "15.1 ms", "D": "10.01 ms"},
        "correct_answer": "B", "explanation": "One rotation is 60/6000 s = 10 ms; average rotation is 5 ms. One-sector transfer is 10/100 = 0.1 ms. Total = 5 + 5 + 0.1 = 10.1 ms.",
        "source": "6. Physical Memory.pptx slides 17–18; FULL CSE 320 Notes (1).docx P148–152",
    },
    "A disk has 500 bytes per sector, 100 sectors per track, 1,000 tracks per surface, two surfaces per platter, and two platters. What raw capacity follows from the lecture formula?": {
        "subcategory": "HDD capacity", "choices": {"A": "50,000,000 bytes", "B": "100,000,000 bytes", "C": "200,000,000 bytes", "D": "400,000,000 bytes"},
        "correct_answer": "C", "explanation": "500 bytes/sector × 100 sectors/track × 1,000 tracks/surface × 2 surfaces/platter × 2 platters = 200,000,000 bytes.",
        "source": "6. Physical Memory.pptx slide 14; FULL CSE 320 Notes (1).docx P143–144",
    },
}

questions["Physical Memory"].update({
    "Which storage category includes Flash Disk and Traditional Disk, and how do those levels generally compare with Main Memory?": {
        "subcategory": "Memory hierarchy", "choices": {"A": "Secondary storage; slower to access but retains stored data without power", "B": "Primary storage; faster to access and retains stored data without power", "C": "Secondary storage; faster to access but loses stored data without power", "D": "On-CPU storage; slower to access and loses stored data without power"},
        "correct_answer": "A", "explanation": "Flash Disk and Traditional Disk are secondary storage. The hierarchy shows that they are slower to access than Main Memory, and unlike volatile DRAM, flash and magnetic disks retain stored data without power.",
        "source": "6. Physical Memory.pptx slides 3, 27–28, 36–37 — Physical Memory Hierachy_NO_CPU_AND_STORAGE_CATEGORIES.png", "image": "cse320/Physical Memory Hierachy_NO_CPU_AND_STORAGE_CATEGORIES.png",
    },
    "At 12,000 RPM, a disk track contains 100 sectors and average seek time is 3 ms. Under the lecture's one-sector model, what is average access time?": {
        "subcategory": "HDD access time", "choices": {"A": "3.05 ms", "B": "5.5 ms", "C": "5.55 ms", "D": "8.05 ms"},
        "correct_answer": "C", "explanation": "One full rotation is 5 ms, so average rotation is 2.5 ms. One-sector transfer takes 5/100 = 0.05 ms. Total = 3 + 2.5 + 0.05 = 5.55 ms.",
        "source": "6. Physical Memory.pptx slides 17–18; FULL CSE 320 Notes (1).docx P153",
    },
    "A disk rotates at 6,000 RPM with 200 sectors per track. Its measured average access time for one sector is 12.55 ms. Using the lecture model, what average seek time is implied?": {
        "subcategory": "HDD access time", "choices": {"A": "7.5 ms", "B": "5 ms", "C": "7.55 ms", "D": "12.5 ms"},
        "correct_answer": "A", "explanation": "One rotation is 10 ms, so average rotation is 5 ms; transfer is 10/200 = 0.05 ms. Seek = 12.55 − 5 − 0.05 = 7.5 ms.",
        "source": "6. Physical Memory.pptx slides 17–18; FULL CSE 320 Notes (1).docx P148–153",
    },
    "A drive specification gives 1,000 bytes per sector, 200 sectors per cylinder, 1,000 cylinders, and two platters. What raw capacity follows?": {
        "subcategory": "HDD capacity", "choices": {"A": "50,000,000 bytes", "B": "200,000,000 bytes", "C": "400,000,000 bytes", "D": "800,000,000 bytes"},
        "correct_answer": "B", "explanation": "1,000 bytes/sector × 200 sectors/cylinder × 1,000 cylinders = 200,000,000 bytes. Sectors per cylinder already covers aligned tracks across the platter surfaces; multiplying by platters again double-counts.",
        "source": "6. Physical Memory.pptx slide 14; FULL CSE 320 Notes (1).docx P143–144",
    },
    "Which comparison best explains why an SSD avoids the HDD's mechanical seek and rotational delay for random reads?": {
        "subcategory": "SSD versus HDD", "choices": {"A": "An SSD has no moving platter or head", "B": "An SSD stores every page in a rotating cylinder", "C": "An HDD erases flash blocks before reading", "D": "An HDD's sectors have no physical location"},
        "correct_answer": "A", "explanation": "The SSD tradeoff slide identifies no moving parts as an advantage. HDD accesses wait for a head to reach the cylinder and a sector to rotate under it.",
        "source": "6. Physical Memory.pptx slides 17, 23–25",
    },
    "Why do the course notes discourage defragmenting an SSD, even though defragmentation can help a rotating disk?": {
        "subcategory": "SSD versus HDD", "choices": {"A": "SSD pages must remain in physical track order", "B": "Defragmentation disables the drive's wear leveling", "C": "Fragmented SSD files require extra head movement", "D": "It adds flash wear without a head-movement benefit"},
        "correct_answer": "D", "explanation": "The notes say SSD defragmentation wastes lifetime and lacks the moving parts that make fragmented HDD access costly. SSD flash also has limited erase/write endurance.",
        "source": "FULL CSE 320 Notes (1).docx P258; 6. Physical Memory.pptx slides 23–25",
    },
})

questions["Basic Code"] = {
    "Assume `int` is 4 bytes, `a` is 16-byte aligned, and a cold cache has 16-byte blocks and at least two nonconflicting lines. Count only reads of `a` in `for (int i=0; i<8; i++) use(a[i]);`. How many misses and hits occur?": {
        "subcategory": "Program cache hit/miss", "choices": {"A": "8 misses, 0 hits", "B": "4 misses, 4 hits", "C": "2 misses, 6 hits", "D": "1 miss, 7 hits"},
        "correct_answer": "C", "explanation": "Each 16-byte block holds four ints. The eight sequential reads touch two blocks, so the first access to each misses and the other six hit.",
        "source": "6.1 Caches.pptx slides 9–14, 21; 6. Physical Memory.pptx slides 5–6",
    },
    "Assume `int` is 4 bytes, `a` is 8-byte aligned, and the cache starts cold with 8-byte blocks. Count only reads of `a` in `for (int i=0; i<8; i+=2) use(a[i]);`. How many hits occur?": {
        "subcategory": "Program cache hit/miss", "choices": {"A": "0", "B": "1", "C": "2", "D": "4"},
        "correct_answer": "A", "explanation": "The reads are a[0], a[2], a[4], a[6]. Each 8-byte block holds two ints, so the stride skips the neighbor and every read enters a new cold block.",
        "source": "6.1 Caches.pptx slides 9–14, 21; 6. Physical Memory.pptx slides 5–6",
    },
    "Assume `int` is 4 bytes, `a` is 8-byte aligned, and a cold direct-mapped cache has two sets and 8-byte blocks. No other data accesses affect it. Count reads of `a` in `for (int pass=0; pass<2; pass++) for (int i=0; i<4; i++) use(a[i]);`. What is the total hit/miss count?": {
        "subcategory": "Program cache hit/miss", "choices": {"A": "4 misses, 4 hits", "B": "2 misses, 6 hits", "C": "1 miss, 7 hits", "D": "8 misses, 0 hits"},
        "correct_answer": "B", "explanation": "Four ints occupy two 8-byte blocks, one in each set. The first pass has two compulsory misses and two hits; both blocks remain for four hits on the second pass.",
        "source": "6.1 Caches.pptx slides 9–14, 21; 6. Physical Memory.pptx slides 5–6",
    },
    "What is `x` after `int x=4; int *p=&x; *p+=3; x+=1;`?": {
        "subcategory": "Code concepts", "choices": {"A": "4", "B": "7", "C": "8", "D": "The address of x"},
        "correct_answer": "C", "explanation": "The dereference changes x from 4 to 7, and the final direct update changes it to 8.",
        "source": "FULL CSE 320 Notes (1).docx P308, basic-code pointer scope",
    },
    "After `int a[4]={2,4,6,8}; int *p=a+1; *(p+1)=*p+5;`, what is `a[2]`?": {
        "subcategory": "Code concepts", "choices": {"A": "4", "B": "9", "C": "11", "D": "8"},
        "correct_answer": "B", "explanation": "p points to a[1], whose value is 4. p+1 points to a[2], so the assignment stores 4+5=9 there.",
        "source": "FULL CSE 320 Notes (1).docx P308, basic-code pointer scope",
    },
    "After `int x=2, y=7; int *p=&x; p=&y; *p=9;`, what are `(x,y)`?": {
        "subcategory": "Code concepts", "choices": {"A": "(9,7)", "B": "(9,9)", "C": "(2,7)", "D": "(2,9)"},
        "correct_answer": "D", "explanation": "Reassigning p changes its target from x to y. The final dereference writes y, leaving x at 2.",
        "source": "FULL CSE 320 Notes (1).docx P308, basic-code pointer scope",
    },
    "After `int x=1; int *p=&x, *q=&x; *p=4; *q+=3;`, what is `x`?": {
        "subcategory": "Code concepts", "choices": {"A": "4", "B": "7", "C": "8", "D": "1"},
        "correct_answer": "B", "explanation": "p and q both point to x. The first write makes x=4; the second adds 3 to that same object, giving 7.",
        "source": "5. Optimizations and Profiling.pptx slides 36–38; FULL CSE 320 Notes (1).docx P279",
    },
    "For `int f(int *p,int *q){ *p=3; *q=5; return *p; }`, what are the results of `f(&x,&x)` and `f(&x,&y)` respectively, with valid distinct `x` and `y`?": {
        "subcategory": "Code concepts", "choices": {"A": "3, 5", "B": "5, 5", "C": "5, 3", "D": "3, 3"},
        "correct_answer": "C", "explanation": "When both arguments name x, the write through q overwrites the 3, so f returns 5. With distinct objects, the later q write does not change *p, so f returns 3.",
        "source": "5. Optimizations and Profiling.pptx slides 36–38",
    },
    "In `int f(int *p,int *q){ int a=*p; *q=7; int b=*p; return a+b; }`, why can't the compiler always reuse the first load for `b`?": {
        "subcategory": "Code concepts", "choices": {"A": "p and q may point to the same object", "B": "All pointer loads are volatile", "C": "The linker may replace the function body", "D": "A local variable cannot hold a loaded value"},
        "correct_answer": "A", "explanation": "If p and q alias, writing 7 through q changes the later value of *p. Reusing a would change program behavior.",
        "source": "5. Optimizations and Profiling.pptx slides 22–23, 36–38",
    },
    "For row-major C array `int a[4][8]`, which loop nest reads `a` with stride 1 in its inner loop?": {
        "subcategory": "Code concepts", "choices": {"A": "`for(j=0;j<8;j++) for(i=0;i<4;i++) use(a[i][j]);`", "B": "`for(i=0;i<4;i++) for(j=0;j<8;j++) use(a[i][j]);`", "C": "Both nests have stride 1", "D": "Neither nest has stride 1"},
        "correct_answer": "B", "explanation": "C stores each row contiguously. Varying the last subscript j in the inner loop reads adjacent ints.",
        "source": "6. Physical Memory.pptx slides 5–8; 6.1 Caches.pptx slide 21",
    },
    "For row-major `int a[4][8]`, the inner loop varies `i` in `use(a[i][j])` while `j` is fixed. What is the stride in int elements between consecutive inner-loop reads?": {
        "subcategory": "Code concepts", "choices": {"A": "1", "B": "4", "C": "8", "D": "32"},
        "correct_answer": "C", "explanation": "Each increment of i moves to the same column in the next row. One row contains eight ints, so the address advances by eight int elements.",
        "source": "6. Physical Memory.pptx slides 5–8",
    },
    "In `int sum=0; for(int i=0;i<n;i++) sum+=a[i];`, which pairing correctly describes the loop's locality?": {
        "subcategory": "Code concepts", "choices": {"A": "sum: temporal locality; a[i]: spatial locality", "B": "sum: spatial locality; a[i]: temporal locality", "C": "sum and a[i]: temporal locality only", "D": "sum and a[i]: neither kind of locality"},
        "correct_answer": "A", "explanation": "sum is reused each iteration, giving temporal locality. Consecutive a elements reside at nearby addresses, giving spatial locality.",
        "source": "6. Physical Memory.pptx slides 5–6",
    },
}

questions["Basic Code"].update({
    "After `int a[3]={1,2,3}; int *b=&a[1]; for(int i=0;i<3;i++) *b += a[i];`, what is `a[1]`?": {
        "subcategory": "Code concepts", "choices": {"A": "8", "B": "5", "C": "6", "D": "9"},
        "correct_answer": "D", "explanation": "b aliases a[1]. The loop changes it from 2 to 3 at i=0, then to 6 at i=1 because a[1] is now 3, then to 9 at i=2. A local accumulator that delayed the write would produce 8 instead.",
        "source": "5. Optimizations and Profiling.pptx slides 35–38",
    },
    "Compare `for(i=0;i<n;i++) *b += a[i];` with `int t=*b; for(i=0;i<n;i++) t+=a[i]; *b=t;`. What is the main optimization opportunity in the second version?": {
        "subcategory": "Code concepts", "choices": {"A": "It eliminates all array reads", "B": "It always preserves behavior even when b aliases a", "C": "It keeps the sum local and writes through b once", "D": "It turns a into read-only memory"},
        "correct_answer": "C", "explanation": "The local accumulator can stay in a register and stores to *b once. If b aliases a, the two snippets can behave differently, so equivalence must not be assumed without a nonaliasing condition.",
        "source": "5. Optimizations and Profiling.pptx slides 35–38",
    },
    "In `for(int j=0;j<n;j++) a[n*i+j]=b[j];`, assume `n` and `i` do not change in the loop. Which named optimization computes `n*i` once before the loop?": {
        "subcategory": "Code concepts", "choices": {"A": "Code motion", "B": "Loop unrolling", "C": "Inlining", "D": "Relocation"},
        "correct_answer": "A", "explanation": "n*i is loop invariant. Code motion moves that multiplication outside the j loop, matching the lecture's set_row example.",
        "source": "5. Optimizations and Profiling.pptx slides 24–25",
    },
    "In `for(int i=0;i<n;i++) use(i*8);`, a running value starts at 0 and increases by 8 per iteration instead of multiplying each time. Which named optimization is this?": {
        "subcategory": "Code concepts", "choices": {"A": "Common subexpression sharing", "B": "Reduction in strength", "C": "Loop unrolling", "D": "Code motion"},
        "correct_answer": "B", "explanation": "A repeated multiplication is replaced by a cheaper addition recurrence, the slide's reduction-in-strength pattern.",
        "source": "5. Optimizations and Profiling.pptx slide 26",
    },
    "For `int t=(x+y)*(x+y);`, which transformation avoids computing `x+y` twice without changing the operands?": {
        "subcategory": "Code concepts", "choices": {"A": "Compute each `x+y` separately as written", "B": "Move the multiplication outside the function regardless of x and y", "C": "Replace each `x+y` with `x*y`", "D": "Store `x+y` in a temporary and use that result twice"},
        "correct_answer": "D", "explanation": "Sharing the common subexpression computes x+y once and reuses it. The source has no intervening writes to x or y.",
        "source": "5. Optimizations and Profiling.pptx slide 27",
    },
    "Assume `n` is a multiple of 4. A loop changes from one `use(a[i])` per iteration to four calls on `a[i]` through `a[i+3]`, increasing `i` by 4. What benefit is loop unrolling intended to provide?": {
        "subcategory": "Code concepts", "choices": {"A": "It removes all data accesses", "B": "It makes every call inline automatically", "C": "It reduces loop-control work per element", "D": "It guarantees no cache misses"},
        "correct_answer": "C", "explanation": "Four elements are handled per branch and index update. Unrolling reduces loop-control overhead per element without guaranteeing cache hits or inlining.",
        "source": "5. Optimizations and Profiling.pptx slides 20, 52–53; FULL CSE 320 Notes (1).docx P280",
    },
    "Given `int square(int x){return x*x;}` and `int y=square(v);`, what does function inlining do at the call site?": {
        "subcategory": "Code concepts", "choices": {"A": "It replaces the call with square's body", "B": "It changes square into a macro before compilation", "C": "It resolves square's symbol but leaves the call in place", "D": "It moves the result outside every loop regardless of v"},
        "correct_answer": "A", "explanation": "Inlining replaces the call with the callee's work at the call site. The slides discuss it as a way to reduce frequent procedure-call overhead.",
        "source": "5. Optimizations and Profiling.pptx slides 14–15, 19–20",
    },
    "Given `void unknown(void); int f(int *p){int a=*p; unknown(); int b=*p; return a+b;}`, assume `unknown()` could modify the object reached through p. Why is replacing `b=*p` with `b=a` unsafe?": {
        "subcategory": "Code concepts", "choices": {"A": "p must point to a cache line", "B": "The call can change *p between the two reads", "C": "The assembler cannot represent two loads", "D": "The second read is always a cache miss"},
        "correct_answer": "B", "explanation": "The unknown procedure may have a side effect on the pointed-to object, so the second value need not equal the first.",
        "source": "5. Optimizations and Profiling.pptx slides 22–23, 28–34",
    },
    "Under the lecture's linker rules, file a.c defines `int x=3;` and file b.c defines `int x=4;`. What happens when the files are linked?": {
        "subcategory": "Global variables", "choices": {"A": "The linker chooses x=3", "B": "The linker chooses x=4", "C": "Link error: two strong definitions of x", "D": "Two independent global x objects remain"},
        "correct_answer": "C", "explanation": "Both initialized global definitions are strong. The lecture's first duplicate-symbol rule forbids two strong definitions with the same name.",
        "source": "7. Compiler Toolchains.pptx slides 16–18; FULL CSE 320 Notes (1).docx P297–299",
    },
    "Under the lecture's linker rules, file a.c has `int x;` and file b.c has `int x=7;`. Which definition does a reference to x use?": {
        "subcategory": "Global variables", "choices": {"A": "The initialized strong definition in b.c", "B": "The uninitialized weak definition in a.c", "C": "Both definitions cause a two-strong-symbol error", "D": "The reference is unresolved"},
        "correct_answer": "A", "explanation": "An uninitialized global is weak under the lecture model; the initialized global is strong. The linker chooses the strong definition.",
        "source": "7. Compiler Toolchains.pptx slides 16–18",
    },
    "Under the lecture's model, file a.c defines `int x=7;`. File b.c contains `extern int x; int f(void){return x;}`. What does f return after successful linking?": {
        "subcategory": "Global variables", "choices": {"A": "0", "B": "An unpredictable weak value", "C": "A link error from two definitions", "D": "7"},
        "correct_answer": "D", "explanation": "extern in b.c declares a reference, not another definition. Symbol resolution connects it to a.c's initialized x, so f returns 7.",
        "source": "7. Compiler Toolchains.pptx slides 7, 13, 19; FULL CSE 320 Notes (1).docx P296–299",
    },
    "File a.c has `static int x=2; int f(void){return x;}`. File b.c has `int x=5;`. What does f return under the lecture's linker model?": {
        "subcategory": "Global variables", "choices": {"A": "5", "B": "2", "C": "A duplicate-strong-symbol error", "D": "An arbitrary weak value"},
        "correct_answer": "B", "explanation": "File-scope static x is a local linker symbol in a.c, separate from b.c's global x. f reads its own file's x, which is 2.",
        "source": "7. Compiler Toolchains.pptx slides 13, 16–19",
    },
    "Given `int g=4; int z; int next(void){static int n=1; return ++n;}`, which statement matches the lecture's storage model and two successive calls to next?": {
        "subcategory": "Global variables", "choices": {"A": "g and n are on the stack; calls return 2 then 2", "B": "g is in .bss, z in .data; calls return 1 then 1", "C": "g and n are in .data, z in .bss; calls return 2 then 3", "D": "All three are in .text; calls return 1 then 2"},
        "correct_answer": "C", "explanation": "Initialized global g and initialized static local n have static storage in .data under the slide model; uninitialized global z is in .bss. n persists across calls, so prefix increment returns 2, then 3.",
        "source": "7. Compiler Toolchains.pptx slides 11, 15–16",
    },
})

questions["General Concepts"] = {
    "Two expressions in a C program may refer to the same storage location, so a write through one can change a later read through the other. Which term describes this?": {
        "subcategory": "Definition identification", "choices": {"A": "Memory Aliasing", "B": "Relocation", "C": "Spatial Locality", "D": "Symbol Resolution"},
        "correct_answer": "A", "explanation": "Memory aliasing means two different references designate one location. The possibility can block a compiler from reusing a prior load.",
        "source": "5. Optimizations and Profiling.pptx slides 35–38; FULL CSE 320 Notes (1).docx P98",
    },
    "The notes list a nonvolatile memory category intended primarily to be read and contrast it with programmable and erasable variants. Which official term is being described?": {
        "subcategory": "Definition identification", "choices": {"A": "Volatile Memory", "B": "Read Only Memory", "C": "Memory Bus", "D": "Write-Back"},
        "correct_answer": "B", "explanation": "The notes group read-only memory with nonvolatile ROM variants. Volatile RAM loses its contents when power is removed.",
        "source": "Copy of CSE 320 Notes.docx P110–113; FULL CSE 320 Notes (1).docx P304",
    },
    "A device signals the CPU that an event needs attention instead of making the CPU check continuously. Which official term matches?": {
        "subcategory": "Definition identification", "choices": {"A": "DMA", "B": "Branch Prediction", "C": "Interrupt", "D": "Memory Bus"},
        "correct_answer": "C", "explanation": "An interrupt alerts the CPU to an event; polling makes the CPU repeatedly check for one.",
        "source": "6. Physical Memory.pptx slide 22; Copy of CSE 320 Notes.docx P164–165",
    },
    "A cache removes an existing block to make room for a newly requested block. Which term names the removal?": {
        "subcategory": "Definition identification", "choices": {"A": "Write-through", "B": "Relocation", "C": "DMA", "D": "Eviction"},
        "correct_answer": "D", "explanation": "Eviction removes cache data to free a line. In an associative cache, a replacement policy selects which line leaves.",
        "source": "6.1 Caches.pptx slides 16–17",
    },
    "SRAM and DRAM lose stored information when the machine is powered off. Which memory category does that describe?": {
        "subcategory": "Definition identification", "choices": {"A": "Volatile Memory", "B": "Read Only Memory", "C": "Write-Back", "D": "Memory Bus"},
        "correct_answer": "A", "explanation": "The slides identify SRAM and DRAM as volatile because their contents are lost without power.",
        "source": "6. Physical Memory.pptx slides 27, 36–37; Copy of CSE 320 Notes.docx P108–113",
    },
    "Trace DMA data from the disk controller toward main memory in the unlabeled figure. Which named bus carries it from the controller to the I/O bridge?": {
        "subcategory": "Definition identification", "choices": {"A": "Memory Bus", "B": "IO Bus", "C": "DMA", "D": "Interrupt"},
        "correct_answer": "B", "explanation": "The disk controller sits on the I/O bus, which connects peripheral controllers to the I/O bridge. DMA then moves data onward toward main memory without the CPU copying each word.",
        "source": "6. Physical Memory.pptx slides 20–21; io_memory_bus_diagram_UNLABELED.png", "image": "cse320/io_memory_bus_diagram_UNLABELED.png",
    },
    "Continue the disk-to-memory DMA path through the I/O bridge in the unlabeled figure. Which named bus carries the data from that bridge to main memory?": {
        "subcategory": "Definition identification", "choices": {"A": "IO Bus", "B": "DMA", "C": "Memory Bus", "D": "Interrupt"},
        "correct_answer": "C", "explanation": "The memory bus connects the I/O bridge to main memory. The I/O bus is on the controller side of the bridge, and the system bus is on the CPU side.",
        "source": "6. Physical Memory.pptx slides 20–21; io_memory_bus_diagram_UNLABELED.png", "image": "cse320/io_memory_bus_diagram_UNLABELED.png",
    },
    "Specialized hardware copies a large amount of data between memory and a device without the CPU handling each transferred word. Which term matches?": {
        "subcategory": "Definition identification", "choices": {"A": "Memory Bus", "B": "Interrupt", "C": "Write-Through", "D": "DMA"},
        "correct_answer": "D", "explanation": "Direct Memory Access performs bulk transfers without making the CPU babysit each word; an interrupt can notify the CPU when the transfer finishes.",
        "source": "6. Physical Memory.pptx slide 21; Copy of 320 midterm 1 notes.docx P151–165",
    },
    "A loop body handles several consecutive original iterations before its next loop-control test. Which optimization term describes this transformation?": {
        "subcategory": "Definition identification", "choices": {"A": "Loop Unrolling", "B": "Inlining", "C": "Code Motion", "D": "Reduction in Strength"},
        "correct_answer": "A", "explanation": "Loop unrolling repeats the per-iteration work within one larger iteration, reducing loop-control overhead and sometimes exposing parallel work.",
        "source": "5. Optimizations and Profiling.pptx slides 52–53; FULL CSE 320 Notes (1).docx P280",
    },
    "Before a conditional branch is resolved, a processor guesses its direction and starts fetching from the predicted path. Which term matches?": {
        "subcategory": "Definition identification", "choices": {"A": "Inlining", "B": "Branch Prediction", "C": "Super scalar", "D": "Code Motion"},
        "correct_answer": "B", "explanation": "Branch prediction guesses whether a branch will be taken so the processor can continue fetching; a wrong guess requires recovery.",
        "source": "5. Optimizations and Profiling.pptx slides 66–69; Copy of 320 midterm 1 notes.docx P82",
    },
}

questions["General Concepts"].update({
    "A small frequently called function has its body substituted at each call site, potentially removing call overhead. Which term describes this?": {
        "subcategory": "Definition identification", "choices": {"A": "Loop Unrolling", "B": "Inlining", "C": "Code Motion", "D": "Reduction in Strength"},
        "correct_answer": "B", "explanation": "Inlining places the callee's work at a call site rather than executing a separate call. It is distinct from repeating loop iterations.",
        "source": "5. Optimizations and Profiling.pptx slides 14–15, 19–20",
    },
    "A calculation whose value cannot change during a loop is performed once before the loop instead of on every iteration. Which optimization is this?": {
        "subcategory": "Definition identification", "choices": {"A": "Reduction in Strength", "B": "Inlining", "C": "Loop Unrolling", "D": "Code Motion"},
        "correct_answer": "D", "explanation": "Code motion moves loop-invariant work out of the loop, reducing how often it runs.",
        "source": "5. Optimizations and Profiling.pptx slides 24–25",
    },
    "A repeated multiplication in a loop is replaced by an addition that advances a running value. Which optimization term matches?": {
        "subcategory": "Definition identification", "choices": {"A": "Reduction in Strength", "B": "Code Motion", "C": "Inlining", "D": "Loop Unrolling"},
        "correct_answer": "A", "explanation": "Reduction in strength substitutes a cheaper operation, such as an addition recurrence, for a more costly repeated multiplication.",
        "source": "5. Optimizations and Profiling.pptx slide 26",
    },
    "A processor can issue and execute multiple instructions during one cycle by exploiting instruction-level parallelism. Which course term describes it?": {
        "subcategory": "Definition identification", "choices": {"A": "Branch Prediction", "B": "Throughput", "C": "Super scalar", "D": "Loop Unrolling"},
        "correct_answer": "C", "explanation": "The slide defines a superscalar processor as one that can issue and execute multiple instructions in a cycle.",
        "source": "5. Optimizations and Profiling.pptx slide 47; Copy of 320 midterm 1 notes.docx P83–84",
    },
    "For one operation, a measurement gives the time between starting it and having its result ready. Which performance term is being measured?": {
        "subcategory": "Definition identification", "choices": {"A": "Throughput", "B": "Latency", "C": "Branch Prediction", "D": "Profiler"},
        "correct_answer": "B", "explanation": "Latency is the delay for one operation or dependent result; throughput instead measures how many operations can be completed per unit time.",
        "source": "5. Optimizations and Profiling.pptx slides 48–49; Copy of CSE 320 Notes.docx P69–70",
    },
    "A measurement gives the maximum number of operations a system can complete per second when its hardware units are kept busy. Which term is this?": {
        "subcategory": "Definition identification", "choices": {"A": "Latency", "B": "Branch Prediction", "C": "Super scalar", "D": "Throughput"},
        "correct_answer": "D", "explanation": "Throughput is work completed per unit time. Latency instead describes how long one operation takes.",
        "source": "Copy of CSE 320 Notes.docx P69–70; 6.1 Caches.pptx slide 22",
    },
    "After a program reads one array element, it soon reads neighboring addresses. Which locality term describes the pattern?": {
        "subcategory": "Definition identification", "choices": {"A": "Spatial Locality", "B": "Temporal Locality", "C": "Memory Aliasing", "D": "Code Motion"},
        "correct_answer": "A", "explanation": "Spatial locality is the tendency to access nearby addresses close together in time, as in stride-1 array traversal.",
        "source": "6. Physical Memory.pptx slides 5–7",
    },
    "A program reuses an item it accessed recently, such as an accumulator on each loop iteration. Which locality term describes this?": {
        "subcategory": "Definition identification", "choices": {"A": "Spatial Locality", "B": "Memory Aliasing", "C": "Temporal Locality", "D": "Branch Prediction"},
        "correct_answer": "C", "explanation": "Temporal locality is reuse of the same recently referenced item; spatial locality concerns nearby addresses.",
        "source": "6. Physical Memory.pptx slides 5–6",
    },
    "After a cache write hit, the changed line is kept locally and lower memory is updated when that line is replaced. Which write policy is described?": {
        "subcategory": "Definition identification", "choices": {"A": "Write-Through", "B": "Write-Back", "C": "DMA", "D": "Eviction"},
        "correct_answer": "B", "explanation": "Write-back defers the lower-level write until replacement and uses a dirty bit to record that the line differs from memory.",
        "source": "6.1 Caches.pptx slide 15",
    },
    "After a cache write hit, the change is propagated immediately to lower memory rather than waiting for replacement. Which write policy is described?": {
        "subcategory": "Definition identification", "choices": {"A": "Write-Back", "B": "Eviction", "C": "DMA", "D": "Write-Through"},
        "correct_answer": "D", "explanation": "Write-through writes through to lower memory on the hit. Write-back defers that update until the dirty line is replaced.",
        "source": "6.1 Caches.pptx slide 15",
    },
})

questions["General Concepts"].update({
    "The linker associates each reference to a function or global name with exactly one definition from its input object files. Which linker task is this?": {
        "subcategory": "Definition identification", "choices": {"A": "Relocation", "B": "Inlining", "C": "Symbol Resolution", "D": "Code Motion"},
        "correct_answer": "C", "explanation": "Symbol resolution connects references with definitions. Relocation later adjusts their addresses in the combined output.",
        "source": "7. Compiler Toolchains.pptx slides 6–8",
    },
    "After combining object-file sections, the linker adjusts symbol positions and the code/data references to their final locations. Which task is described?": {
        "subcategory": "Definition identification", "choices": {"A": "Relocation", "B": "Symbol Resolution", "C": "Inlining", "D": "Assembler"},
        "correct_answer": "A", "explanation": "Relocation assigns final locations and updates references to them. Symbol resolution decides which definition each reference names.",
        "source": "7. Compiler Toolchains.pptx slides 6, 8, 20",
    },
    "The compiler produces code intended to work when loaded at different memory locations instead of relying on a fixed starting address. Which term matches?": {
        "subcategory": "Definition identification", "choices": {"A": "Relocation", "B": "Symbol Resolution", "C": "Reduction in Strength", "D": "Position Independent Code"},
        "correct_answer": "D", "explanation": "The PIC slide describes code built without depending on an ELF start at address zero so it can be loaded at arbitrary locations.",
        "source": "7. Compiler Toolchains.pptx slide 40",
    },
    "A tool records where a running program spends time or allocates memory so a developer can find hot spots. Which course term matches?": {
        "subcategory": "Definition identification", "choices": {"A": "Debugger", "B": "Profiler", "C": "Compiler", "D": "Linker"},
        "correct_answer": "B", "explanation": "A profiler measures execution or allocation behavior and helps identify expensive functions; the slides use gprof as an example.",
        "source": "5. Optimizations and Profiling.pptx slides 5–6, 12–13",
    },
    "The course notes name GDB as a tool for investigating a program while finding defects. Which official term identifies that kind of tool?": {
        "subcategory": "Definition identification", "choices": {"A": "Profiler", "B": "Assembler", "C": "Debugger", "D": "Linker"},
        "correct_answer": "C", "explanation": "GDB is the debugger named in the notes; its role is investigating program behavior while locating defects. A profiler measures performance instead.",
        "source": "FULL CSE 320 Notes (1).docx P2, P46, P304",
    },
    "In the course's toolchain diagram, `cc` translates preprocessed C (`.i`) into assembly (`.s`). Which stage is `cc` performing?": {
        "subcategory": "Definition identification", "choices": {"A": "Compiler", "B": "Assembler", "C": "Linker", "D": "Debugger"},
        "correct_answer": "A", "explanation": "The compiler converts preprocessed C to assembly. The slide names cc for this stage, followed by as and ld.",
        "source": "7. Compiler Toolchains.pptx slides 2–3",
    },
    "In the course's toolchain diagram, `ld` combines relocatable `.o` files, resolves symbols, and produces an executable. Which stage is `ld`?": {
        "subcategory": "Definition identification", "choices": {"A": "Compiler", "B": "Assembler", "C": "Profiler", "D": "Linker"},
        "correct_answer": "D", "explanation": "ld is the linker. It combines object files and performs symbol resolution and relocation to form an executable.",
        "source": "7. Compiler Toolchains.pptx slides 2, 6–8",
    },
    "In the course's toolchain diagram, `as` converts assembly (`.s`) into a relocatable object file (`.o`). Which stage is `as`?": {
        "subcategory": "Definition identification", "choices": {"A": "Linker", "B": "Assembler", "C": "Compiler", "D": "Profiler"},
        "correct_answer": "B", "explanation": "as is the assembler. It translates assembly into a relocatable object file for the linker.",
        "source": "7. Compiler Toolchains.pptx slides 2–3",
    },
    "A function receives `int *p`. Which statement distinguishes `p++` from `(*p)++` inside the function?": {
        "subcategory": "Concept", "choices": {"A": "Both change the caller's pointer variable", "B": "Both increment the pointed-to int", "C": "`p++` moves the pointer; `(*p)++` changes the int", "D": "`p++` changes the int; `(*p)++` moves p"},
        "correct_answer": "C", "explanation": "The parentheses make the dereference happen before incrementing the int. Without them, postfix ++ advances the local pointer value.",
        "source": "FULL CSE 320 Notes (1).docx P304, P308, pointer scope",
    },
    "A compiler sees `int a=*p; *q=9; int b=*p;` with pointer arguments that may be equal. Which assumption is unsafe?": {
        "subcategory": "Concept", "choices": {"A": "The second `*p` must equal the first", "B": "The write through q may change *p", "C": "p and q can refer to one object", "D": "The source order matters when p and q alias"},
        "correct_answer": "A", "explanation": "If p and q alias, the write of 9 changes the value seen by the second *p load. The compiler cannot always reuse a.",
        "source": "5. Optimizations and Profiling.pptx slides 22–23, 35–38",
    },
    "For row-major `int a[4][8]`, which inner-loop access pattern generally gets better spatial locality: increasing `j` in `a[i][j]` or increasing `i` in `a[i][j]`?": {
        "subcategory": "Concept", "choices": {"A": "Increasing i, because it stays in one column", "B": "Increasing j, because array elements are contiguous", "C": "Both have identical address stride", "D": "Neither accesses neighboring elements"},
        "correct_answer": "B", "explanation": "C stores the last subscript contiguously. Incrementing j steps to the next int, while incrementing i skips a whole row of eight ints.",
        "source": "6. Physical Memory.pptx slides 5–8",
    },
    "A loop calls `strlen(s)` in its condition on every iteration while also changing characters of `s`. Why may the compiler hesitate to move that call outside the loop?": {
        "subcategory": "Concept", "choices": {"A": "Moving calls is the linker's job", "B": "Every strlen result is always different", "C": "A cache block cannot store the string", "D": "The call's result may change as s changes"},
        "correct_answer": "D", "explanation": "The optimization slides treat a procedure call as a possible black box with side effects or changing results. Explicitly storing the length before the loop is code motion when safe.",
        "source": "5. Optimizations and Profiling.pptx slides 28–34",
    },
    "Starting with C source, which tool order produces an executable?": {
        "subcategory": "Concept", "choices": {"A": "`cpp` → `cc` → `as` → `ld`", "B": "`cc` → `cpp` → `ld` → `as`", "C": "`as` → `cpp` → `cc` → `ld`", "D": "`ld` → `as` → `cc` → `cpp`"},
        "correct_answer": "A", "explanation": "The driver slide orders preprocessing (cpp), compilation (cc), assembly (as), and linking (ld).",
        "source": "7. Compiler Toolchains.pptx slide 2",
    },
    "A flat profile shows one function consumes about 80% of runtime. Which next step follows the course's optimization workflow?": {
        "subcategory": "Concept", "choices": {"A": "Rewrite every function before measuring again", "B": "Disable compiler optimization to keep the result stable", "C": "Optimize the hot function, then measure again", "D": "Optimize only the function with the fewest calls"},
        "correct_answer": "C", "explanation": "The slides recommend using profiles to focus on functions consuming the most time and comparing results after a change.",
        "source": "5. Optimizations and Profiling.pptx slides 3, 5, 12–13",
    },
})
