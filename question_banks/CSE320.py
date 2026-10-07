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
    """Consider this loop:

```c
int sum = 0;
for (int i = 0; i < n; i++) {
    sum += a[i];
}
```

Which pairing correctly describes the loop's locality?""": {
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
    "Code motion changes `for(int j=0;j<n;j++) a[n*i+j]=b[j];` by computing `n*i` before the loop. If the loop runs n times, how does this affect the number of `n*i` multiplications?": {
        "subcategory": "Code concepts", "choices": {"A": "It falls from n multiplications to 1", "B": "It rises from 1 multiplication to n", "C": "It remains n because the expression still appears in the index", "D": "It falls to 0 because the multiplication is replaced by division"},
        "correct_answer": "A", "explanation": "Because n and i do not change during the j loop, code motion computes their product once before the loop and reuses it for all n iterations.",
        "source": "5. Optimizations and Profiling.pptx slides 24–25",
    },
    "Reduction in strength rewrites `for(int i=0;i<n;i++) use(i*8);` to update a running value after each call. Which update preserves the original argument sequence?": {
        "subcategory": "Code concepts", "choices": {"A": "Start at 8 and subtract 1", "B": "Start at 0 and add 8", "C": "Start at 0 and add i", "D": "Start at n and divide by 8"},
        "correct_answer": "B", "explanation": "The original arguments are 0, 8, 16, and so on. Starting at 0 and adding 8 after each use produces the same sequence without multiplying on every iteration.",
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
    "What is memory aliasing?": {
        "subcategory": "Definition recall", "answer": "Memory aliasing occurs when different expressions or references designate the same storage location, so a write through one may affect a read through another.",
        "source": "5. Optimizations and Profiling.pptx slides 35–38; FULL CSE 320 Notes (1).docx P98, P139, P304",
    },
    "What is read-only memory (ROM)?": {
        "subcategory": "Definition recall", "answer": "Read-only memory is nonvolatile memory intended primarily for reading stored data. ROM variants differ in whether and how their contents can be programmed or erased.",
        "source": "Copy of CSE 320 Notes.docx P110–113; FULL CSE 320 Notes (1).docx P304",
    },
    "What is an interrupt?": {
        "subcategory": "Definition recall", "answer": "An interrupt is a signal that causes the CPU to suspend its current work and handle an event, allowing a device to request attention without continuous polling.",
        "source": "6. Physical Memory.pptx slide 22; Copy of CSE 320 Notes.docx P164–165",
    },
    "What is cache eviction?": {
        "subcategory": "Definition recall", "answer": "Cache eviction is the removal of a resident cache block to make a cache line available for another block. A replacement policy selects the victim when necessary.",
        "source": "6.1 Caches.pptx slides 16–17",
    },
    "What is volatile memory?": {
        "subcategory": "Definition recall", "answer": "Volatile memory requires power to retain its stored information. SRAM and DRAM lose their contents when power is removed.",
        "source": "6. Physical Memory.pptx slides 27, 36–37; Copy of CSE 320 Notes.docx P108–113",
    },
    "What is an I/O bus?": {
        "subcategory": "Definition recall", "answer": "An I/O bus is the communication path that connects peripheral controllers and expansion devices to the I/O bridge.",
        "source": "6. Physical Memory.pptx slides 20–21",
    },
    "What is a memory bus?": {
        "subcategory": "Definition recall", "answer": "A memory bus is the communication path between the I/O bridge or memory controller and main memory.",
        "source": "6. Physical Memory.pptx slides 20–21",
    },
    "What is direct memory access (DMA)?": {
        "subcategory": "Definition recall", "answer": "Direct memory access is a mechanism in which specialized hardware transfers data directly between an I/O device and main memory without requiring the CPU to handle each transferred word.",
        "source": "6. Physical Memory.pptx slide 21; Copy of 320 midterm 1 notes.docx P151–165",
    },
    "What is loop unrolling?": {
        "subcategory": "Definition recall", "answer": "Loop unrolling expands a loop body to perform several original iterations during one loop iteration, reducing loop-control overhead and potentially exposing more parallel work.",
        "source": "5. Optimizations and Profiling.pptx slides 52–53; FULL CSE 320 Notes (1).docx P280",
    },
    "What is branch prediction?": {
        "subcategory": "Definition recall", "answer": "Branch prediction is the processor's attempt to predict a conditional branch's outcome before it is resolved so instruction fetching can continue along the predicted path.",
        "source": "5. Optimizations and Profiling.pptx slides 66–69; Copy of 320 midterm 1 notes.docx P82",
    },
    "What is function inlining?": {
        "subcategory": "Definition recall", "answer": "Function inlining substitutes a function's body at a call site, which can eliminate function-call overhead while increasing generated code size.",
        "source": "5. Optimizations and Profiling.pptx slides 14–15, 19–20",
    },
    "What is code motion?": {
        "subcategory": "Definition recall", "answer": "Code motion moves a computation to a location where it executes less often while preserving program behavior, such as moving a loop-invariant calculation before the loop.",
        "source": "5. Optimizations and Profiling.pptx slides 24–25",
    },
    "What is reduction in strength?": {
        "subcategory": "Definition recall", "answer": "Reduction in strength replaces a costly operation with a cheaper equivalent operation, such as replacing repeated multiplication with addition or a constant multiplication with a shift.",
        "source": "5. Optimizations and Profiling.pptx slide 26",
    },
    "What is a superscalar processor?": {
        "subcategory": "Definition recall", "answer": "A superscalar processor can issue and execute multiple instructions during one cycle by exploiting instruction-level parallelism.",
        "source": "5. Optimizations and Profiling.pptx slide 47; Copy of 320 midterm 1 notes.docx P83–84",
    },
    "What is latency?": {
        "subcategory": "Definition recall", "answer": "Latency is the time between starting an operation and having its result available.",
        "source": "5. Optimizations and Profiling.pptx slides 48–49; Copy of CSE 320 Notes.docx P69–70",
    },
    "What is throughput?": {
        "subcategory": "Definition recall", "answer": "Throughput is the amount of work or number of operations completed per unit time when available hardware resources are kept busy.",
        "source": "Copy of CSE 320 Notes.docx P69–70; 6.1 Caches.pptx slide 22",
    },
    "What is spatial locality?": {
        "subcategory": "Definition recall", "answer": "Spatial locality is the tendency to access memory locations near recently accessed locations within a short period of time.",
        "source": "6. Physical Memory.pptx slides 5–7",
    },
    "What is temporal locality?": {
        "subcategory": "Definition recall", "answer": "Temporal locality is the tendency to access the same data or instructions again soon after they were accessed.",
        "source": "6. Physical Memory.pptx slides 5–6",
    },
    "What is a write-back cache policy?": {
        "subcategory": "Definition recall", "answer": "A write-back policy updates the cache on a write and postpones updating lower memory until the modified cache block is evicted, typically tracking the change with a dirty bit.",
        "source": "6.1 Caches.pptx slide 15",
    },
    "What is a write-through cache policy?": {
        "subcategory": "Definition recall", "answer": "A write-through policy updates both the cache and the next lower memory level immediately on a cache write.",
        "source": "6.1 Caches.pptx slide 15",
    },
    "What is symbol resolution?": {
        "subcategory": "Definition recall", "answer": "Symbol resolution is the linker's process of associating each symbol reference with exactly one symbol definition from its input object files.",
        "source": "7. Compiler Toolchains.pptx slides 6–8",
    },
    "What is relocation?": {
        "subcategory": "Definition recall", "answer": "Relocation is the linker's process of assigning final addresses to combined code and data sections and modifying references so they use those addresses.",
        "source": "7. Compiler Toolchains.pptx slides 6, 8, 20",
    },
    "What is position-independent code?": {
        "subcategory": "Definition recall", "answer": "Position-independent code executes correctly regardless of the memory address at which it is loaded, without depending on a fixed starting address.",
        "source": "7. Compiler Toolchains.pptx slide 40",
    },
    "What is a profiler?": {
        "subcategory": "Definition recall", "answer": "A profiler measures a running program's performance behavior, such as time spent in functions, call activity, or memory allocation, to identify hot spots.",
        "source": "5. Optimizations and Profiling.pptx slides 5–6, 12–13",
    },
    "What is a debugger?": {
        "subcategory": "Definition recall", "answer": "A debugger is a tool for observing and controlling a program's execution to investigate its state and locate defects. GDB is the debugger named in the notes.",
        "source": "FULL CSE 320 Notes (1).docx P2, P46, P304",
    },
    "What is a compiler?": {
        "subcategory": "Definition recall", "answer": "A compiler translates preprocessed source code into assembly code. In the course toolchain, it transforms a `.i` file into a `.s` file.",
        "source": "7. Compiler Toolchains.pptx slides 2–3",
    },
    "What is a linker?": {
        "subcategory": "Definition recall", "answer": "A linker combines relocatable object files, resolves symbol references, relocates code and data, and produces an executable or shared object.",
        "source": "7. Compiler Toolchains.pptx slides 2, 6–8",
    },
    "What is an assembler?": {
        "subcategory": "Definition recall", "answer": "An assembler translates assembly-language code into machine code stored in a relocatable object file. In the course toolchain, it transforms a `.s` file into a `.o` file.",
        "source": "7. Compiler Toolchains.pptx slides 2–3",
    },
}

questions["General Concepts"].update({
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
    "Starting with C source, which sequence of toolchain stages produces an executable?": {
        "subcategory": "Concept", "choices": {"A": "Preprocessor → Compiler → Assembler → Linker", "B": "Compiler → Preprocessor → Linker → Assembler", "C": "Assembler → Preprocessor → Compiler → Linker", "D": "Linker → Assembler → Compiler → Preprocessor"},
        "correct_answer": "A", "explanation": "The toolchain preprocesses C source, compiles it into assembly, assembles it into a relocatable object file, and links object files into an executable.",
        "source": "7. Compiler Toolchains.pptx slide 2",
    },
    "A flat profile shows that `parse_input` uses 40% of runtime across 2 calls, while `compare_word` uses 40% across 20 million calls. What does the profile suggest?": {
        "subcategory": "Concept", "choices": {"A": "`parse_input` is expensive per call, while `compare_word` is a hotspot mainly because it is called frequently", "B": "`compare_word` is expensive per call, while `parse_input` is a hotspot mainly because it is called frequently", "C": "The two functions have approximately the same cost per call", "D": "No comparison is possible without a heap-allocation profile"},
        "correct_answer": "A", "explanation": "Both functions consume the same total share of runtime, but `parse_input` does so in only two calls. `compare_word` reaches the same total through millions of calls. The course notes that a hotspot may be individually slow or frequently used.",
        "source": "5. Optimizations and Profiling.pptx slides 5, 12–13",
    },
})

# Audited MT1 review-session questions. These are also distributed into the
# chapter topics below so they can be studied either by chapter or as one review.

questions['MT1_review_session'] = {
    'An int is 4 bytes, cache blocks are 64 bytes, a[0] begins a cache block, and the cache starts empty. Read a[0], then a[8], then a[16], with no intervening evictions. What is the hit/miss sequence? Which elements are loaded by the first read?': {
        'subcategory': 'Address mapping',
        'choices': {'A': 'Miss, hit, miss; first read loads a[0] through a[7]', 'B': 'Miss, miss, miss; first read loads a[0] through a[15]', 'C': 'Miss, hit, miss; first read loads a[0] through a[15]', 'D': 'Miss, hit, hit; first read loads a[0] through a[16]'},
        'correct_answer': 'C',
        'explanation': 'One block holds 16 ints. Reading a[0] misses and loads a[0] through a[15]. a[8] hits; a[16] is in the next block and misses.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp24; midterm_review_transcript.txt',
    },
    'A cache has 8 sets, 4 lines per set, and 32-byte blocks in a system with 32-bit addresses. How many data bytes does it hold?': {
        'subcategory': 'Address-field interpretation',
        'choices': {'A': '512 bytes', 'B': '1024 bytes', 'C': '2048 bytes', 'D': '256 bytes'},
        'correct_answer': 'B',
        'explanation': 'C=S*E*B=8*4*32=1024 data bytes. Address width does not multiply the data capacity.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp26; midterm_review_transcript.txt',
    },
    'Use Cache #1 in the image. For the 6-bit byte address 0x1D, which cache block and byte offset are selected, and is the read a hit?': {
        'subcategory': 'Address mapping',
        'choices': {'A': 'Block 1; hit; offset 3', 'B': 'Block 3; miss; offset 1', 'C': 'Block 3; hit; offset 1', 'D': 'Block 2; hit; offset 1'},
        'correct_answer': 'C',
        'explanation': '0x1D is 011101 in six bits. Splitting as tag/set/offset gives 01/11/01: tag 1, set 3, offset 1. Block number 3 is valid and stores tag 1, so it hits.',
        'source': 'CSE_320_MT1_Review_Session.pdf p32; midterm_review_transcript.txt lines 250-259; 6.1 Caches.pptx slides 8-11',
        'image': 'cse320/Cache Diagram.png',
    },
    'Use Cache #2 in the image. Express 0x35 as a 7-bit byte address. Which block number and byte offset apply if the read hits?': {
        'subcategory': 'Address mapping',
        'choices': {'A': 'Block 2, offset 1', 'B': 'Block 3, offset 1', 'C': 'Block 2, offset 3', 'D': 'Block 1, offset 1'},
        'correct_answer': 'A',
        'explanation': '0x35 is 00110101 in eight bits; the extra leading zero can be dropped to fit the seven-bit address space. The fields are 011/01/01: tag 3, set 1, offset 1. Valid block number 2 has tag 3, so the read hits.',
        'source': 'CSE_320_MT1_Review_Session.pdf p33; midterm_review_transcript.txt lines 262-273; 6.1 Caches.pptx slides 12-14',
        'image': 'cse320/Cache Diagram.png',
    },
    'Consider the complete matrix-multiplication example from the review:\n```c\nfor (i = 0; i < n; i++) {\n    for (j = 0; j < n; j++) {\n        double sum = 0;\n        for (k = 0; k < n; k++) {\n            sum += A[i][k] * B[k][j];\n        }\n        C[i][j] = sum;\n    }\n}\n```\nUse the review\'s cache model: each 64-byte block holds eight doubles, an A[i][k] block remains cached for its eight consecutive accesses, and every B[k][j] access misses. Count only the reads of A and B. What are the approximate misses per inner-loop iteration and the miss rate?': {
        'subcategory': 'Program cache hit/miss',
        'choices': {'A': '9/8 misses; 56.25% miss rate', 'B': '1 miss; 50% miss rate', 'C': '1/8 miss; 6.25% miss rate', 'D': '2 misses; 100% miss rate'},
        'correct_answer': 'A',
        'explanation': 'A[i][k] is sequential, giving one miss per eight doubles (1/8). B[k][j] advances by a row and has one miss per read under the stated model. Total misses per iteration are 1/8+1=9/8. There are two reads, so the miss fraction is (9/8)/2=9/16=56.25%. Misses per iteration and misses per access have different denominators.',
        'source': 'CSE_320_MT1_Review_Session.pdf p37; midterm_review_transcript.txt',
    },
    'L1, L2, and L3 have local hit rates of 90%, 80%, and 50%, and lookup times of 1 ns, 5 ns, and 20 ns. Main memory adds 100 ns after an L3 miss. Each lookup time is paid whenever that level is reached, including on a miss. What is average memory access time from L1?': {
        'subcategory': 'Average access time',
        'choices': {'A': '1.0 ns', 'B': '19.0 ns', 'C': '70.0 ns', 'D': '2.9 ns'},
        'correct_answer': 'D',
        'explanation': 'Local miss rates are 0.10, 0.20, and 0.50. Starting at L3 costs 20+0.50*100=70 ns on average; L2 costs 5+0.20*70=19 ns; L1 costs 1+0.10*19=2.9 ns. Equivalently, 1+0.10*(5+0.20*(20+0.50*100)).',
        'source': 'CSE_320_MT1_Review_Session.pdf pp40-43; midterm_review_transcript.txt lines 370-402; 6.1 Caches.pptx slides 18-20',
    },
    'After this code executes, what are the contents of a?\n```c\nint a[3] = {3, 5, 7};\nint *p = a;\nint *q = p;\np++;\n*q += *p;\n(*p)++;\n```': {
        'subcategory': 'Code concepts',
        'choices': {'A': '{3, 6, 7}', 'B': '{8, 5, 8}', 'C': '{3, 10, 7}', 'D': '{8, 6, 7}'},
        'correct_answer': 'D',
        'explanation': 'Copying p into q copies the address of a[0]. Incrementing p moves only p to a[1]. The write through q adds a[1]=5 to a[0]=3, producing 8. (*p)++ then changes a[1] from 5 to 6.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp47-48; midterm_review_transcript.txt lines 479-506; 5. Optimizations and Profiling.pptx slides 35-36',
    },
    'For the review code int y=10; int x=y*3;, would replacing y*3 with y<<3 be correct, and what values do the two expressions produce?': {
        'subcategory': 'Code concepts',
        'choices': {'A': 'Yes; both produce 30', 'B': 'Yes; both produce 80', 'C': 'No; they produce 30 and 20', 'D': 'No; they produce 30 and 80'},
        'correct_answer': 'D',
        'explanation': 'For this positive representable value, shifting left three multiplies by 2^3=8, so y<<3=80, while y*3=30. This replacement does not preserve the result.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp53; midterm_review_transcript.txt',
    },
    'Assume <stdio.h> is included. Start each version in a fresh execution with calls=0.\n```c\nint calls = 0;\nint next_value(void) { return ++calls; }\nint analyze(int *a, int *out) {\n    *out = 0;\n    for (int i = 0; i < 3; i++)\n        *out += a[i];\n    int extra = 0;\n    for (int j = 0; j < 3; j++)\n        extra += next_value();\n    return *out + extra;\n}\nint main(void) {\n    int a[] = {1, 2, 3};\n    int *p = a;\n    int *q = p + 1;\n    int result = analyze(p, q);\n    printf("%d %d %d\\n", result, a[1], calls);\n}\n```\nReplace only the initialization *out=0 and the first loop with:\n```c\nint total = 0;\nfor (int i = 0; i < 3; i++)\n    total += a[i];\n*out = total;\n```\nWhat does the changed program print, and is this replacement behavior-preserving for the shown call?': {
        'subcategory': 'Code concepts',
        'choices': {'A': '11 5 3; yes', 'B': '12 6 3; yes', 'C': '12 6 3; no', 'D': '8 5 1; no'},
        'correct_answer': 'C',
        'explanation': 'The replacement reads the original {1,2,3}, sums to 6, and only then sets a[1]=6. The unchanged second loop gives extra=6 and calls=3, so result=12. It prints 12 6 3 instead of 11 5 3. Delayed writes change later reads when out aliases the input.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp57-58, 67; midterm_review_transcript.txt lines 608-620; 5. Optimizations and Profiling.pptx slides 35-36',
    },
    'Assume <stdio.h> is included. Start each version in a fresh execution with calls=0.\n```c\nint calls = 0;\nint next_value(void) { return ++calls; }\nint analyze(int *a, int *out) {\n    *out = 0;\n    for (int i = 0; i < 3; i++)\n        *out += a[i];\n    int extra = 0;\n    for (int j = 0; j < 3; j++)\n        extra += next_value();\n    return *out + extra;\n}\nint main(void) {\n    int a[] = {1, 2, 3};\n    int *p = a;\n    int *q = p + 1;\n    int result = analyze(p, q);\n    printf("%d %d %d\\n", result, a[1], calls);\n}\n```\nKeep the original first loop. Replace only the extra initialization and second loop with:\n```c\nint extra = 0;\nint value = next_value();\nfor (int j = 0; j < 3; j++)\n    extra += value;\n```\nWhat does the changed program print, and is this replacement behavior-preserving?': {
        'subcategory': 'Code concepts',
        'choices': {'A': '8 5 1; no', 'B': '11 5 3; yes', 'C': '12 6 3; no', 'D': '8 5 3; yes'},
        'correct_answer': 'A',
        'explanation': 'The original first loop still leaves *out=a[1]=5. The hoisted call executes once, returns 1, and leaves calls=1. Adding that value three times gives extra=3, result=8. The output is 8 5 1. Both the return-value sequence and the global side effect differ from the original.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp57, 59; midterm_review_transcript.txt lines 621-639; 5. Optimizations and Profiling.pptx slides 23, 28-34',
    },
    'What is the difference between p, *p, and &p when p is a pointer?': {
        'subcategory': 'Concept',
        'answer': 'p is the address stored in the pointer, *p accesses the object at that address, and &p is the address of the pointer variable itself. For example, after int x = 5; int *p = &x;, p holds the address of x, *p is 5, and &p is the address where the pointer p is stored.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp61; midterm_review_transcript.txt',
    },
    'Does incrementing a pointer with p++ always move it forward by one byte?': {
        'subcategory': 'Concept',
        'choices': {'A': 'Yes; int* and char* both advance by one byte', 'B': 'Yes; all pointer types use one-byte steps regardless of type', 'C': 'No; if int is four bytes, an int* advances four bytes', 'D': 'No; every pointer advances by its own storage size'},
        'correct_answer': 'C',
        'explanation': 'p++ moves p to the next element of its pointed-to type, so the address changes by sizeof(*p). For example, if p is an int* holding address 1000 and an int is four bytes, p++ changes the address to 1004. A char* at address 1000 would advance to 1001 because sizeof(char) is one byte.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp62; midterm_review_transcript.txt',
    },
    'When a function receives a pointer argument, can it modify the caller data? Can assigning a new address to that parameter change the caller pointer?': {
        'subcategory': 'Concept',
        'choices': {'A': 'Caller data: no; caller pointer: yes', 'B': 'Caller data: yes; caller pointer: yes', 'C': 'Caller data: yes; caller pointer: no', 'D': 'Caller data: no; caller pointer: no'},
        'correct_answer': 'C',
        'explanation': 'The function receives a copy of the pointer value. To change the caller pointer itself it needs access to that variable, commonly via a pointer to a pointer.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp63; midterm_review_transcript.txt',
    },
    'Does a pointer being non-NULL guarantee that it is safe to dereference?': {
        'subcategory': 'Concept',
        'choices': {'A': 'Yes; non-NULL always identifies a live object', 'B': 'Yes; non-NULL guarantees the address is readable', 'C': 'No; only pointers returned by malloc are safe to dereference', 'D': 'No; it may be dangling or outside a valid object'},
        'correct_answer': 'D',
        'explanation': 'Non-NULL is insufficient. Dangling, out-of-bounds, or improperly initialized pointers may not be valid to dereference; free does not clear all aliases.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp64; midterm_review_transcript.txt',
    },
    'Does copying one pointer into another create a separate copy of the pointed-to data?': {
        'subcategory': 'Concept',
        'choices': {'A': 'No; it copies the address, so both pointers can refer to the same data', 'B': 'Yes; it duplicates the pointed-to object at a new address', 'C': 'No; the second pointer remains NULL until data is assigned to it', 'D': 'Yes; every pointer assignment performs a complete data copy'},
        'correct_answer': 'A',
        'explanation': 'A copied pointer can refer to the same object, so changes through either pointer can be observed through the other.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp65; midterm_review_transcript.txt',
    },
    'Why can replacing repeated writes through an output pointer with a local accumulator change a program result?': {
        'subcategory': 'Concept',
        'choices': {'A': 'Local variables always have uninitialized values', 'B': 'Local accumulators always change mathematical addition', 'C': 'The output may alias input; delaying writes changes values read by later iterations', 'D': 'Because pointer values cannot be copied'},
        'correct_answer': 'C',
        'explanation': 'An output pointer into the input array lets an early write alter a later input read. Delayed final stores can therefore change the result.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp67; midterm_review_transcript.txt',
    },
    'If an input pointer is declared const int *a, can the compiler assume that the values in the array never change?': {
        'subcategory': 'Concept',
        'choices': {'A': 'Yes; const makes the underlying array immutable everywhere', 'B': 'Yes; const guarantees that no writable alias can exist', 'C': 'No; const blocks writes through a, not through other aliases', 'D': 'No; const affects pointer reassignment, not access through a'},
        'correct_answer': 'C',
        'explanation': 'The declaration restricts writes through a, not through every other pointer. It does not establish separate storage or global immutability.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp68; midterm_review_transcript.txt',
    },
    'What is the difference between spatial locality and temporal locality?': {
        'subcategory': 'Concept',
        'choices': {'A': 'Spatial accesses nearby locations; temporal reuses the same recently accessed location', 'B': 'Spatial reuses one address; temporal means addresses are neighbors', 'C': 'Both mean all data fits in cache', 'D': 'Neither relates to memory addresses'},
        'correct_answer': 'A',
        'explanation': 'Caches exploit spatial locality by loading whole blocks and temporal locality by retaining recently used blocks.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp69; midterm_review_transcript.txt',
    },
    'Why does sequential array traversal usually have better spatial locality than linked-list traversal? Does using an array automatically guarantee good locality?': {
        'subcategory': 'Concept',
        'choices': {'A': 'Linked-list nodes are contiguous, while array elements usually are not', 'B': 'Array elements are contiguous, but large strides can still waste blocks', 'C': 'Arrays always have good locality, regardless of their access order', 'D': 'Arrays use fewer instructions, which guarantees that accesses hit'},
        'correct_answer': 'B',
        'explanation': 'A block can provide several consecutive array elements; list nodes may be scattered. An array can still skip most loaded bytes with a large stride.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp70; midterm_review_transcript.txt',
    },
    'For a C two-dimensional array, why is it usually better for the innermost loop to change the second index? Does the loop variable name matter?': {
        'subcategory': 'Concept',
        'choices': {'A': 'It follows columns; the variable name matters', 'B': 'It follows columns; the variable name does not matter', 'C': 'It follows rows; the variable name does not matter', 'D': 'It follows rows; the variable name matters'},
        'correct_answer': 'C',
        'explanation': 'C stores two-dimensional arrays in row-major order, so elements that differ only in the second index are adjacent in memory. Changing that index in the innermost loop therefore traverses a row sequentially and usually improves spatial locality. The identifier itself is irrelevant: i, j, k, or any other name behaves the same if it changes the second index.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp71; midterm_review_transcript.txt',
    },
    'What is cache blocking, and why can it improve performance even when a program performs the same calculations?': {
        'subcategory': 'Concept',
        'choices': {'A': 'It removes arithmetic by skipping iterations that access memory', 'B': 'It stores whole matrices in registers before computation begins', 'C': 'It changes results so fewer values need to be processed', 'D': 'It processes cache-sized regions and reuses data before eviction'},
        'correct_answer': 'D',
        'explanation': 'Blocking clusters reuse and adjacent accesses, improving temporal and spatial locality without needing fewer mathematical operations. Tiles too large for cache can lose the benefit.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp72; midterm_review_transcript.txt',
    },
    'Is an unchanged result enough to make moving a calculation outside a loop safe?': {
        'subcategory': 'Concept',
        'choices': {'A': 'No; moving it can change observable program behavior', 'B': 'Yes; an unchanged value guarantees equivalent program behavior', 'C': 'Yes; loop-invariant calculations are always safe to move', 'D': 'No; calculations must always remain inside their original loops'},
        'correct_answer': 'A',
        'explanation': 'The moved calculation may run when the original would not, or change effects and call counts. Safe motion preserves complete required behavior.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp73; midterm_review_transcript.txt',
    },
    'Function A performs one addition and is called millions of times inside a loop. Function B performs a lengthy calculation and is called once. Which is generally the stronger candidate for inlining and why?': {
        'subcategory': 'Concept',
        'choices': {'A': 'B, because inlining removes the lengthy calculation it performs', 'B': 'A, because repeated call overhead is large relative to its tiny body', 'C': 'Both, because inlining always saves the same execution time', 'D': 'Neither, because functions called inside loops cannot be inlined'},
        'correct_answer': 'B',
        'explanation': 'A pays call overhead millions of times; B pays it once and is dominated by its computation. Inlining can also expose work to nearby optimizations.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp74; midterm_review_transcript.txt',
    },
    'If a function return value is unused, can the compiler automatically remove the function call?': {
        'subcategory': 'Concept',
        'choices': {'A': 'Yes, whenever its return value is ignored', 'B': 'Yes, unless it changes a global variable', 'C': 'No; the call may have observable side effects', 'D': 'No; function calls can never be removed'},
        'correct_answer': 'C',
        'explanation': 'An unused result does not prove absence of effects. Removing the call requires proof that required behavior is preserved.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp75; midterm_review_transcript.txt',
    },
    'Does loop unrolling always make a program faster? What limitations can remain after a loop is unrolled?': {
        'subcategory': 'Concept',
        'choices': {'A': 'Yes; dependencies vanish and code size always decreases', 'B': 'Yes; register pressure falls and remainder handling disappears', 'C': 'No; only cache misses can limit the resulting speedup', 'D': 'No; dependencies, code growth, register pressure, and remainders may remain'},
        'correct_answer': 'D',
        'explanation': 'Unrolling processes more work per loop iteration, reducing branch, comparison, and index-update overhead. It does not remove dependencies within the loop body, so operations may still execute serially. It can also increase code size and register pressure, and a cleanup loop may be needed when the iteration count is not divisible by the unroll factor. These costs can outweigh the saved loop overhead.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp76; midterm_review_transcript.txt',
    },
    'A programmer supplies a condition to check for programming errors. When the enabled check fails, the program reports the failure and typically terminates. Which term describes this?': {
        'subcategory': 'Definition identification',
        'choices': {'A': 'Interrupt', 'B': 'Profiler', 'C': 'Assertion', 'D': 'Branch Prediction'},
        'correct_answer': 'C',
        'explanation': 'An assertion checks a programmer-specified condition that is expected to hold. A failed enabled assertion typically reports the failure and terminates. This is now directly defined by the new review material.',
        'source': 'CSE_320_MT1_Review_Session.pdf p11; midterm_review_transcript.txt lines 41-43; CSE 320 Notes.docx P28',
    },
    'A cache keeps 2 lines per set and 32-byte blocks, but increases from 8 sets to 16 sets. Which structural change and likely performance tradeoff follow?': {
        'subcategory': 'Design tradeoff',
        'choices': {'A': 'Capacity doubles; misses may fall, but area and power may rise', 'B': 'Capacity stays fixed; misses may fall without additional hardware cost', 'C': 'Block size doubles; transfers grow, but area and power stay fixed', 'D': 'Associativity doubles; conflicts fall, but each lookup checks more lines'},
        'correct_answer': 'A',
        'explanation': 'C=S*E*B changes from 8*2*32=512 to 16*2*32=1024 data bytes. The set index grows from 3 to 4 bits, while the offset stays at 5. More capacity can reduce misses at an area/power cost; improvement depends on the workload.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp25-30; midterm_review_transcript.txt lines 213-225; 6.1 Caches.pptx slide 7',
    },
    'Which HDD component is a rotating disk with two magnetic recording surfaces?': {
        'subcategory': 'HDD component',
        'choices': {'A': 'Cylinder', 'B': 'Sector', 'C': 'Read/write head', 'D': 'Platter'},
        'correct_answer': 'D',
        'explanation': 'A platter is the rotating disk. Its two surfaces contain tracks, and each track is divided into sectors. A cylinder groups same-radius tracks across surfaces.',
        'source': '6. Physical Memory.pptx slides 10-12; Copy of CSE 320 Notes.docx P125-131',
    },
    'What is an HDD sector?': {
        'subcategory': 'HDD component',
        'answer': 'An HDD sector is a smaller storage region within a circular track. Tracks are divided into sectors separated by gaps, and each sector stores a fixed-size block of data.',
        'source': '6. Physical Memory.pptx slide 11; Copy of CSE 320 Notes.docx P128-131',
    },
    'What is an HDD cylinder component?': {
        'subcategory': 'HDD component',
        'answer': 'An HDD cylinder is the collection of aligned, same-radius tracks across all recording surfaces. Moving the heads radially changes cylinders; selecting another surface at the same radius does not.',
        'source': '6. Physical Memory.pptx slides 12-13; Copy of CSE 320 Notes.docx P131',
    },
    'Which order follows the review session memory hierarchy from fastest access to slowest access?': {
        'subcategory': 'Memory hierarchy',
        'choices': {'A': 'Registers, L3, L2, L1, DRAM, SSD, HDD', 'B': 'Registers, L1, L2, L3, SSD, DRAM, HDD', 'C': 'Registers, L1, L2, L3, DRAM, SSD, HDD', 'D': 'Registers, L1, L3, L2, DRAM, SSD, HDD'},
        'correct_answer': 'C',
        'explanation': 'The review orders registers, L1 cache, L2 cache, L3 cache, main memory (DRAM), SSD, then HDD. Moving downward generally increases capacity and latency and lowers cost per byte.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp78-79; 6. Physical Memory.pptx slides 2-4, 38-40',
    },
    'Which pairing and characteristics match the review: typical cache memory versus typical main memory?': {
        'subcategory': 'Memory hierarchy',
        'choices': {'A': 'Cache uses DRAM; main memory uses faster SRAM without refreshing', 'B': 'Cache uses SRAM; main memory uses nonvolatile flash without refreshing', 'C': 'Cache uses SRAM; main memory uses denser DRAM requiring refreshing', 'D': 'Cache uses flash; main memory uses faster SRAM requiring refreshing'},
        'correct_answer': 'C',
        'explanation': 'Caches typically use fast relatively expensive SRAM; main memory uses denser cheaper DRAM, which requires periodic refresh. Both are volatile.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp78; midterm_review_transcript.txt',
    },
}

# Additional questions retained after the individual supplemental audit.
questions['MT1_review_session'].update({
    'Assume even n, valid array bounds, and integer sums that do not overflow. Compare these unrolled loops:\n```c\n/* P */\nfor (int i=0; i<n; i+=2) {\n    total += a[i];\n    total += a[i+1];\n}\n/* Q */\nfor (int i=0; i<n; i+=2) {\n    total0 += a[i];\n    total1 += a[i+1];\n}\n```\nThe accumulators start at zero and Q combines total0+total1 afterward. Why can Q expose more parallel work?': {
        'subcategory': 'Code concepts',
        'choices': {'A': 'Q reads fewer array elements per loop iteration', 'B': 'Q guarantees that every array access hits the cache', 'C': 'Q removes loop-control work that remains in P', 'D': 'Q uses two independent accumulator chains'},
        'correct_answer': 'D',
        'explanation': 'In P, each addition needs the preceding total. In Q, updating total0 does not require the result of updating total1, permitting independent work. Both read n elements and reduce loop-control overhead; a speedup still depends on the processor and workload.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp55-56, 76; midterm_review_transcript.txt lines 575-598, 805-819; 5. Optimizations and Profiling.pptx (loop unrolling examples)',
    },
    'A block is accessed for the first time and is absent from the cache. Which cache-miss category applies?': {
        'subcategory': 'Miss types',
        'choices': {'A': 'Compulsory/cold', 'B': 'Conflict', 'C': 'Capacity', 'D': 'Write-through'},
        'correct_answer': 'A',
        'explanation': 'This is a compulsory miss, also called a cold miss, because the block has never been brought into the cache before. It occurs on the first access regardless of the cache\'s capacity or associativity. Conflict and capacity misses instead describe blocks that were previously loaded but later displaced.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp27; midterm_review_transcript.txt',
    },
    'The working set cannot fit in the cache even without set-placement restrictions. Which cache-miss category applies?': {
        'subcategory': 'Miss types',
        'choices': {'A': 'Compulsory/cold', 'B': 'Conflict', 'C': 'Capacity', 'D': 'Write-back'},
        'correct_answer': 'C',
        'explanation': 'Insufficient total cache capacity causes capacity misses.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp27; midterm_review_transcript.txt',
    },
    'Why can regrouping floating-point additions prevent a compiler optimization from preserving the required result, even when the expressions are algebraically equivalent?': {
        'subcategory': 'Code concepts',
        'choices': {'A': 'Intermediate rounding can change the final value', 'B': 'Floating-point addition is always exactly associative', 'C': 'Regrouping changes the program\'s cache block size', 'D': 'Faster transformations may ignore numerical differences'},
        'correct_answer': 'A',
        'explanation': 'Finite-precision floating-point operations round intermediate results. A different grouping can therefore produce a different final value. Under requirements that preserve these results, algebraic equivalence alone does not justify reassociation.',
        'source': 'CSE_320_MT1_Review_Session.pdf p46; midterm_review_transcript.txt lines 462-466',
    },
    'Consider this function from the review:\n```c\nint f(void) {\n    int x;      // line 1\n    x = 3;      // line 2\n    x = 5;      // line 3\n    return x;   // line 4\n}\n```\nWhich change safely optimizes the function without changing its return value?': {
        'subcategory': 'Code concepts',
        'choices': {'A': 'Delete line 2; its stored value is overwritten before use', 'B': 'Delete line 3; its stored value is overwritten before use', 'C': 'Delete line 4; returning a local value has no visible effect', 'D': 'Swap lines 2 and 3; assignment order cannot affect the return'},
        'correct_answer': 'A',
        'explanation': 'Line 2 stores 3 in x, but line 3 overwrites x with 5 before any read occurs. The value 3 is therefore a dead store, so deleting line 2 preserves the return value of 5. Deleting line 3 or changing the assignment order would change the result, and deleting line 4 would remove the required return value.',
        'source': 'CSE_320_MT1_Review_Session.pdf pp54; midterm_review_transcript.txt',
    },
})

# Place every audited review question in its appropriate chapter while keeping
# MT1_review_session as a complete review-specific copy.
_CACHE_CONCEPT_QUESTIONS = {
    'What is the difference between spatial locality and temporal locality?',
    'Why does sequential array traversal usually have better spatial locality than linked-list traversal? Does using an array automatically guarantee good locality?',
    'For a C two-dimensional array, why is it usually better for the innermost loop to change the second index? Does the loop variable name matter?',
    'What is cache blocking, and why can it improve performance even when a program performs the same calculations?',
}

_BASIC_CODE_CONCEPT_QUESTIONS = {
    'What is the difference between p, *p, and &p when p is a pointer?',
    'Does incrementing a pointer with p++ always move it forward by one byte?',
    'When a function receives a pointer argument, can it modify the caller data? Can assigning a new address to that parameter change the caller pointer?',
    'Does a pointer being non-NULL guarantee that it is safe to dereference?',
    'Does copying one pointer into another create a separate copy of the pointed-to data?',
    'Why can replacing repeated writes through an output pointer with a local accumulator change a program result?',
    'If an input pointer is declared const int *a, can the compiler assume that the values in the array never change?',
}

_CACHE_SUBCATEGORIES = {
    'Address mapping',
    'Address-field interpretation',
    'Program cache hit/miss',
    'Average access time',
    'Design tradeoff',
    'Miss types',
}

for _question, _record in questions['MT1_review_session'].items():
    _subcategory = _record['subcategory']
    if _subcategory in _CACHE_SUBCATEGORIES or _question in _CACHE_CONCEPT_QUESTIONS:
        _destination = 'Cache'
    elif _subcategory in {'HDD component', 'Memory hierarchy'}:
        _destination = 'Physical Memory'
    elif _subcategory == 'Code concepts' or _question in _BASIC_CODE_CONCEPT_QUESTIONS:
        _destination = 'Basic Code'
    else:
        _destination = 'General Concepts'
    questions[_destination][_question] = _record

del _question, _record, _subcategory, _destination
del _CACHE_CONCEPT_QUESTIONS, _BASIC_CODE_CONCEPT_QUESTIONS, _CACHE_SUBCATEGORIES

from question_banks._mp3_stub_questions import build_questions

questions['HW1 · MP3'] = build_questions()

questions['HW2 · CACHE'] = {
    'Why can a row-wise transpose cause many cache misses, and how do tiling and read/write order reduce conflicts?': {
        'subcategory': 'Transpose locality',
        'answer': 'Reading across a row of A is contiguous, but writing the corresponding values to B jumps between rows and can displace useful cache lines. Tiling works on a small region while its lines remain useful; delaying conflicting writes lets source values be read before their lines are evicted.',
        'explanation': 'The blocked implementation delays diagonal stores in square tiles, where A and B can compete for the same set.',
        'sources': ['cse320/CACHE_HW_ORIGINAL/README.md (Part B Hints)', 'cse320/CACHE_HW_NEW/src/trans.c'],
    },
    'Why might transpose_submit() use different strategies for different matrix shapes and cache configurations?': {
        'subcategory': 'Transpose strategy',
        'answer': 'Matrix dimensions change access patterns, while the three graded cache configurations have different numbers of sets and ways. That changes which A and B lines compete, so one tile shape or access order need not give the fewest misses in every case.',
        'explanation': 'The implementation selects a strategy using matrix dimensions and trans_cache_profile.',
        'sources': ['cse320/CACHE_HW_ORIGINAL/README.md (Cache Configurations; Part B Hints)', 'cse320/CACHE_HW_NEW/src/trans.c'],
    },
}
