import json
from pathlib import Path
D=json.load(open('tmp/mt2_slides.json',encoding='utf-8')); entries=[]
def add(d,s,i,caption,code=None,lang='c'):
 t=D[d]['slides'][s-1]['shapes'][i] if code is None else code
 entries.append((d,s,caption,t.strip(),lang))
# Direct extractions retain the actual slide text and deliberately faulty examples.
for s,i,c in [
(13,1,'A minimal shell: fork a child, execute a command in that child, and wait in the parent. If exec fails, the child exits with failure.'),
(20,2,'Separate address spaces after fork: the child increments its copy of x to 2; the parent decrements its copy to 0. Scheduling determines which print runs first.'),
(21,2,'Both processes execute the second fork. Trace the process graph: L0 is reached once, L1 twice, and Bye four times, assuming successful forks and the lecture’s simple output model.'),
(22,1,'fork4: only the parent follows each nonzero fork branch. Build the process graph and compare it with fork5; three processes eventually reach Bye.'),
(22,2,'fork5: only the child follows each zero fork branch. It produces a different ancestry graph from fork4, although both have three processes reaching Bye.'),
(24,1,'A child can keep running after its parent exits. The infinite loop illustrates an orphaned running process.'),
(24,2,'Terminal demonstration of the surviving child: ps lists it, and kill terminates it. The PID values are specific to this demonstration.'),
(25,2,'wait synchronizes the parent with child termination: CT is printed after the child exits. The child exits before reaching the final Bye.'),
(26,2,'Create N children, reap them in completion order, and decode normal termination using WIFEXITED and WEXITSTATUS.'),
(28,1,'Repeated shell example from slide 13, revisited after execve: fork creates a process; exec replaces the child program; waitpid synchronizes the parent.')]:add(0,s,i,c,lang='text' if (s,i)==(24,2) else 'c')
for s,code,c in [
(12,'int fork(void)','Slide signature: fork returns differently in the parent and child. This is the slide’s simplified declaration.'),
(15,'pid_t getpid(void)\npid_t getppid(void)','Obtain the current process ID and parent process ID.'),
(18,'void exit(int status)','Terminate the process with an exit status; exit does not return.'),
(25,'int wait(int *child_status)','Slide signature: wait returns a terminated child’s PID and stores encoded status. The slide uses int for the return type.'),
(26,'pid_t waitpid(pid_t pid, int &status, int options)','Slide signature for selecting a child to wait for. The slide prints int &status; treat this as slide notation rather than a valid C declaration.'),
(27,'int execve(char *filename, char *argv[], char *envp[])','Load another program into the current process, retaining its PID. Successful execve does not return.')]:add(0,s,0,c,code)
for s,i,c in [
(10,1,'Install a SIGINT handler and wait with pause. This introductory example intentionally predates the safety rules: its printf, fflush, and exit calls should not be copied into a safe signal handler.'),
(12,2,'Construct a signal set, block SIGINT during a region, and restore the previous mask rather than blindly unblocking every signal.'),
(15,2,'Incorrect reaping: standard signals can coalesce, so one wait per handler call can leave children unreaped and the parent spinning. The plain int counter also precedes the slide’s safer flag guidance.'),
(16,2,'Reap multiple children per notification and preserve errno. As printed, wait can block; the slide mentions WNOHANG but does not use it in this code.'),
(17,2,'Implement the course Signal wrapper with sigaction and SA_RESTART. It returns the previous handler and arranges more consistent handling semantics.'),
(18,1,'Race example: the child can exit and be deleted by the handler before the parent adds its PID to the job list. Blocking only after fork is too late.'),
(19,1,'The shell’s SIGCHLD handler reaps children and protects job-list deletion with a signal mask. The printed waitpid uses options 0, so it can block.'),
(20,1,'Fix the job-list race by blocking SIGCHLD before fork, adding the job before restoring the parent’s mask, and restoring the inherited mask in the child before exec.'),
(21,1,'Communicate child termination through a volatile sig_atomic_t variable while preserving errno. The empty SIGINT handler permits interruption without the default termination action.'),
(22,1,'Wait for the handler to update pid using a busy loop. Blocking SIGCHLD while clearing pid prevents a lost update, but spinning wastes CPU.'),
(23,1,'Incorrect replacement for spinning: SIGCHLD can arrive after the condition is tested but before pause, leaving the process waiting for another signal.'),
(23,3,'Polling with sleep avoids continuous spinning but introduces up to a polling interval of delay.'),
(24,1,'The slide’s conceptual mask/wait/restore sequence introduces sigsuspend. Preserve this as printed; separate calls are not atomic, and this sequence is not a drop-in implementation of sigsuspend.'),
(25,1,'Avoid the test/pause race with sigsuspend: keep SIGCHLD blocked while testing pid, temporarily restore prev while waiting, and recheck after wakeup.'),
(28,1,'Nested functions use longjmp to report different errors to the active setjmp recovery point. These functions belong with the globals and main on this same slide.'),
(28,2,'setjmp initially returns zero; a longjmp makes it return an error code handled by switch. With the shown error flags, bar reports error2.'),
(30,2,'Save a signal-aware recovery point. Ctrl-C jumps back and prints restarting, then resumes the processing loop; sigsetjmp’s second argument requests saving the signal mask.')]:add(1,s,i,c)
for s,code,c,lang in [
(2,'Run an infinite loop\nRead user input\nFork a new process\nexecvp the user input in the child process\nWait for the child to end (or don’t)','Shell pseudocode: distinguish foreground waiting from background execution.','text'),
(6,'getpgrp()\nsetpgid()','Process-group APIs connect job control with group-directed signals.','c'),
(7,'/bin/kill –9 24818\n/bin/kill –9 -24818','First command targets one PID; second targets a process group. The slide uses an en dash before 9; replace it with an ASCII hyphen when typing a command.','text'),
(8,'pnb = pending & ~blocked\nIf pnb == 0\n    return to process\nElse\n    Choose least non-zero bit in pnb and send that signal\n    If the process ignores the signal send next signal','Signal-delivery pseudocode: consider pending signals whose types are not blocked. The assignment formats the expression shown in the slide prose.','text'),
(9,'handler_t *signal(int signum, handler_t *handler)','Install a handler, ignore a signal with SIG_IGN, or restore its default action with SIG_DFL.','c'),
(24,'int sigsuspend(const sigset_t *mask)','Temporarily replace the signal mask and suspend atomically; the previous mask is restored when the call returns after a handler.','c'),
(26,'int setjmp(jmp_buf j)','Record a recovery environment; it must remain active for a later longjmp.','c'),
(27,'void longjmp(jmp_buf j, int i)','Restore the recorded environment and resume at setjmp with a nonzero return value.','c')]:add(1,s,0,c,code,lang)
for s,i,c in [(57,1,'Driver for copying a named file to standard output: validate arguments, open the file, obtain its size, and call mmapcopy.'),(57,2,'Map the input file read-only and privately, then write the mapped bytes to standard output. File contents are accessed through the mapping rather than an explicit read into a separate buffer.')]:add(2,s,i,c)
for s,code,c in [(55,'void *mmap(void *start, int len,\n           int prot, int flags, int fd, int offset)','Slide signature for mapping a file region, with protection and sharing flags. This simplified teaching declaration is preserved as printed.'),(56,'void *mmap(void *start, int len,int prot, int flags, int fd, int offset)','Repeated mmap signature alongside the mapping diagram: connect the requested address, length, and file offset to the mapped region.')]:add(2,s,0,c,code)
for s,i,c in [
(5,1,'Allocate n integers, check the allocation, initialize each element, and free the block when finished.'),
(19,2,'Split a free block: round the requested length to an even value, mask the allocation bit from the old size, mark the first part allocated, and write the remaining free-block header. ptr and the size units are teaching abstractions.'),
(21,2,'Clear the allocation bit and merge with a free successor. The source packs code and // comments onto one line; the readable version below restores line breaks only. next and ptr are undeclared teaching abstractions.'),
(42,2,'An allocated block becomes unreachable when the only local pointer goes out of scope. This illustrates garbage; ordinary C malloc does not reclaim it automatically.'),
(48,1,'Mark phase: traverse reachable objects depth first, skipping non-pointers and already marked blocks. This is pseudocode, including its ptr return type with bare returns.'),
(48,4,'Sweep phase: walk the heap, clear survivor marks, and free allocated unmarked blocks. Preserve the slide’s incomplete pseudocode, including missing syntax and the unspecified clearMarkBit argument.'),
(51,1,'Read pointer declarations using parentheses and operator binding. The declarations are printed without semicolons; the explanations below come from the same slide.'),
(53,2,'Bug: scanf expects the address of the destination integer; passing val supplies a value instead. The intended call uses &val. Curly quotes are preserved from the slide.'),
(53,3,'Bug: unbounded gets can overflow s[8] when given the nine shown characters plus a terminator.'),
(54,2,'Bug: malloc leaves y uninitialized, yet += reads its old elements. Initialize the accumulators before summing, or use zero-initialized storage.'),
(55,2,'Bug: p is an array of pointers, but the outer allocation uses sizeof(int). Allocate space for pointer elements, for example N * sizeof *p.'),
(55,3,'Bug: i <= N writes the nonexistent element p[N]. The valid indices for N elements end at N-1.'),
(55,4,'Bug: pointer arithmetic already scales by the pointed-to type. Adding sizeof(int) skips that many integers; increment by one to visit adjacent elements.'),
(56,2,'Bug: *size-- decrements the pointer size because postfix -- binds first. Use (*size)-- to decrement the integer it points to.'),
(57,2,'Bug: returning &val exposes a local variable whose lifetime ends on return. The result is a dangling pointer.'),
(58,2,'Bug: x is freed twice while y is allocated separately. Each allocation needs the correct ownership and matching release.'),
(58,3,'Bug: the loop reads and modifies x after free. A later allocation can reuse the same storage, making this especially misleading.'),
(58,4,'Bug: returning discards the only pointer to the allocation without freeing it, causing a memory leak.'),
(59,2,'Bug: freeing head alone does not release the rest of a linked list. Traverse and free each node while retaining the next pointer.')]:add(3,s,i,c)
add(3,4,0,'Header and slide signatures for explicit allocation and release. calloc, realloc, and sbrk are also introduced in the accompanying prose.','#include <stdlib.h>\nvoid *malloc(size_t size)\nvoid free(void *p)')
add(3,20,0,'Clear the allocated bit without coalescing. Adjacent free blocks remain separate and can cause false fragmentation. The missing semicolon is present in the source.','void free_block(ptr p) { *p = *p & -2 }')
# Restore only line breaks in a text box flattened by the source author.
for j,e in enumerate(entries):
 if e[0:2]==(3,21):
  entries[j]=(e[0],e[1],e[2],'void free_block(ptr p) {\n    *p = *p & -2;          // clear allocated flag\n    next = p + *p;         // find next block\n    if ((*next & 1) == 0)\n      *p = *p + *next;     // add to this block if\n}                          //    not allocated',e[4])
add(3,47,0,'Collector interface pseudocode: application operations create and access blocks; collector operations identify pointers, inspect lengths, and enumerate roots. The header is addressed as b[-1].','new(n)\nread(b,i)\nwrite(b,i,v)\nb[-1]\nis_ptr(p)\nlength(b)\nget_roots()', 'text')
add(3,60,0,'The slide’s shell command enables the allocator checking mode discussed with memory-debugging tools. It is shown in setenv shell syntax.','setenv MALLOC_CHECK_ 3','sh')
for s,code,c in [
(7,'p1 = malloc(4)\np2 = malloc(5)\np3 = malloc(6)\nfree(p2)\np4 = malloc(2)','Allocation sequence embedded in the diagram: a smaller request reuses part of the freed region. Sizes follow the lecture’s word-addressed model.'),
(11,'p1 = malloc(4)\np2 = malloc(5)\np3 = malloc(6)\nfree(p2)\np4 = malloc(6)','Diagram sequence demonstrating external fragmentation: available total space does not guarantee one sufficiently large free block.'),
(14,'p0 = malloc(4)\nfree(p0)','Diagram labels show how a preceding header lets free recover a block’s size from its payload pointer.'),
(19,'addblock(p, 4)','Diagram call demonstrating the split performed by addblock; compare the before and after block layouts.'),
(20,'free(p)\nmalloc(5)','Diagram sequence illustrating false fragmentation when freeing does not merge adjacent free blocks.'),
(21,'free(p)','Diagram call showing forward coalescing: merge a newly freed block with its free successor.')]:add(3,s,0,c,code)
entries.sort(key=lambda e:(e[0],e[1]))
out=['# Midterm 2 — code examples from the slides','',
'All 178 slides reviewed: Processes (29), Signals (31), Virtual Memory (58), and Heap (60). Sources are the four PowerPoint decks in `cse320/midterm-2`. Slide numbers are 1-based positions in each deck. Textbooks, notes, homework, and review transcripts are outside this slide-only collection.','',
'Includes program blocks, short API declarations, shell commands, pseudocode, and code labels inside allocation diagrams. Repeated examples are retained with their own slide references. Captions explain the intended lesson; source errors and intentionally buggy examples remain visible. Text is extracted directly from PowerPoint text runs, with whitespace cleanup; diagram labels are transcribed. No programs were executed.','',
'Course helpers such as `Fork`, `Signal`, `Waitpid`, `Mmap`, and `Write` are wrappers, not standard C function names. `Sio_*` denotes course signal-safe I/O helpers. Many snippets omit headers, helper definitions, or surrounding context and are not standalone programs.','',
'## Contents','']
for d in range(4):out.append(f'- {D[d]["deck"]}: {sum(e[0]==d for e in entries)} entries')
last=None
for n,(d,s,c,code,lang) in enumerate(entries,1):
 if d!=last:out+=['',f'## {D[d]["deck"]}',''];last=d
 title=D[d]['slides'][s-1]['shapes'][0].strip()
 out += [f'### {n}. Slide {s} — {title}', '',f'**Source:** `{D[d]["deck"]}`, slide {s}.','',f'**What it teaches:** {c}','','```'+lang,code,'```','']
 if d==3 and s==51:
  out+=['**Slide explanations:**','']+['- '+t.replace('\n',' ') for t in D[d]['slides'][s-1]['shapes'][2:]]+['']
out += ['## Coverage check','', '| Deck | Slides reviewed | Slides containing collected material |','| --- | ---: | --- |']
for d in range(4):out.append(f'| {D[d]["deck"]} | {len(D[d]["slides"])} | '+', '.join(str(s) for s in sorted({e[1] for e in entries if e[0]==d}))+' |')
out+=['','Other slides contain explanatory prose, formulas, tables, diagrams, or process graphs rather than additional code blocks. Diagram allocation labels are included above; graph output labels and mathematical address-translation formulas are not treated as program blocks.','']
p=Path('midterm-2-code-examples.md');p.write_text('\n'.join(out),encoding='utf-8');print(f'Wrote {len(entries)} entries to {p}, {p.stat().st_size} bytes')
