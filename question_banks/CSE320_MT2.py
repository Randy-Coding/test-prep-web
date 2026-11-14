"""Source-grounded Midterm 2 practice. HW3-5 await the actual assignments.

Stable IDs and sources are recorded for the accompanying audits. Numerical
tables are original practice fixtures, not transcriptions of slide diagrams.
"""

questions = {}


def _add(topic, ident, category, prompt, answer, explanation, deck, slides):
    questions.setdefault(topic, {})[prompt] = {
        "id": ident,
        "subcategory": category,
        "answer": answer,
        "explanation": explanation,
        "sources": [f"cse320/midterm-2/{deck}.pptx, slides {slides}"],
    }


def _p(ident, category, prompt, answer, explanation, slides):
    _add("Processes", ident, category, prompt, answer, explanation, "8. Processes", slides)


_p("P01", "General", "A single-core machine switches to another runnable process while the current process waits for disk I/O. What benefit does this provide, and does it mean both processes execute instructions simultaneously?",
   "It hides I/O latency and improves CPU utilization. Only one process executes on that core at an instant.",
   "Concurrency permits overlapping lifetimes and waiting; simultaneous instruction execution needs multiple execution resources.", "9-11, 29")
_p("P02", "General", "A child has terminated but its parent is still running. What information remains, and what should a long-running shell do with it?",
   "The child is a zombie: status and process bookkeeping remain. The parent should reap it using wait or waitpid.",
   "Termination and reaping are separate. A SIGCHLD notification alone does not collect the status.", "23-26")
_p("P03", "General", "Compare fork with a successful execve: which creates a new PID, which replaces the program, and which can return to the following statement?",
   "Successful fork creates a child with a new PID and returns in both parent and child. Successful execve replaces the current program, retains its PID, and does not return.",
   "fork returns zero in the child and the child PID in the parent; execve returns only on error.", "12, 15, 27")

_TRACE = "Assume all calls succeed, stdout is unbuffered, each displayed print is atomic, and no external signals intervene. "
_p("P04", "Output", _TRACE + "List every possible output order and value:\n```\nint x = 1;\npid_t p = fork();\nif (p == 0) printf(\"C%d\\n\", ++x);\nelse printf(\"P%d\\n\", --x);\n```",
   "C2 then P0, or P0 then C2.", "Each process has its own x. There is no parent-before-child scheduling guarantee.", "12, 19-20")
_p("P05", "Output", _TRACE + "How many times is each line printed? Is L1,L1,Bye,Bye,Bye,Bye a possible suffix after L0?\n```\nprintf(\"L0\\n\");\nfork();\nprintf(\"L1\\n\");\nfork();\nprintf(\"Bye\\n\");\n```",
   "L0 once, L1 twice, Bye four times. Yes, that suffix is possible.",
   "Both processes may print L1 before either performs the second fork. Each then forks and both descendants print Bye.", "19, 21")
_p("P06", "Output", _TRACE + "Give the line counts and explain the constraint on L2:\n```\nif (fork() != 0) {\n    printf(\"L1\\n\");\n    if (fork() != 0) printf(\"L2\\n\");\n}\nprintf(\"Bye\\n\");\n```",
   "L1 once, L2 once, Bye three times. L2 must follow L1, but the first child can print Bye before L1.",
   "Only the original parent performs the second fork. Each of the three processes reaches the final print.", "19, 22")
_p("P07", "Output", _TRACE + "List every possible output order:\n```\npid_t p = fork();\nif (p == 0) { printf(\"C\\n\"); _exit(7); }\nprintf(\"P\\n\");\nwaitpid(p, NULL, 0);\nprintf(\"D\\n\");\n```",
   "C,P,D or P,C,D.", "The parent's P precedes D, and the child's C precedes termination, which precedes the return from waitpid and D.", "19, 25-26")
_p("P08", "Output", _TRACE + "execve succeeds and the new program prints NEW once and exits. What lines appear?\n```\nif (fork() == 0) {\n    execve(path, argv, envp);\n    printf(\"OLD\\n\");\n    _exit(1);\n}\nwait(NULL);\nprintf(\"DONE\\n\");\n```",
   "NEW followed by DONE; OLD is never printed.", "Successful execve replaces the child program. Waiting orders the parent's DONE after the child's termination.", "25-28")


# PROCESSES CUSTOM: prepared from processes_topic.txt and the November 5 review.
# Code is embedded below so the bank remains independent of local source files.
# All source references support the answer explanation as well as the prompt.
def _pc(number, category, prompt, answer, explanation, slides, example=None,
        modification=None):
    topic = "PROCESSES CUSTOM"
    _add(topic, f"PC{number:02}", category, prompt, answer, explanation,
         "8. Processes", slides)
    record = questions[topic][prompt]
    record["sources"].append(
        "cse320/midterm-2/Nov 5 mt2 review (transcribed on 06-Nov-2026 20-15-16).txt, line 85"
    )
    if example is not None:
        record["sources"].append(
            "cse320/midterm-2/midterm-2-code-examples.md, "
            f"8. Processes.pptx section, entry {example}"
        )
    if modification:
        record["code_modification"] = modification
        record["explanation"] += f"\n\nCode adaptation: {modification}"


_pc(1, "General", "What execution state makes a process more than an executable file? If two users launch that executable, must their processes have the same PID, variable values, and current instruction?",
    "A process includes its program counter, registers, variables, memory, and other execution state. The two instances have distinct PIDs and independent state, so their variable values and current instructions can differ.",
    "The executable describes the program; each process is a running instance with its own identity and virtual address space. Sharing an executable does not make those instances share their changing execution state.", "8, 12, 15")
_pc(3, "General", "Besides hiding I/O latency, give three reasons an operating system supports multiple processes.",
    "Keeping long-running programs from monopolizing the machine, running services/daemons, and performing parallel computation on multiple cores.",
    "The Processes lecture lists responsiveness, services, and multicore computation as distinct benefits of supporting multiple processes.", "9")
_pc(4, "General", "A process is preempted while it could still execute. Another process is waiting for disk input. Classify each using the OS scheduling states and explain the difference.",
    "The preempted process is ready; the process waiting for disk input is blocked.",
    "Ready means eligible to execute when scheduled. Blocked means an external event must occur before the process can become runnable.", "16")
_pc(5, "General", "What must the kernel preserve when switching away from a process so that the process can later resume correctly?",
    "Its execution context, including the program counter and registers, while retaining its process memory/state.",
    "Resuming requires returning to the correct instruction with the correct machine state. The kernel manages the transfer of execution between processes through a context switch.", "8, 11")
_pc(6, "General", "In the utilization model U = 1 - p^n, what do p and n represent? Calculate U when p = 0.5 and n = 3, then explain the effect of increasing n.",
    "p is the fraction of time a process waits for hardware; n is the number of processes. U = 1 - 0.5^3 = 0.875, or 87.5%. Increasing n increases modeled utilization for 0 < p < 1.",
    "The modeled idle fraction is p^n: all n processes are waiting. More processes reduce that idle fraction. This is the lecture's utilization model, not a guarantee for every real workload.", "10")
_pc(7, "General", "What is an exception in the system-control-flow sense, and how does it differ from a context switch?",
    "An exception transfers control to the kernel in response to an event. A context switch transfers execution from one process to another.",
    "An exception describes entry into kernel handling; a context switch describes changing the running process. Kernel handling can return to the same process, so the two terms are not interchangeable.", "3-4, 8, 11")
_pc(8, "General", "Classify a disk-completion notification and a system-call instruction as synchronous or asynchronous exceptions. Explain the distinction.",
    "Disk completion is asynchronous (an interrupt). A system-call instruction is synchronous (an intentional trap).",
    "An interrupt is caused by an external event rather than the current instruction. A system call is deliberately requested by the executing program and enters the kernel through a trap.", "6-7")
_pc(9, "General", "How do a trap, a recoverable fault, and an abort differ in where execution continues after kernel handling?",
    "A trap normally continues at the next instruction; a recoverable fault can restart the faulting instruction; an abort does not resume the interrupted program.",
    "Traps implement intentional transfers such as system calls. Fault handling can repair a condition such as a missing page before retrying. An abort is unrecoverable.", "6")
_pc(10, "General", "What is the purpose of a system call, and what role does errno play when a call fails?",
    "A system call requests an operating-system service. On failure, errno indicates the cause; many calls also return -1.",
    "The call's return value reports success or failure according to that API. errno supplies error information after a reported failure; it is not the normal result of the requested service.", "7, 13")
_pc(11, "General", "A process with PID 410 calls fork and creates child 725. Explain what fork creates and why it returns twice. Give its return value in each process and the child's getpid and getppid values.",
    "fork creates a child process. The single call returns in both processes: 725 in the parent and 0 in the child. In the child, getpid returns 725 and getppid returns 410.",
    "Both processes continue after the same call site. The distinct fork return values select the parent and child paths; zero is the child's fork return value, not its PID. getpid identifies the caller, while getppid identifies its parent.", "12, 15")
_pc(12, "General", "Immediately after fork, which of these are initially copied from the parent: virtual-address-space contents, open file descriptors, and PID? Which copy has separate variable storage?",
    "The child initially gets matching address-space contents and copies of open file descriptors, but a different PID. Its variables occupy a separate virtual address space.",
    "Matching initial contents do not make ordinary parent and child variables shared. Process identity differs even though execution state is initially very similar.", "12, 15")
_pc(16, "General", "Give the three termination mechanisms listed in the Processes lecture. What does an exit status of zero conventionally mean?",
    "Returning from main, calling exit, or receiving a signal whose action terminates the process. Zero conventionally indicates normal/successful completion.",
    "exit terminates with a status and never returns. Returning an integer from main also supplies a status; nonzero conventionally indicates an error.", "18")
_pc(17, "General", "A long-running server creates children but never calls wait or waitpid. After those children terminate, what remains, why is that a problem, and what should the server do? Why doesn't adoption after parent exit solve this while the server remains alive?",
    "The children become zombies: their termination status and process bookkeeping remain. These resources can accumulate while the server stays alive. The server should reap terminated children with wait or waitpid. Adoption after parent exit does not help while the server continues running.",
    "Termination stops execution, but reaping collects the child's status and releases the remaining bookkeeping. A server may remain alive indefinitely, so it cannot rely on its own eventual termination to clean up unreaped children.", "23, 25-26")
_pc(20, "General", "After wait(&status) succeeds, what do its return value and status represent? Explain how WIFEXITED/WEXITSTATUS and WIFSIGNALED/WTERMSIG distinguish and decode the termination cases.",
    "The return value is the reaped child's PID; status contains encoded termination information. If WIFEXITED(status) is true, WEXITSTATUS(status) extracts the normal exit status. If WIFSIGNALED(status) is true, WTERMSIG(status) identifies the terminating signal.",
    "The stored status is neither the returned PID nor a plain exit code. Test the termination case before using its corresponding decoder: a signal-terminated child does not supply a normal exit status through WEXITSTATUS.", "25-26")
_pc(22, "General", "A parent has children A and B. Compare wait(NULL) with waitpid(A, NULL, 0). Can B's termination alone satisfy the second call? What does the NULL status pointer discard, and does either successful call still reap its selected child?",
    "wait can collect an available terminated child; waitpid with positive PID A selects A, so B's termination alone does not satisfy it. NULL discards the encoded termination-status output. Both successful calls still reap their selected terminated child and return its PID.",
    "Selecting a child controls which termination the parent waits for. Requesting status storage is separate from reaping: a NULL pointer declines the status information without preventing collection of the child.", "23, 25-26")
_pc(24, "General", "What is a process graph, and what must a printed output sequence respect to be feasible?",
    "A graph of statement executions and happens-before edges. A feasible sequence must respect every ordering edge, including per-process execution order and synchronization dependencies.",
    "The lecture describes feasible executions as topological orderings. Independent branches may interleave, but a scheduler cannot reverse a required dependency.", "19-22, 25")
_pc(25, "General", "What is exec, and what becomes of the calling process's old code, data, stack, and PID after it succeeds?",
    "exec replaces the current program image. The old code, data, and stack are replaced; the PID is retained.",
    "The operation runs another program inside the existing process. It does not create an additional process or preserve the old program as another executing branch.", "27")
_pc(26, "General", "For execve(filename, argv, envp), what does each argument supply? What is argv[0] conventionally used for?",
    "filename identifies the executable; argv supplies its argument list; envp supplies environment strings of the form name=value. argv[0] conventionally names the program.",
    "The new image starts with the supplied arguments and environment. The slide gives the filename/program name as the convention for argv[0].",
    "27", example=15)
_pc(27, "General", "Must execve's filename always identify a compiled object executable, or can it identify a script? What script feature does the slide describe?",
    "It can identify a script beginning with a #! shebang that names its interpreter, such as #!/bin/bash.",
    "The execve slide explicitly includes interpreter scripts as well as object executables among the programs that can be loaded.", "27")


def _pc_code(number, category, lead, code, answer, explanation, slides, example,
             modification=None):
    _pc(number, category, lead + "\n```c\n" + code + "\n```",
        answer, explanation, slides, example, modification)


_pc_code(31, "Output", "List every possible order of the printed lines, including their values.",
    '''int main()
{
    pid_t pid;
    int x = 1;
    pid = Fork();
    if (pid == 0) {  /* Child */
        printf("child : x=%d\\n", ++x);
        exit(0);
    }
    /* Parent */
    printf("parent: x=%d\\n", --x);
    exit(0);
}''',
    "child : x=2 then parent: x=0; or parent: x=0 then child : x=2.",
    "Each process changes its own copy of x from 1. The child exits before the parent-path print. No wait orders the two processes' prints.", "12, 19-20", 5)
_pc_code(32, "Output", "Give the number of times each line is printed. Then decide which sequences are possible:\nA: L0, L1, Bye, Bye, L1, Bye, Bye\nB: L0, L1, Bye, Bye, Bye, L1, Bye\nC: L0, L1, L1, Bye, Bye, Bye, Bye",
    '''void fork2()
{
    printf("L0\\n");
    fork();
    printf("L1\\n");
    fork();
    printf("Bye\\n");
}''',
    "L0 once, L1 twice, Bye four times. A and C are possible; B is impossible.",
    "Each of the two processes from the first fork prints L1 before creating its second-fork child. One L1 can enable at most two Bye prints. B places three Bye prints before the second L1, violating that dependency. A runs one branch through both Bye prints first; C delays all Bye prints until both L1 prints occur.", "19, 21", 6)
_pc_code(33, "Output", "For each function, give the process ancestry and line counts. Is a Bye before L1 possible? Does reversing the fork comparison change the total number of processes?",
    '''void fork4()
{
    printf("L0\\n");
    if (fork() != 0) {
        printf("L1\\n");
        if (fork() != 0) {
            printf("L2\\n");
        }
    }
    printf("Bye\\n");
}

void fork5()
{
    printf("L0\\n");
    if (fork() == 0) {
        printf("L1\\n");
        if (fork() == 0) {
            printf("L2\\n");
        }
    }
    printf("Bye\\n");
}''',
    "fork4: the original parent creates two children (siblings). fork5: the original parent creates a child that creates a grandchild. Each function prints L0, L1, and L2 once and Bye three times. A Bye before L1 is possible in both. Both create three total processes.",
    "In fork4 only the original parent enters the nonzero branches; its first child can print Bye immediately. In fork5 only children enter the zero branches; the original parent can print Bye immediately. Both require L0 before all other output and L1 before L2, even though their ancestry differs.", "19, 22", "7-8")
_pc_code(34, "Output", "List every possible output order. Which process prints Bye?",
    '''void fork9()
{
    int child_status;
    if (fork() == 0) {
        printf("HC: hello from child\\n");
        exit(0);
    } else {
        printf("HP: hello from parent\\n");
        wait(&child_status);
        printf("CT: child has terminated\\n");
    }
    printf("Bye\\n");
}''',
    "HC, HP, CT, Bye; or HP, HC, CT, Bye. Only the parent prints Bye.",
    "HC precedes child exit, which precedes the parent's return from wait and CT. HP precedes wait; CT precedes the parent's Bye. The child exits inside its branch and cannot reach the final print.", "18, 19, 25", 11)
_pc_code(35, "Output", "Let N = 3. What exit-status values can be printed, and how are they associated with PIDs? Must their order be 100, 101, 102? If all children have already terminated before the first wait, must it reap the one created first or the one that terminated first?",
    '''void fork10()
{
    pid_t pid[N];
    int i, child_status;
    for (i = 0; i < N; i++)
        if ((pid[i] = fork()) == 0)
            exit(100+i); /* Child */
    for (i = 0; i < N; i++) { /* Parent */
        pid_t wpid = wait(&child_status);
        if (WIFEXITED(child_status))
            printf("Child %d terminated with exit status %d\\n",
                   wpid, WEXITSTATUS(child_status));
        else
            printf("Child %d terminate abnormally\\n", wpid);
    }
}''',
    "Three lines report statuses 100, 101, and 102, each paired with the PID of the child created at its corresponding i. Their printed order is not fixed. With several already-terminated children, neither creation order nor termination order is guaranteed to determine which is reaped first.",
    "Each child exits inside the creation loop and therefore never creates later children. Only the original parent completes the loop and performs the three waits. wpid and child_status come from the same wait, so that pair, not the parent's current loop index, identifies the result. wait selects an eligible child; it does not sort the results by creation or termination time.", "26", 13)
_pc_code(36, "Output", "Must the parent line print first? After that parent exits, can the child continue to consume CPU? Define orphan and zombie to classify it, and identify its adopter in the lecture's Unix hierarchy model.",
    '''void fork8()
{
    if (fork() == 0) {
        /* Child */
        printf("Running Child, PID = %d\\n", getpid());
        while (1)
            ; /* Infinite loop */
    } else {
        printf("Terminating Parent, PID = %d\\n", getpid());
        exit(0);
    }
}''',
    "Either line can print first. The child continues its infinite loop after the parent exits. An orphan has lost its parent; a zombie has terminated but has not been reaped. This child is a running orphan, adopted by init in the lecture model, not a zombie.",
    "There is no synchronization ordering the initial prints. Parent termination does not terminate this child. In the lecture's hierarchy, processes descend from init and orphaned children are adopted by init; adoption does not mean the child has stopped executing.", "14, 23-24", 9)
_pc_code(37, "Output", "Why does this shell fork and wait in the parent? The command's new program prints NEW and then exits: what is printed when execl succeeds, and what does the child do if execl fails? If fork returns a negative value, what does the function return and is there a new child?",
    '''int my_system(const char *command)
{
    int status;
    pid_t pid;
    pid = fork();
    if (pid == 0) {
        execl(SHELL, SHELL, "-c", command, NULL);
        _exit(EXIT_FAILURE);
    } else if (pid < 0)
        status = -1;
    else if (waitpid(pid, &status, 0) != pid)
        status = -1;
    return status;
}''',
    "fork lets the child run the command while the parent remains the shell; waiting synchronizes the parent with command completion. Successful execl prints NEW once through the replacement program; the shell function adds no lines. Failed exec reaches _exit(EXIT_FAILURE). A negative fork result creates no child, and my_system returns -1.",
    "Successful exec replaces the calling process's program and never returns to its old next statement. Running it in a child preserves the parent shell. Exec failure returns to the failure-exit line; fork failure instead takes the parent's pid < 0 branch. The parent waits for the child only after successful creation.", "13, 27-28", "2, 16")
_pc_code(38,
    'Code diagnosis',
    'The intent is for the child to print HC and terminate, and for only the parent to print Bye. Identify the missing operation and explain the extra output it permits.',
    'void fork9()\n{\n    int child_status;\n    if (fork() == 0) {\n        printf("HC: hello from child\\n");\n    } else {\n        printf("HP: hello from parent\\n");\n        wait(&child_status);\n        printf("CT: child has terminated\\n");\n    }\n    printf("Bye\\n");\n}',
    'The child branch is missing exit(0). It falls through to the final Bye print, so both processes can print Bye. Restore exit(0) after HC.',
    'Finishing an if branch does not terminate a process. The original slide explicitly exits inside the child branch to prevent this fall-through.',
    '18, 25',
    11,
    "Removed exit(0) from slide 25's child branch to introduce a fall-through bug.")
_pc_code(39, "Code diagnosis", "The intent is to create N children of the original parent, with child i exiting with status 100+i. What is wrong with the child branch below? For N = 3, how many total processes reach the end of the loop?",
    '''pid_t pid[N];
for (int i = 0; i < N; i++) {
    if ((pid[i] = fork()) == 0) {
        /* child work */
    }
}''',
    "The child no longer exits, so it also performs subsequent loop iterations and forks. For N = 3 there are 8 total processes (the original plus 7 descendants), rather than 4. Restore exit(100+i) in the child branch.",
    "Every surviving process now reaches every remaining fork, doubling the count at each iteration: 1 -> 2 -> 4 -> 8. The slide's exit is what keeps each child from continuing the creation loop.", "21, 26", 13,
    "Shortened slide 26 to its creation loop, scoped i inside the loop, and removed the child's exit(100+i) to introduce unintended descendant creation.")
_pc_code(40, "Code diagnosis", "If execl fails, what is wrong with this shortened shell function's control flow? Repair the child branch.",
    '''int my_system(const char *command)
{
    int status = 0;
    pid_t pid = fork();
    if (pid == 0) {
        execl(SHELL, SHELL, "-c", command, NULL);
    } else if (pid < 0) {
        status = -1;
    } else if (waitpid(pid, &status, 0) != pid) {
        status = -1;
    }
    return status;
}''',
    "The child returns 0 from my_system into its caller after failed exec, instead of terminating with failure. Restore _exit(EXIT_FAILURE) immediately after execl.",
    "Only exec failure returns to the old code. Without the slide's failure exit, the child leaves the branch and returns from the function, potentially continuing the shell's caller and incorrectly reporting success.", "13, 27-28", "2, 16",
    "Initialized status to zero and removed _exit(EXIT_FAILURE) from the slide's shell example to isolate failure-path fall-through without using an uninitialized result.")


def _s(ident, category, prompt, answer, explanation, slides):
    _add("Signals", ident, category, prompt, answer, explanation, "8.1 Signals", slides)


_s("S01", "General", "SIGCHLD is blocked while three children exit. Must the parent later receive three separate SIGCHLD handler calls? Explain the required reaping strategy.",
   "No. Standard signals can coalesce into one pending notification. Reap all available terminated children in a loop.",
   "A pending bit records notification, not an event count. A nonblocking waitpid loop prevents waiting for children still running.", "5-6, 15-16")
_s("S02", "General", "A terminal has a foreground pipeline and an unrelated background job. Under ordinary job control, where does Ctrl-C go, and what does it normally do?",
   "The terminal sends SIGINT to the foreground process group. Its default action is termination.",
   "The background job is not in that foreground group. A process may install a SIGINT handler; SIGKILL cannot be caught or ignored.", "4, 7")
_s("S03", "General", "A process blocks SIGINT, receives one, and then restores its previous mask, which did not block SIGINT. Has blocking discarded the signal? Is a handler a child process?",
   "The signal remains pending and becomes eligible for handling when unblocked. The handler runs in the same process.",
   "A handler is another control flow sharing the process's globals, rather than a forked address space.", "5-6, 9, 11-12")
_s("S04", "Handlers", "Find the safety problems and suggest a simple design:\n```\nvoid handler(int sig) {\n    char *p = malloc(100);\n    printf(\"signal %d\\n\", sig);\n    free(p);\n}\n```",
   "malloc, printf, and free are not async-signal-safe. Set a volatile sig_atomic_t flag in the handler and do allocation/output in the main flow.",
   "A signal may interrupt library routines while their internal state is inconsistent. A flag communicates that work is needed without calling those routines.", "13-14")
_s("S05", "Handlers", "What is wrong with reaping one child per notification? Give a nonblocking replacement for the core reaping operation.\n```\nvoid handler(int sig) { waitpid(-1, NULL, 0); }\n```",
   "One call can leave other zombies, and a blocking wait can stall the handler. Use while (waitpid(-1, NULL, WNOHANG) > 0) { /* record reaped PID safely */ }.",
   "Save errno on entry and restore it on exit; production code also handles EINTR and distinguishes ECHILD from unexpected errors. WNOHANG returns zero if children exist but none is ready.", "13, 15-16")
_s("S06", "Handlers", "Why save errno around this handler's work?\n```\nvoid handler(int sig) {\n    int saved = errno;\n    while (waitpid(-1, NULL, WNOHANG) > 0) { }\n    errno = saved;\n}\n```",
   "waitpid can change errno, including setting ECHILD after the last child is reaped. Restore the interrupted main flow's errno.",
   "The handler shares the process environment; it must not silently replace an error code that main was about to inspect.", "13, 15-16")
_s("S07", "Handlers", "A SIGCHLD handler deletes the reaped PID from a job list. Explain the race and the fix:\n```\npid = fork();\n/* child execs and can exit immediately */\nsigprocmask(SIG_BLOCK, &chld_mask, &old);\naddjob(pid);\nsigprocmask(SIG_SETMASK, &old, NULL);\n```",
   "The child can terminate and the handler can delete its PID before addjob runs. Block SIGCHLD before fork, add the job in the parent, then restore the previous mask.",
   "The child inherits the blocked mask and must restore the previous mask before exec. Other job-list accesses also need appropriate protection.", "18-20")
_s("S08", "Handlers", "A handler sets a flag. Why can the main loop below sleep indefinitely, and what primitive avoids the gap?\n```\nwhile (!done) pause();\n```",
   "The signal can arrive after testing done but before pause; then pause waits for another signal. Block the signal while checking, and use sigsuspend to atomically install a temporary mask and wait.",
   "Use a volatile sig_atomic_t flag and recheck it in a loop after sigsuspend returns; restore the original mask afterward.", "21-25")


def _v(ident, category, prompt, answer, explanation, slides):
    _add("Virtual Memory", ident, category, prompt, answer, explanation, "9. Virtual Memory", slides)


_v("V01", "Translation", "Byte-addressed memory has 12-bit virtual addresses, 10-bit physical addresses, and 64-byte pages. Derive the VPN, VPO, PPN, and PPO widths and the number of virtual and physical pages.",
   "VPO=PPO=6 bits; VPN=6 bits; PPN=4 bits; 64 virtual pages and 16 physical frames.",
   "64=2^6. Subtract six offset bits from each address width. Translation preserves the offset.", "4, 16-18")
_SINGLE = "Use this complete single-level mapping for a byte-addressed system with 8 virtual pages, 4 physical frames, and 32-byte pages. All valid pages permit reads/writes. '-' means not resident.\nVPN: 0 1 2 3 4 5 6 7\nValid: 1 1 0 1 1 0 1 1\nPPN: 2 0 - 3 1 - 2 0\n"
_v("V02", "Translation", _SINGLE + "Translate virtual address 0x73. Give VPN, offset, and physical address.",
   "VPN=3, offset=0x13, PA=0x73.", "0x73=3*32+19; VPN 3 maps to frame 3. Equal VA and PA here is incidental.", "16-19")
_v("V03", "Translation", _SINGLE + "What happens when reading virtual address 0x4A? Can the offset alone supply a physical address?",
   "VPN=2 and offset=0x0A; the nonresident PTE causes a page fault. No current physical address can be returned from this mapping.",
   "A page offset identifies a byte within a page, not a physical frame. If the access is legitimate, the OS may page it in and restart the instruction.", "8-9, 19")
_v("V04", "Translation", _SINGLE + "Find ALL virtual addresses that currently map to physical address 0x45.",
   "0x05 and 0xC5.", "PA 0x45 has PPN 2 and offset 5. Both VPN 0 and VPN 6 map to frame 2: 0*32+5 and 6*32+5. Reverse translation need not be unique.", "12, 16-18")
_TWO = "Complete two-level diagram, byte-addressed: virtual space has four directory slots; each present leaf has four PTEs; physical memory has eight frames of 16 bytes each. All shown valid mappings permit reads/writes. Directory: 0->A, 1->absent, 2->B, 3->C. Leaves list PPNs by index 0..3; '-' is nonresident. A=[3,0,-,5], B=[6,1,7,2], C=[-,4,0,6].\n"
_v("V05", "Translation", _TWO + "Infer virtual/physical address widths and the virtual-address bit fields. Then translate VA 0xAD.",
   "VA width=8 bits, PA width=7 bits; VA fields are 2 directory bits, 2 leaf bits, 4 offset bits. 0xAD -> directory 2, leaf 2, offset 0xD -> PPN 7 -> PA 0x7D.",
   "There are 4*4 virtual pages and 8 frames. Offset width is log2(16)=4. The leaf, not the directory's slot number, provides the final PPN.", "16, 29-33, 58")
_v("V06", "Translation", _TWO + "Find ALL virtual addresses mapping to PA 0x63.",
   "0x83 and 0xF3.", "Frame 6 appears in B[0] and C[3]. VPNs are binary 10|00 and 11|11, or 8 and 15. Append offset 3.", "12, 29-33, 58")
_v("V07", "Translation", _TWO + "Compare reads of VA 0x54 and VA 0x21. Where does each walk stop?",
   "0x54: directory index 1 is absent, so no leaf can be consulted. 0x21: directory 0 exists, but A[2] is nonresident.",
   "Both fail to yield a resident data-page mapping, at different levels. Do not invent a missing table or treat a directory index as a frame number.", "29-33, 58")
_TLB = "Use 16-byte pages and a two-level page table. One TLB lookup per data reference; TLB hit bypasses the walk, TLB miss walks both levels. Assume all mappings are present and permitted, no data/PTE caches or page-walk caches, and count the final data RAM access.\n"
_v("V08", "Translation", _TLB + "For a TLB hit mapping VPN 0xA to PPN 3, translate VA 0xA7 and count TLB lookups, page-table RAM reads, and total RAM accesses.",
   "PA=0x37; 1 TLB lookup, 0 page-table RAM reads, 1 total RAM access.", "Append the unchanged 4-bit offset 7 to PPN 3. The TLB supplies translation, not the requested data byte.", "22-27, 33")
_v("V09", "Translation", _TLB + "VA 0xB2 misses in the TLB; the page-table walk maps VPN 0xB to PPN 5. Give the PA and access counts.",
   "PA=0x52; 1 TLB lookup, 2 page-table RAM reads, 3 total RAM accesses.", "One directory read, one leaf read, and one data access. A TLB miss is not necessarily a page fault.", "24, 26-27, 33")
_v("V10", "Translation", "A direct-mapped TLB has 4 sets. Pages are 64 bytes. VA 0x2DA is requested. Derive VPN, offset, TLB set and tag. The selected line has valid=1, tag=2, PPN=5; give the result.",
   "VPN=0xB, offset=0x1A; TLB set=3, tag=2. It hits and produces PA=0x15A.",
   "VPN 11 splits into tag 2 and two-bit index 3. PA=5*64+26=346=0x15A. TLB indexing uses the VPN, not offset bits.", "16, 26-27")
_v("V11", "Translation", "With a single-level page table, no TLB and no caches, how many RAM reads are needed for one permitted resident data load? Compare a three-level table under the same assumptions.",
   "Two for single-level; four for three-level.", "Count one read per page-table level plus the final data read. Fault-service traffic is excluded.", "18, 23, 33")
_v("V12", "Translation", "A page-aligned array of 16,384 one-byte elements is read once in increasing order. Pages hold 1,024 bytes, the initially empty TLB has 4 fully associative entries, and there is no other traffic or eviction except capacity. How many TLB misses and hits occur?",
   "16 misses and 16,368 hits.", "The first byte on each of 16 pages misses. Remaining bytes on that page hit; pages already left behind are not revisited. Having only four entries does not imply a miss every four bytes.", "25-27")
_v("V13", "Translation", "For a 32-bit byte-addressed virtual space, 4 KiB pages, and 4-byte PTEs, find the size of a flat page table. If the 20 VPN bits split evenly across two levels, how large is each table?",
   "Flat: 2^20 entries * 4 bytes = 4 MiB. Each directory or leaf: 2^10 entries * 4 bytes = 4 KiB.",
   "The offset uses 12 bits. A two-level layout can leave leaves for unused regions unallocated, rather than reserving the whole flat table.", "28-33")
_v("V14", "General", "Two processes use the same virtual address 0x1000. Must it refer to the same physical byte? Can different virtual addresses share physical memory?",
   "No; each process has its own mappings. Yes; different virtual pages can map to the same physical frame.", "Isolation and controlled sharing are both supported by page tables.", "5, 12, 51")
_v("V15", "General", "A workload's active pages exceed available physical memory and it repeatedly evicts pages it needs again immediately. Identify the performance problem and explain why locality matters.",
   "Thrashing: repeated page-in/page-out traffic dominates useful work.", "A working set that fits in RAM can be reused after initial faults; a combined working set exceeding RAM defeats that reuse.", "7, 9, 11")
_v("V16", "Translation", "A valid PTE maps VPN 5 to PPN 2 with read=1, write=0. Pages are 256 bytes. Compare a read and a write to VA 0x512. Assume the mapping is genuinely read-only, not copy-on-write.",
   "Read: PA=0x212. Write: protection fault; no permitted data write.", "Residency does not imply permission. The offset 0x12 is preserved, but the access type must also pass the PTE permission check.", "14, 16-19")


def _h(ident, category, prompt, answer, explanation, slides):
    _add("Heap Memory", ident, category, prompt, answer, explanation, "9.1 (The) Heap", slides)


_h("H01", "General", "An allocator has adjacent free blocks of 24 and 40 bytes. A request requires a 56-byte total block. Explain why the request may fail before coalescing and succeed afterward. Contrast this with padding inside a live block.",
   "Separate blocks are individually too small; coalescing forms a 64-byte free block. Padding within an allocated block is internal fragmentation.",
   "The separated free space is external/false fragmentation. Coalescing combines adjacent free blocks without moving live allocations.", "11-12, 20-22")
_h("H02", "General", "Compare an implicit list, an explicit free list, and segregated free lists. Which blocks are searched, and why can segregation help?",
   "An implicit list walks all blocks by size; an explicit free list links only free blocks; segregated lists divide free blocks into size classes.",
   "Explicit lists avoid scanning allocated blocks. Size classes skip clearly undersized blocks and approximate best fit; they do not guarantee constant-time search in every workload.", "15-18, 28, 36, 38-40")
_h("H03", "General", "Free block sizes in search order are 32, 80, 48, 64 bytes. A request needs 40 bytes including overhead. Which does first fit choose and which does best fit choose? Assume splitting is allowed and all remainders are legal.",
   "First fit chooses 80, leaving 40. Best fit chooses 48, leaving 8.", "Fit uses total block requirements; first fit stops at the first sufficient block, while best fit seeks the least excess.", "18-19")
_BAD = "Assume positive sizes, successful allocations, required headers, and no integer overflow unless stated otherwise. Identify the first memory error and give a repair. "
_h("H04", "Bad memory code", _BAD + "\n```\nint value;\nscanf(\"%d\", value);\n```",
   "scanf needs int *, but value is an uninitialized int. Pass &value.", "The destination must be the address of the integer object, not its stored value.", "52-53")
_h("H05", "Bad memory code", _BAD + "\n```\nint *sum = malloc(n * sizeof *sum);\nfor (size_t i = 0; i < n; ++i) sum[i] += 1;\n```",
   "sum[i] is read before initialization. Initialize each element to zero before accumulation (or use suitable zero-initialized allocation).",
   "malloc reserves storage without setting its contents to zero. Successful allocation does not initialize int values.", "54")
_h("H06", "Bad memory code", _BAD + "Assume sizeof(int *)=8 and sizeof(int)=4.\n```\nint **rows = malloc(n * sizeof(int));\nfor (size_t i = 0; i < n; ++i)\n    rows[i] = malloc(m * sizeof(int));\n```",
   "The pointer array is too small: it needs n*sizeof(int *) bytes. Allocate n*sizeof *rows.", "Each rows[i] stores a pointer. Allocating space for n ints provides only half of the required pointer-array storage on the stated machine.", "55")
_h("H07", "Bad memory code", _BAD + "\n```\nint **rows = malloc(n * sizeof *rows);\nfor (size_t i = 0; i <= n; ++i)\n    rows[i] = malloc(m * sizeof **rows);\n```",
   "At i=n, rows[n] writes past the pointer array. Use i<n.", "Valid array indices are 0 through n-1. Correct element sizing does not fix an incorrect iteration count.", "55")
_h("H08", "Bad memory code", "Assume sizeof(int)=4, a has 8 elements, and the target is present at a[1]. Diagnose this traversal and repair its stride:\n```\nint *p = a;\nwhile (*p != target) p += sizeof(int);\n```",
   "p advances four ints (16 bytes), skipping a[1]. Use ++p to advance one int, and bound the search in general.", "Pointer arithmetic scales by the pointed-to type already. This loop reaches a one-past pointer and then dereferences it.", "55")
_h("H09", "Bad memory code", "What does *size-- actually change? How should it decrement the caller's count?\n```\nvoid remove_one(int *size) {\n    *size--;\n    use_count(*size);\n}\n```",
   "It parses as *(size--), decrementing the local pointer. Use (*size)-- to decrement the int.", "The subsequent dereference uses the displaced pointer. Postfix -- binds more tightly than unary *.", "56")
_h("H10", "Bad memory code", "What lifetime problem occurs, and give a repair that returns a usable integer value?\n```\nint *make_value(void) {\n    int value = 42;\n    return &value;\n}\n```",
   "The returned address points to a local object whose lifetime ends on return. Return int 42 by value, or use caller-owned storage.", "Keeping an address does not extend an automatic object's lifetime. A later dereference has undefined behavior.", "57")
_h("H11", "Bad memory code", _BAD + "\n```\nint *p = malloc(4 * sizeof *p);\nint *q = p;\nfree(p);\nfree(q);\n```",
   "free(q) frees the same allocation a second time. Give the allocation one owner and free it once.", "Aliases do not represent separate allocations. Setting p=NULL alone would not make the dangling q valid.", "58")
_h("H12", "Bad memory code", _BAD + "\n```\nint *p = malloc(sizeof *p);\n*p = 9;\nfree(p);\nprintf(\"%d\\n\", *p);\n```",
   "The print reads freed storage. Read/print before free, or copy the value to a live object before freeing.", "An allocator may reuse or modify freed memory. There is no guaranteed output after undefined behavior.", "58")
_h("H13", "Bad memory code", _BAD + "\n```\nvoid work(void) {\n    int *p = malloc(100 * sizeof *p);\n    consume(p); /* neither stores nor frees p */\n}\n```",
   "The allocation leaks when the only pointer is lost. Call free(p) after consume, before return.", "Returning destroys the local pointer, not the heap allocation it points to.", "42, 58")
_h("H14", "Bad memory code", "A nonempty singly linked list owns every node, each separately malloc'd. Does free(head) release the list? Give a safe iterative teardown.",
   "It releases only the first node. Use while (head) { struct node *next = head->next; free(head); head = next; }.",
   "Save next before freeing its node. Reading head->next after free would be use-after-free; freeing only the head leaks the remaining nodes.", "59")
_h("H15", "General", "A tracing collector has root->A, A->B, and C->D->C. No other roots or edges exist. Which objects survive mark-and-sweep, and does the C/D cycle prevent collection?",
   "A and B survive; C and D are reclaimed. Their unreachable cycle does not keep them alive under tracing collection.",
   "Mark follows reachability from roots. Sweep frees unmarked objects; this differs from naive reference counting's handling of cycles.", "42-48")


# One recall prompt per official term. These are a separate study mode, not
# additional scenario coverage or independent copies of review exercises.
_terms = [
    ("Exception", "A transfer of control to the OS kernel in response to a processor/system event.", "8. Processes", "4-6"),
    ("Interrupt", "An asynchronous exception caused by an event external to the executing instruction stream, such as an I/O completion or timer.", "8. Processes", "6"),
    ("System Call", "A controlled interface through which a user program requests a service from the operating system kernel.", "8. Processes", "6-7"),
    ("Synchronous Exception", "An exception caused by executing the program's own instructions, such as a system-call trap or a page fault.", "8. Processes", "6"),
    ("Context Switch", "The kernel saves one execution context and restores another so the CPU can run a different process.", "8. Processes", "8, 11"),
    ("fork", "The operation that creates a child process with a separate virtual address space initially matching the parent's; it returns zero in the child and the child's PID in the parent on success.", "8. Processes", "12"),
    ("exec", "The family of operations that replaces the current process's program image while retaining its PID; successful execution does not return to the old program.", "8. Processes", "27-28"),
    ("wait", "An operation that waits for a child state change, typically termination, collects status, and reaps a terminated child; its successful return identifies the child.", "8. Processes", "23, 25-26"),
    ("exit", "An operation that terminates the calling process with an exit status and does not return.", "8. Processes", "18"),
    ("zombie", "A terminated child whose status and process bookkeeping remain until it is reaped.", "8. Processes", "23"),
    ("orphan", "A child whose parent has terminated; in the lecture model it is adopted by init. It may still be running and is not necessarily a zombie.", "8. Processes", "23-24"),
    ("foreground", "A shell job running in the terminal's foreground process group, ordinarily receiving terminal-generated signals while the shell waits for it.", "8.1 Signals", "2, 7"),
    ("background", "A shell job started without the shell waiting for it to finish before accepting another command; it is outside the terminal's foreground process group under ordinary job control.", "8.1 Signals", "2-3, 7"),
    ("SIGINT", "The interrupt signal commonly sent by terminal Ctrl-C to the foreground process group; its default action is termination and a handler can be installed.", "8.1 Signals", "4, 7, 9-10"),
    ("SIGCHLD", "A notification to a parent of a child state change, including termination; it can prompt the parent to reap children.", "8.1 Signals", "3-4, 15-16"),
    ("SIGALRM", "The timer/alarm signal, whose default action is termination.", "8.1 Signals", "4"),
    ("SIGSEGV", "A signal reporting an invalid memory access or protection violation; its default action terminates the process.", "8.1 Signals", "4"),
    ("SIGKILL", "A signal that forcibly terminates its target and cannot be caught, blocked, or ignored.", "8.1 Signals", "4, 7"),
    ("working set", "The set of active virtual pages a program is using during a period of execution.", "9. Virtual Memory", "11"),
    ("virtual memory", "An abstraction giving each process a private linear address space mapped onto physical memory, with support for caching, management, sharing, and protection.", "9. Virtual Memory", "5-6, 12, 34"),
    ("physical memory", "The actual main-memory storage (DRAM) addressed by physical addresses, providing frames for resident virtual pages.", "9. Virtual Memory", "4, 6-8"),
    ("page table", "A per-process data structure whose entries map virtual pages to physical frames and record mapping state and permissions.", "9. Virtual Memory", "8, 14"),
    ("TLB", "Translation lookaside buffer: a small hardware cache of page-table translations, used to avoid page-table walks on hits.", "9. Virtual Memory", "22-27"),
    ("multi-level page table", "A hierarchy of tables indexed by successive VPN fields; unused lower-level tables need not be allocated, reducing space for sparse address spaces.", "9. Virtual Memory", "28-33"),
    ("address translation", "Mapping a virtual address to its physical address using the page mapping while preserving the within-page offset; some addresses have no permitted resident mapping.", "9. Virtual Memory", "15-19"),
    ("thrashing", "Severe performance degradation from repeatedly moving pages in and out of memory when active working sets exceed available physical memory.", "9. Virtual Memory", "11"),
    ("implicit allocation", "The course's implicit allocator model: the application requests storage, but automatic memory management determines when to reclaim it.", "9.1 (The) Heap", "2, 42-46"),
    ("explicit allocation", "The allocator model where the application explicitly allocates and releases storage, as with malloc and free in C.", "9.1 (The) Heap", "2-3"),
    ("garbage collection", "Automatic reclamation of heap storage that is no longer reachable or otherwise determined reclaimable by the memory manager.", "9.1 (The) Heap", "42-48"),
    ("padding", "Extra space added within a block to satisfy alignment or other block-layout requirements; it contributes to internal fragmentation.", "9.1 (The) Heap", "12"),
    ("implicit list", "A sequence of all heap blocks traversed using block sizes in their headers rather than explicit next/previous free-block pointers.", "9.1 (The) Heap", "15-18"),
    ("payload", "The portion of an allocated block available for the application's requested data, excluding allocator metadata and padding.", "9.1 (The) Heap", "10, 12, 14"),
    ("internal fragmentation", "Space inside allocated blocks that is not requested payload, including metadata, alignment padding, or excess allocation.", "9.1 (The) Heap", "12"),
    ("external fragmentation", "Free space exists, but no individual free block is large enough for a requested allocation.", "9.1 (The) Heap", "11, 20-22"),
    ("coalescing", "Merging adjacent free heap blocks into one larger free block.", "9.1 (The) Heap", "21-23"),
    ("splinters", "Small leftover free fragments that are too small to be useful for subsequent allocation requests.", "9.1 (The) Heap", "18-19, 25"),
]
for _i, (_term, _answer, _deck, _slides) in enumerate(_terms, 1):
    _add("General Concepts", f"D{_i:02}", "Definition recall",
         f"What is {_term}?", _answer, "", _deck, _slides)
