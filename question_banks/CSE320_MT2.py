"""Reviewed Midterm 2 practice: PROCESSES CUSTOM.

Stable IDs and source references are recorded in the coverage notes.
Other Midterm 2 topics await preparation and review.
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


# PROCESSES CUSTOM: prepared from processes_topic.txt and the November 5 review.
# Code is embedded below so the bank remains independent of local source files.
# Technical sources support the answers. Starred questions separately cite
# the transcript passage that establishes their study priority.
def _pc(number, category, prompt, answer, explanation, slides, example=None,
        modification=None):
    topic = "PROCESSES CUSTOM"
    _add(topic, f"PC{number:02}", category, prompt, answer, explanation,
         "8. Processes", slides)
    record = questions[topic][prompt]
    if prompt.startswith("⭐ "):
        record["explanation"] += (
            '\n\nPriority basis: In the November 5 review, the instructor explicitly '
            'identifies Processes exercises asking: "here\'s a program. It has a bunch '
            'of printouts. What are valid sequences of those printouts?" '
            'This supports prioritizing this output-tracing exercise; the slides '
            'supply its particular code and technical answer.'
        )
        record["sources"].append(
            "cse320/midterm-2/Nov 5 mt2 review (transcribed on 06-Nov-2026 20-15-16).txt, "
            "line 85 (priority basis: Processes printout-sequence exercises)"
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
_pc(12, "General", "After fork, does the child start with the same variable values as the parent? If the child changes an ordinary local variable, does the parent's value change too? Does the child inherit the parent's open file descriptors and PID?",
    "The child starts with the same variable values, but changing its ordinary local variables does not change the parent's values. It inherits the parent's open file descriptors, but receives a different PID.",
    "fork gives the child a separate virtual address space whose initial contents match the parent's. The variables start with equal values but belong to independent process memory. Inheriting open file descriptors lets the child access files already open in the parent; it does not give the child the parent's process identity.", "12, 15")
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


_pc_code(31, "Output", "⭐ List every possible order of the printed lines, including their values.",
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
_pc_code(32, "Output", "⭐ Give the number of times each line is printed. Then decide which sequences are possible:\nA: L0, L1, Bye, Bye, L1, Bye, Bye\nB: L0, L1, Bye, Bye, Bye, L1, Bye\nC: L0, L1, L1, Bye, Bye, Bye, Bye",
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
_pc_code(33, "Output", "⭐ For each function, give the process ancestry and line counts. Is a Bye before L1 possible? Does reversing the fork comparison change the total number of processes?",
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
_pc_code(34, "Output", "⭐ List every possible output order. Which process prints Bye?",
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
_pc_code(35, "Output", "⭐ Let N = 3. What exit-status values can be printed, and how are they associated with PIDs? Must their order be 100, 101, 102? If all children have already terminated before the first wait, must it reap the one created first or the one that terminated first?",
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
_pc_code(37, "Output", "⭐ Why does this shell fork and wait in the parent? The command's new program prints NEW and then exits: what is printed when execl succeeds, and what does the child do if execl fails? If fork returns a negative value, what does the function return and is there a new child?",
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
