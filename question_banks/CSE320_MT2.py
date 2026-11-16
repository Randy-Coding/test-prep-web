"""Reviewed Midterm 2 practice: PROCESSES CUSTOM and SIGNALS.

Stable IDs and source references are recorded in the coverage notes.
Signals coverage follows signals_topic.txt and QUESTION GUIDELINES.txt.
"""

questions = {}


# User-approved slide 24 correction; remaining Signals questions follow below.
questions["SIGNALS"] = {
    "⭐ This sequence is proposed as an implementation of sigsuspend(&mask), "
    "where mask and prev are sigset_t objects. What is wrong with it? "
    "Explain how the wait could fail and give the correct replacement.\n\n"
    "```c\n"
    "sigprocmask(SIG_BLOCK, &mask, &prev);\n"
    "pause();\n"
    "sigprocmask(SIG_SETMASK, &prev, NULL);\n"
    "```": {
        "id": "SG01",
        "subcategory": "Code diagnosis",
        "answer":
            "- SIG_BLOCK adds mask's signals to the existing blocked set. "
            "sigsuspend instead temporarily replaces the blocked set with mask. "
            "For example, a signal blocked before this sequence stays blocked "
            "even if mask excludes it, so it cannot wake pause by running its handler.\n"
            "- Separate mask-setting and pause calls leave a race: an unblocked "
            "signal can run its handler after the mask change but before pause. "
            "pause then waits for another signal, even though the event being "
            "awaited has already been handled.\n"
            "- Replace the sequence with sigsuspend(&mask). It atomically installs "
            "mask and suspends execution, then restores the previous mask when "
            "it returns after a handler. Changing SIG_BLOCK to SIG_SETMASK alone "
            "does not remove the race.",
        "explanation":
            "Slide 24 intends to describe an atomic mask/wait/restore operation, "
            "but its SIG_BLOCK operation does not express mask replacement. "
            "Slide 25 demonstrates the intended use: block SIGCHLD before "
            "checking the flag, then call Sigsuspend(&prev) to temporarily "
            "restore the previous mask while waiting. Slide 23 shows the "
            "test/pause race. The user accepted the slide 24 correction. "
            "Here mask is a sigset_t object, so &mask is the pointer passed "
            "to sigsuspend; in its declaration, const sigset_t *mask already "
            "names a pointer parameter.",
        "sources": [
            "8.1 Signals.pptx, slides 12, 23-25 (slide 24 mask-operation correction accepted by user)",
            "midterm-2-code-examples.md, 8.1 Signals.pptx section, entries 34-36",
            "Nov 5 mt2 review (transcribed on 06-Nov-2026 20-15-16).txt, line 85: "
            '"Tell me what I\'m doing wrong."',
        ],
    },
}


def _add(topic, ident, category, prompt, answer, explanation, deck, slides):
    questions.setdefault(topic, {})[prompt] = {
        "id": ident,
        "subcategory": category,
        "answer": answer,
        "explanation": explanation,
        "sources": [f"{deck}.pptx, slides {slides}"],
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
        record["sources"].append(
            "Nov 5 mt2 review (transcribed on 06-Nov-2026 20-15-16).txt, "
            "line 85"
        )
    if example is not None:
        record["sources"].append(
            "midterm-2-code-examples.md, "
            f"8. Processes.pptx section, entry {example}"
        )
    if modification:
        record["code_modification"] = modification
        record["explanation"] += f"\n\nCode adaptation: {modification}"


_pc(1, "General", "How does a process differ from an executable file? Compare the PIDs, variable values, and current instructions of two processes created when two users launch the same executable.",
    "An executable is a file containing program code and initial data that the operating system can load. A process is a running instance of that program, not a type of executable. It includes the loaded code and data along with a program counter, registers, variables, memory, PID, and other execution state. Two processes running the same executable have distinct PIDs and independent state, so their variable values and current instructions can differ.",
    "The executable describes the program; each process is a running instance with its own identity and virtual address space. Sharing an executable does not make those instances share their changing execution state.", "8, 12, 15")
_pc(3, "General", "Why do we need multiple processes?",
    "- Hide I/O or memory latency (improve utilization).\n"
    "- Prevent long-running programs from hogging the computer.\n"
    "- Run services and daemons.\n"
    "- Allow parallel computation on multicore systems.",
    "The Processes slide lists all four as reasons for supporting multiple processes: better utilization while work waits, fair access to the computer, background services, and parallel execution across cores.", "9")
_pc(4, "General", "What are the three OS states a process can be in? How does the programmer perspective describe process states, and what is distinctive about that perspective?",
    "- Running: currently executing on the CPU.\n"
    "- Ready: runnable but not currently executing. A running process enters the ready state when the scheduler preempts it, and it waits to be scheduled again.\n"
    "- Blocked: unable to run until an external event occurs, such as completion of an I/O operation.\n\n"
    "From the programmer perspective:\n"
    "- Running combines the OS Running and Ready states: the process is executing or waiting to be scheduled.\n"
    "- Stopped corresponds to a suspended/blocked process that will not be scheduled until further notice.\n"
    "- Terminated means the process has stopped permanently and the OS has stopped tracking it.\n\n"
    "The distinctive feature of the programmer perspective is that it combines OS Running and Ready into one Running category and describes the process in terms of whether its execution can continue.",
    "The OS model distinguishes the process currently using the CPU from runnable processes waiting for CPU time. The programmer model hides that scheduling distinction: both are Running from the program's perspective. It separately describes processes that are Stopped and those that are permanently Terminated.", "16-17")
_pc(6, "General", "In the utilization model U = 1 - p^n, what do p and n represent, and what is the effect of increasing n?",
    "p is the fraction of time a process waits for hardware, and n is the number of processes. Increasing n increases modeled utilization for 0 < p < 1.",
    "The modeled idle fraction is p^n: all n processes are waiting. More processes reduce that idle fraction. This is the lecture's utilization model, not a guarantee for every real workload.", "10")
_pc(7, "General", "What is an exception in the system-control-flow sense, and how does it differ from a context switch?",
    "An exception transfers control to the kernel in response to an event. A context switch transfers execution from one process to another.",
    "An exception describes entry into kernel handling; a context switch describes changing the running process. Kernel handling can return to the same process, so the two terms are not interchangeable.", "3-4, 8, 11")
_pc(8, "General", "Classify a disk-completion notification and a system-call instruction as synchronous or asynchronous exceptions. Explain the distinction, and state what an asynchronous exception is called.",
    "Disk completion is asynchronous, while a system-call instruction is synchronous and is an intentional trap. An asynchronous exception is called an interrupt.",
    "An interrupt is caused by an external event rather than the current instruction. A system call is deliberately requested by the executing program and enters the kernel through a trap.", "6-7")
_pc(9, "General", "What are the three kinds of synchronous exceptions? Are they intentional or unintentional, and when do they happen?",
    "Traps:\n"
    "Intentional — return to the next instruction afterward.\n"
    "Examples: system calls, breakpoints, and special instructions.\n\n"
    "Faults:\n"
    "Unintentional — may return to the current instruction or abort.\n"
    "Examples: page, segmentation, and protection faults; floating-point exceptions.\n\n"
    "Aborts:\n"
    "Unintentional and unrecoverable — abort the program.\n"
    "Examples: illegal instructions and parity errors.",
    "Traps are deliberate exceptions that resume at the next instruction. Faults arise unintentionally and may be recoverable by retrying the current instruction. Aborts are unintentional, unrecoverable exceptions that terminate the program.", "6")
_pc(10, "General", "What is the purpose of a system call, and what role does errno play when a call fails?",
    "A system call requests an operating-system service. On failure, the global variable errno indicates the cause; many calls also return -1.",
    "The call's return value reports success or failure according to that API. errno supplies error information after a reported failure; it is not the normal result of the requested service.", "7, 13")
_pc(11, "General", "A process with PID 410 calls fork and creates child 725. Explain what fork creates and why it returns twice. Give its return value in each process and the child's getpid and getppid values.",
    "fork creates a child process. The single call returns in both processes: 725 in the parent and 0 in the child. In the child, getpid returns 725 and getppid returns 410.",
    "Both processes continue after the same call site. The distinct fork return values select the parent and child paths; zero is the child's fork return value, not its PID. getpid identifies the caller, while getppid identifies its parent.", "12, 15")
_pc(12, "General", "Describe the child's variable values immediately after fork and the effect of later changes to an ordinary local variable. Also state what happens to the parent's open file descriptors and PID in the child.",
    "The child starts with the same variable values, but changing its ordinary local variables does not change the parent's values. It inherits the parent's open file descriptors, but receives a different PID.",
    "fork gives the child a separate virtual address space whose initial contents match the parent's. The variables start with equal values but belong to independent process memory. Inheriting open file descriptors lets the child access files already open in the parent; it does not give the child the parent's process identity.", "12, 15")
_pc(13, "General", "What is the purpose of calling exit(status) in a child process? What does exit do, and how can the parent use the supplied status?",
    "exit(status) immediately terminates the calling child and does not return. It prevents the child from continuing into later or parent-only code. The child's status remains available for the parent to collect with wait or waitpid; the parent can use WIFEXITED to confirm normal termination and WEXITSTATUS to extract the status value.",
    "Calling exit in a child ends only that process. In a child-creation loop, it also prevents the child from continuing the loop and creating unintended descendants. The parent later reaps the terminated child and inspects its encoded termination status.", "18, 25-26")
_pc(14, "General", "How does Unix differ from Windows in how their processes communicate?",
    "Unix organizes a process and its descendants into a process group. A signal can be sent to the group, and each process decides how to handle it individually; all processes belong to the hierarchy descending from init. Windows gives the creator a handle to the new process. That handle can be passed to other processes, and Windows does not use the same process hierarchy.",
    "The slide contrasts Unix communication through hierarchical process groups and group-directed signals with Windows communication through transferable process handles and no equivalent hierarchy.", "14")
_pc(16, "General", "Give the three termination mechanisms listed in the Processes lecture. Which exit status indicates normal execution?",
    "A process terminates by returning from main, calling exit, or receiving a signal whose action terminates the process. An exit status of 0 indicates normal, successful execution.",
    "Returning from main and calling exit both supply an exit status. A terminating signal is the third mechanism. By convention, status 0 reports successful completion, while a nonzero status reports an error or another unsuccessful outcome.", "18")
_pc(17, "General", "What are zombie and orphan processes? How does each one happen, how are they related, and what happens to each afterward?",
    "A zombie is a child that has terminated but has not yet been reaped, so its exit status and process bookkeeping remain. An orphan is a child whose parent terminates before it does; the orphan may still be running and is adopted by init in the lecture's model. They are related through the parent-child lifecycle, but neither condition implies the other: zombie describes a terminated, unreaped child, while orphan describes a child that has lost its parent. A parent reaps a zombie with wait or waitpid; init adopts an orphan and eventually reaps it after it terminates.",
    "The distinction is whether the child has terminated and whether its original parent is still present. A long-running parent must reap its own terminated children so zombies do not accumulate. If the parent terminates first, the child becomes an orphan and is handled through adoption by init in the lecture's Unix model.", "23-26")
_pc(18, "General", "What is the name of a terminated child whose parent has not reaped it? What happens to it, and how does the parent reap these children?",
    "It is a zombie. The child has stopped executing, but its exit status and process-table entry remain until it is reaped. The parent reaps terminated children by calling wait or waitpid, which collects their termination information and releases the remaining process bookkeeping.",
    "Termination ends the child's execution, while reaping removes the record retained so the parent can collect its status. Until the parent successfully calls wait or waitpid, that terminated child remains a zombie.", "23, 25-26")
_pc(20, "General", "After wait(&status) succeeds, what do its return value and status represent? Explain how WIFEXITED/WEXITSTATUS and WIFSIGNALED/WTERMSIG distinguish and decode the termination cases.",
    "The return value is the reaped child's PID; status contains encoded termination information. If WIFEXITED(status) is true, WEXITSTATUS(status) extracts the normal exit status. If WIFSIGNALED(status) is true, WTERMSIG(status) identifies the terminating signal.",
    "The stored status is neither the returned PID nor a plain exit code. Test the termination case before using its corresponding decoder: a signal-terminated child does not supply a normal exit status through WEXITSTATUS.", "25-26")
_pc(22, "General", "A parent has children A and B. Compare wait(NULL) with waitpid(A, NULL, 0): identify which child's termination satisfies each call, explain what the NULL status pointer discards, and describe what a successful call does to the selected child.",
    "- wait(NULL) waits for any child to terminate. Either child A or child B can satisfy it.\n"
    "- waitpid(A, NULL, 0) waits specifically for child A. Child B terminating does not cause that call to return.\n"
    "- NULL means the parent does not keep information about how the child terminated, such as its exit status.\n"
    "- Even with NULL, the terminated child is still reaped: the operating system removes its remaining process record, so it does not remain a zombie.\n"
    "- A successful call returns the PID of the child it reaped.",
    "Selecting a child controls which termination the parent waits for. Requesting status storage is separate from reaping: a NULL pointer declines the status information without preventing collection of the child.", "23, 25-26")
_pc(25, "General", "What is exec, and what becomes of the calling process's old code, data, stack, and PID after it succeeds?",
    "exec loads and runs another program in the current process. It overwrites the old code, data, and stack, and retains the PID.",
    "Loading and running in the current process means exec does not create another process. The slide states that code, data, and stack are overwritten while the PID is retained.", "27")
_pc(26, "General", "For execve(filename, argv, envp), what does each argument supply? What is argv[0] conventionally used for?",
    "filename identifies the executable; argv supplies its argument list; envp supplies environment strings of the form name=value. argv[0] conventionally names the program.",
    "The new image starts with the supplied arguments and environment. The slide gives the filename/program name as the convention for argv[0].",
    "27", example=15)
_pc(27, "General", "What can execve's filename identify?",
    "An object file or a script file beginning with a #! (shebang), such as #!/bin/bash.",
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
_pc_code(33, "Output", "⭐ For each function, give the process ancestry and line counts. Give an output prefix in which Bye appears before L1, or explain which ordering constraint prevents it. State how changing the conditions from fork() != 0 to fork() == 0 affects the total number of processes.",
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
    "fork4 ancestry: the original parent creates two children (siblings).\n"
    "fork5 ancestry: the original parent creates a child, which creates a grandchild.\n"
    "Line counts for each function: L0 once, L1 once, L2 once, and Bye three times.\n"
    "Bye-before-L1 prefix: L0, Bye, L1 in both functions.\n"
    "Effect of changing fork() != 0 to fork() == 0: the total remains three processes; only the ancestry changes.",
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
_pc_code(35, "Output", "⭐ Let N = 3. What values are passed to exit by the children? What does wait return, and how does the program obtain and associate each child's exit status with its PID? If multiple children have already terminated when wait is called, what determines which child is reaped?",
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
    "The children pass 100, 101, and 102 to exit. Each wait returns the PID of the child it reaped in wpid and stores that child's encoded termination information in child_status. WEXITSTATUS(child_status) extracts the exit status, so each printed PID is paired with the status from that same child. If multiple children are already eligible to be reaped, wait may select any of them; neither creation order nor termination order is guaranteed.",
    "Each child exits inside the creation loop and therefore never creates later children. Only the original parent completes the loop and performs the three waits. wpid and child_status come from the same wait, so that pair, not the parent's current loop index, identifies the result. wait selects an eligible child; it does not sort the results by creation or termination time.", "26", 13)
_pc_code(36, "Output", "What are the possible orders of the parent and child lines? Describe what happens to the child's execution after the parent exits, then classify the child's resulting process state and explain why.",
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
    "Either line can print first. The child continues its infinite loop after the parent exits. It is an ORPHAN, adopted by init in the lecture model. It is not a ZOMBIE because it has not terminated.",
    "There is no synchronization ordering the initial prints. Parent termination does not terminate this child. Orphan describes a child whose parent has terminated; zombie describes a child that has itself terminated but has not been reaped.", "14, 23-24", 9)
_pc_code(37, "Output", "⭐ Why does this shell fork and wait in the parent? The command's new program prints NEW and then exits: what is printed when execl succeeds, and what does the child do if execl fails? If fork returns a negative value, state the function's return value and the number of new child processes.",
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
    "fork lets the child run the command while the parent remains the shell; waiting synchronizes the parent with command completion. Successful execl loads and runs the new program in the child and never returns to this shell code. The new program prints NEW once; the shell function itself prints nothing. If execl fails, it returns to the next statement, _exit(EXIT_FAILURE), which terminates the child with failure. A negative fork result creates no child, and my_system returns -1.",
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
_pc_code(41,
    "Code diagnosis",
    "The code below has a synchronization bug. Explain why its printed messages may be inaccurate, give an output order that demonstrates the problem, and identify the operation and location needed to fix it.",
    '''void fork9()
{
    int child_status;
    if (fork() == 0) {
        printf("HC: hello from child\\n");
        exit(0);
    } else {
        printf("HP: hello from parent\\n");
        printf("CT: child has terminated\\n");
    }
    printf("Bye\\n");
}''',
    "Without wait, nothing tells the parent that the child has terminated before CT is printed. For example, HP, CT, Bye, HC is possible, so the parent may announce termination before the child even prints HC. Add wait(&child_status) after HP and before CT.",
    "fork creates independently scheduled parent and child processes. wait blocks the parent until a child terminates, creating the ordering needed for the CT message to be accurate. Without that synchronization, the scheduler may run the parent through CT and Bye before running the child.",
    "18, 19, 25", 11)
_pc_code(39, "Code diagnosis", "The intent is to create N children of the original parent, with child i exiting with status 100+i. What is wrong with the child branch below? For N = 3, how many total processes reach the end of the loop?",
    '''pid_t pid[N];
for (int i = 0; i < N; i++) {
    if ((pid[i] = fork()) == 0) {
        /* child work */
    }
}''',
    "The child no longer exits, so it also performs subsequent loop iterations and forks. For N = 3 there are 8 total processes (the original plus 7 descendants), rather than 4. Restore exit(100+i) in the child branch.",
    "Every surviving process now reaches every remaining fork, doubling the count at each iteration: 1 -> 2 -> 4 -> 8. The slide's exit is what keeps each child from continuing the creation loop.", "21, 26", 13)
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


# SIGNALS: source-mapped in signals_topic.txt. Code excerpts derive from
# midterm-2-code-examples.md; meaningful adaptations are recorded per question.
def _sg(number, category, prompt, answer, explanation, slides, example=None,
        code=None, modification=None, quote=None, extra_sources=()):
    if quote:
        prompt = "⭐ " + prompt
    if code:
        prompt += "\n\n```c\n" + code.strip() + "\n```"
    _add("SIGNALS", f"SG{number:02}", category, prompt, answer, explanation,
         "8.1 Signals", slides)
    record = questions["SIGNALS"][prompt]
    if example:
        record["sources"].append(
            "midterm-2-code-examples.md, 8.1 Signals.pptx section, "
            f"entries {example}")
    if modification:
        record["code_modification"] = modification
        record["explanation"] += "\n\nCode adaptation: " + modification
    if quote:
        record["sources"].append(
            'Nov 5 mt2 review (transcribed on 06-Nov-2026 20-15-16).txt, '
            f'line 85: "{quote}"')
    record["sources"].extend(extra_sources)


_sg(2, "General", "What is a signal? Describe where it comes from, what information it carries, and the three ways a receiving process can react.",
    "- A signal notifies a process that a system event occurred.\n- The kernel sends it, sometimes at another process's request through kill.\n- It carries its signal-type ID and the fact that it arrived.\n- The process can ignore it, terminate, or catch it with a handler, subject to the signal's permitted actions.",
    "Signals provide process-level event notification. Their limited information does not provide a separate record of each event; SIGKILL's action cannot be overridden or ignored.", "3-5, 9", quote="generic signal theory stuff")
_sg(3, "General", "Compare foreground and background execution in a shell. Why does a long-running shell need to reap its completed background children?",
    "- Foreground: the shell waits for the job before accepting the next command.\n- Background: the shell continues without waiting for that job to finish.\n- Completed children remain zombies until reaped. A shell that keeps running cannot rely on its own termination and init adoption to clean them up; it must reap them, commonly in response to SIGCHLD.",
    "Slides 2-3 introduce signals through the problem of background-child cleanup. Receiving a notification is distinct from collecting the child's termination status with wait or waitpid.", "2-3, 15-16")
_sg(4, "General", "Give the signal name and default action for each event: Ctrl-C, forced uncatchable kill, segmentation violation, timer expiration, and a child stopping or terminating.",
    "- Ctrl-C: SIGINT, terminate.\n- Forced uncatchable kill: SIGKILL, terminate.\n- Segmentation violation: SIGSEGV, terminate.\n- Timer expiration: SIGALRM, terminate.\n- Child stopped or terminated: SIGCHLD, ignore.",
    "This is the course's signal table. SIGKILL cannot be caught or ignored. SIGCHLD's default Ignore action does not itself perform the shell's wait/waitpid reaping work.", "3-4, 15-16")
_sg(5, "General", "Distinguish a pending signal, a blocked signal, and an ignored signal. What state does the kernel keep for pending and blocked signals?",
    "- Pending: sent but not yet received.\n- Blocked: receipt is postponed by the process's signal mask; a signal sent while blocked can remain pending.\n- Ignored: the signal's disposition is to take no action when it is received.\n- The kernel keeps per-process pending and blocked bit vectors, with one bit per signal type.",
    "Blocking postpones receipt; it does not select the Ignore disposition. The pending bits record types awaiting receipt, while blocked bits determine which types are currently withheld.", "5-6, 8-9")
_sg(6, "General", "SIGINT is blocked with no SIGINT initially pending. Three SIGINT signals are sent before it is unblocked. How many pending SIGINT notifications are represented, and how many handler invocations result from those sends after unblocking?",
    "One pending SIGINT is represented, producing one handler invocation after unblocking if a handler is installed. The other sends do not create extra queued notifications.",
    "These ordinary signals have one pending bit per type. Multiple occurrences while that bit is set coalesce; this is why signals cannot count child terminations.", "5-6, 15")
_sg(7, "General", "A shell has one foreground process group and a separate background process group. Describe the recipients and default effects of Ctrl-C and Ctrl-Z. How does fg change the job's role?",
    "- Ctrl-C sends SIGINT to processes in the foreground group; its default action terminates them.\n- Ctrl-Z sends SIGTSTP to processes in the foreground group; its default action stops them.\n- The separate background group is not the target of those terminal keystrokes.\n- fg brings a background job into the foreground.",
    "The terminal directs these signals to the foreground job's process group. Stopping suspends a process rather than terminating it; the default actions differ.", "7-8")
_sg(8, "General", "Compare /bin/kill -9 24818 and /bin/kill -9 -24818. What do getpgrp and setpgid do? For a catchable group-directed signal, how are the individual processes' responses determined?",
    "- /bin/kill -9 24818 targets PID 24818 with SIGKILL.\n- /bin/kill -9 -24818 targets every process in process group 24818 with SIGKILL.\n- getpgrp returns the calling process's group ID; setpgid changes a process's group.\n- Each recipient of a catchable signal uses its own disposition or handler; shared group membership does not require identical responses.",
    "The negative target denotes a process group. SIGKILL itself forces termination, while the deferred Processes learning point concerns the independent dispositions used for catchable signals.", "6-7, 9", extra_sources=("8. Processes.pptx, slide 14",))
_sg(9, "General", "The pending types are SIGINT, SIGALRM, and SIGCHLD; the blocked types are SIGINT and SIGSEGV. Which pending types are eligible for receipt, and what bit-vector expression determines this?",
    "SIGALRM and SIGCHLD are eligible. SIGINT remains pending but blocked. The expression is pending & ~blocked.",
    "The kernel masks out blocked types from the pending vector when checking for signals before returning to the process. No cross-type delivery-order prediction is needed here.", "8")
_sg(10, "General", "What actions do signal(signum, SIG_IGN), signal(signum, SIG_DFL), and signal(signum, handler) select? Where does execution continue after a handler returns normally?",
    "- SIG_IGN selects ignoring that signal type.\n- SIG_DFL restores that type's default action.\n- A handler address installs a user-level handler.\n- After a normal handler return, execution resumes in the interrupted control flow.",
    "Installing a handler changes the signal disposition; catching is executing that handler. Normal return resumes the interrupted process, whereas a handler that exits or performs a nonlocal jump does not follow that normal return path.", "9-10, 30")
_sg(11, "General", "In slide 11's diagram, process A is sent a signal, process B runs, and A later executes its handler. Explain the difference between delivery and receipt here, which process executes the handler, and the blocking rule while that handler runs.",
    "- Delivery records the signal for A; receipt is when A reacts to it by executing its handler. Scheduling can put B's execution between those events.\n- The handler executes in process A and shares A's data; it is a separate control flow within A.\n- The handled signal type is implicitly blocked during the handler under the course's normal handling semantics. Other unblocked signal types can interrupt it.",
    "The figure places both the handler and resumed main flow in A, with context switches to and from B before receipt. Slide 17 explains why the sigaction-based wrapper is used for consistent handling semantics.", "11, 13, 17")
_sg(12, "General", "What makes a function async-signal-safe? List the common async-signal-safe and unsafe functions covered in the course.",
    "An async-signal-safe function is reentrant or cannot be interrupted by signals.\n- Safe: _exit, write, wait, waitpid, sleep, kill.\n- Unsafe: printf, sprintf, malloc, exit.",
    "Slides 13-14 distinguish functions suitable for handlers from functions whose internal state can be disrupted by asynchronous interruption. The simple introductory handler on slide 10 is not a model of these later safety rules.", "13-14")
_sg(13, "General", "Explain the purpose of these handler guidelines: keep handlers simple, save and restore errno, block signals around shared structures, and use volatile sig_atomic_t for a shared flag.",
    "- Simplicity limits work and opportunities to corrupt shared state; setting a flag and returning is a common design.\n- Saving and restoring errno preserves the interrupted code's error information.\n- Temporary blocking protects shared structures from conflicting handler accesses.\n- volatile prevents inappropriate compiler assumptions about a flag changing asynchronously; sig_atomic_t supports indivisible flag reads and writes.",
    "Handlers and main share global state. The flag rule concerns simple reads and writes, not making compound operations or arbitrary data structures safe merely by adding volatile.", "13-14, 21")
_sg(14, "General", "After a successful exec, what happens to the blocked-signal mask, ignored-signal dispositions, and installed custom handlers? Why does the corrected shell restore the child's previous mask before Execve?",
    "- The blocked-signal mask is preserved.\n- Ignored-signal dispositions remain ignored.\n- Installed custom handlers reset to default dispositions.\n- The child restores the previous mask so the new program does not inherit the shell's temporary SIGCHLD block.",
    "The user previously accepted this distinction when deferring the Processes exec question to Signals. The shell's pre-exec mask restoration follows slide 20; the signal manual documents the disposition distinctions. Processes slide 27's broad 'retains signal context' wording should not imply custom handler preservation.", "20", extra_sources=("8. Processes.pptx, slide 27", "https://man7.org/linux/man-pages/man7/signal.7.html"))
_sg(15, "General", "What problems with older signal-handling semantics motivate the sigaction-based Signal wrapper? What does SA_RESTART request?",
    "- Some older systems reset the disposition after catching a signal.\n- Some interrupted system calls return with errno equal to EINTR.\n- Some systems do not implicitly block the type being handled.\n- The wrapper uses sigaction for consistent semantics and SA_RESTART to request restarting interrupted system calls when possible.",
    "Slide 17 lists these portability issues. 'When possible' matters: SA_RESTART is not a guarantee that every interrupted call restarts.", "17")
_sg(16, "General", "Compare busy waiting, sleep(1) polling, and sigsuspend for waiting on a flag set by a signal handler.",
    "- Busy waiting repeatedly tests the flag and wastes CPU.\n- sleep(1) polling gives up CPU between checks but can delay noticing a change until the next poll.\n- sigsuspend atomically installs a temporary signal mask and sleeps until a caught signal returns; used with a protected flag check, it avoids the check/pause race.",
    "Slides 22-25 move from spinning to slower polling and then to an atomic masked wait. The wait condition still needs to be checked after waking.", "22-25")
_sg(30, "General", "What does each function do to a signal set: sigemptyset, sigfillset, sigaddset, and sigdelset? How does changing that set differ from changing the process's blocked-signal mask?",
    "- sigemptyset initializes an empty set.\n- sigfillset initializes a set containing all signal numbers.\n- sigaddset adds a specified signal to a set.\n- sigdelset removes a specified signal from a set.\n- These functions manipulate a set object. sigprocmask uses such a set to change the process's blocked-signal mask.",
    "Slide 12 separates constructing a signal set from applying it with sigprocmask. Merely adding SIGINT to a local set does not block SIGINT for the process.", "6, 12")

_sg(18, 'Code diagnosis', 'What is wrong with this SIGINT handler under the safe-handler guidelines? Identify the unsafe calls and suggest a safer design.',
    '- printf and fflush use the unsafe stdio interface; exit is also unsafe in a handler.\n- Use async-signal-safe output such as write if output is necessary, and _exit if terminating directly. Alternatively, have the handler set a volatile sig_atomic_t flag and return so main performs the stdio work and normal exit.\n- sleep is listed as async-signal-safe, though keeping the handler short is preferable.',
    'The introductory bomb handler illustrates catching SIGINT, but slides 13-14 later restrict which functions handlers should call. Predicting guaranteed stdio output would ignore that safety issue.', '10, 13-14', '22',
    code='void sigint_handler(int sig) /* SIGINT handler */\n{\n    printf("So you think you can stop the bomb with ctrl-c, do you?\\n");\n    sleep(2);    printf("Well...");    fflush(stdout);    sleep(1);\n    printf("OK. :-)\\n");    exit(0);\n}', modification='Excerpted the complete handler; omitted main and its installation code.', quote=None)

_sg(19, 'Handler behavior', 'A SIGINT is sent during the protected region below. Describe its effect during the region and after the last call. Explain why prev_mask is used instead of clearing the entire blocked set.',
    '- SIGINT is blocked during the region and remains pending rather than interrupting it.\n- Restoring prev_mask permits receipt if SIGINT was previously unblocked. If it was already blocked before the region, it stays blocked.\n- Restoring the saved mask preserves all preexisting blocked signals instead of inadvertently unblocking them.',
    'SIG_BLOCK adds SIGINT to the blocked set and saves the previous set; SIG_SETMASK restores exactly that set. The slide comment about unblocking SIGINT depends on its prior state.', '5-6, 12', '23',
    code='sigset_t mask, prev_mask;\n    Sigemptyset(&mask);\n    Sigaddset(&mask, SIGINT);\n    /* Block SIGINT and save previous blocked set */\n    Sigprocmask(SIG_BLOCK, &mask, &prev_mask);\n        /* Code region that will not be interrupted by SIGINT */\n    /* Restore previous blocked set, unblocking SIGINT */\n    Sigprocmask(SIG_SETMASK, &prev_mask, NULL);', modification=None, quote='Tell me what you expect to happen.')

_sg(20, 'Code diagnosis', 'For N > 2, explain how this program can leave zombie children and fail to finish waiting. Show a sequence of child terminations and handler executions that demonstrates the problem, and describe the reaping repair.',
    "- The handler reaps only one child per invocation, while multiple SIGCHLD occurrences can coalesce.\n- For example, the first child triggers the handler and is reaped. While that handler sleeps, several other children terminate. SIGCHLD is implicitly blocked, so their notifications become one pending signal. The next handler invocation reaps only one more child, leaving other terminated children unreaped and ccount positive.\n- Drain available terminated children in a loop. In a responsive shell use waitpid(-1, NULL, WNOHANG) while its return is positive; handle 0 as no terminated child currently available and ECHILD as no remaining children.\n- The plain int shared counter also does not follow the slides' volatile flag guidance; fixing reaping alone is not a general shared-state safety guarantee.",
    'Slide 15 explicitly warns that pending signals are not queued; slide 16 changes one wait to a loop and mentions WNOHANG. One SIGCHLD is notification to check child state, not proof that exactly one child terminated. The example schedule demonstrates a failure rather than claiming every execution fails.', '11, 13, 15-16', '24',
    code='int ccount = 0;\nvoid child_handler(int sig) {\n    int olderrno = errno;  pid_t pid;\n    if ((pid = wait(NULL)) < 0)\n        Sio_error("wait error");\n    ccount--;\n    Sio_puts("Handler reaped child ");\n    Sio_putl((long)pid);\n    Sio_puts(" \\n");\n    sleep(1);  errno = olderrno;\n}\nvoid fork14() {\n    pid_t pid[N];   int i;   ccount = N;\n    Signal(SIGCHLD, child_handler);\n    for (i = 0; i < N; i++) {\n        if ((pid[i] = Fork()) == 0) {\n            Sleep(1);   exit(0);  /* Child exits */\n        }\n    }\n    while (ccount > 0); /* Parent spins */\n}', modification=None, quote='does it leave zombies behind?')

_sg(21, 'Handler behavior', 'In this handler, one child has terminated and another child is still running. Explain what happens after the first child is reaped. How would you change the loop to let the main program continue without waiting for the running child?',
    '- The next wait(NULL) blocks until another child terminates; the handler has not returned to main.\n- Use while ((pid = waitpid(-1, NULL, WNOHANG)) > 0) to reap currently available children without waiting for running ones.\n- A return of 0 ends that drain because children exist but none is currently waitable. A return of -1 with ECHILD means no children remain. Update the error test so it does not treat the 0 case as a wait error based on stale errno.',
    'The printed slide 16 loop uses blocking wait. Its accompanying WNOHANG note describes a nonblocking alternative, not a property of the printed wait call. The loop fixes one-reap-per-signal but may keep control in the handler while other children run.', '16, 19', '25',
    code='void child_handler2(int sig)\n{\n    int olderrno = errno;\n    pid_t pid;\n    while ((pid = wait(NULL)) > 0) {\n        ccount--;\n        Sio_puts("Handler reaped child ");\n        Sio_putl((long)pid);\n        Sio_puts(" \\n");\n    }\n    if (errno != ECHILD)\n        Sio_error("wait error");\n    errno = olderrno;\n}', modification=None, quote=None)


_sg(23, 'Code diagnosis', 'These excerpts use handler for SIGCHLD. Identify the job-list error, give an execution order that produces it, and describe the repair in both parent and child.',
    '- The child can exec and terminate before the parent blocks SIGCHLD and calls addjob.\n- A schedule is: fork; child runs and terminates; handler reaps it and tries deletejob before an entry exists; parent then adds the already-reaped PID. The job list can contain a stale entry.\n- Block SIGCHLD before fork. In the parent keep it blocked until after addjob, then restore the prior mask. In the child restore the inherited prior mask before exec.\n- In this schedule the child has already been reaped: a stale job entry is not itself a zombie process.',
    "Slides 18-20 identify the assumption that the parent runs before the child. Blocking only around addjob is too late to establish the required add-before-delete order. The handler's waitpid options are 0, so this printed handler can also block while other children remain running; that does not explain away the demonstrated job-list race.", '18-20', '27, 28',
    code='int main(int argc, char **argv)\n{\n    int pid;  sigset_t mask_all, prev_all;\n    Sigfillset(&mask_all);\n    Signal(SIGCHLD, handler);\n    initjobs(); /* Initialize the job list */\n    while (1) {\n        if ((pid = Fork()) == 0)  /* Child */\n            Execve("/bin/date", argv, NULL); \n        Sigprocmask(SIG_BLOCK, &mask_all, &prev_all); \n/* Parent */\n        addjob(pid);  /* Add the child to the job list */\n        Sigprocmask(SIG_SETMASK, &prev_all, NULL);\n    }\n    exit(0);}\n\nvoid handler(int sig)\n{\n    int olderrno = errno;\n    sigset_t mask_all, prev_all;\n    pid_t pid;\n    Sigfillset(&mask_all);\n    while ((pid = waitpid(-1, NULL, 0)) > 0) { /* Reap child */\n        Sigprocmask(SIG_BLOCK, &mask_all, &prev_all);\n        deletejob(pid); /* Delete the child from the job list */\n        Sigprocmask(SIG_SETMASK, &prev_all, NULL);\n    }\n    if (errno != ECHILD)\n        Sio_error("waitpid error");\n    errno = olderrno;\n}', modification=None, quote=None)


_sg(25, 'Code diagnosis', "These excerpts explicitly wait for child completion. If pid = 0 is moved below the parent's SIG_SETMASK call, what goes wrong? Give the relevant execution order and explain the original placement.",
    "- Restoring the mask can let a pending SIGCHLD handler run and store the reaped child's PID.\n- The moved pid = 0 then overwrites that notification. The parent may spin indefinitely with no child completion left to set it again.\n- The original code clears pid while SIGCHLD is blocked, then restores the mask; the handler's update therefore follows the reset.",
    'The handler and main share the flag. Blocking protects the order of reset and notification; volatile sig_atomic_t alone does not order those actions. The empty SIGINT handler returns without changing pid.', '13, 21-22', '30, 31',
    code='volatile sig_atomic_t pid;\nvoid sigchld_handler(int s)\n{\n    int olderrno = errno;\n    pid = Waitpid(-1, NULL, 0); /* Main is waiting for nonzero pid */\n    errno = olderrno;\n}\nvoid sigint_handler(int s) { }\n\nint main(int argc, char **argv) {\n    sigset_t mask, prev;\n    Signal(SIGCHLD, sigchld_handler);   Signal(SIGINT, sigint_handler);\n    Sigemptyset(&mask);   Sigaddset(&mask, SIGCHLD);\n    while (1) {\n\tSigprocmask(SIG_BLOCK, &mask, &prev); /* Block SIGCHLD */\n\tif (Fork() == 0)  exit(0); /* Child */\n        /* Parent */\n\tpid = 0;\n\tSigprocmask(SIG_SETMASK, &prev, NULL); /* Unblock SIGCHLD */\n\t/* Wait for SIGCHLD to be received (wasteful!) */\n\twhile (!pid) ;\n\t/* Do some work after receiving SIGCHLD */\n        printf(".");\n    }\n    exit(0);}', modification=None, quote=None)

_sg(26, 'Code diagnosis', 'This loop replaces the busy wait on pid set by the SIGCHLD handler. Identify the problem, show an execution order that demonstrates it, and describe a repair.',
    '- Main tests pid and finds zero. Before pause, SIGCHLD arrives, the handler reaps the child and sets pid nonzero, then returns. Main calls pause anyway and can wait indefinitely for another caught signal.\n- Keep SIGCHLD blocked while testing pid, then use sigsuspend with a temporary mask that permits SIGCHLD; recheck pid in a loop and restore the original mask after waiting.',
    "Slide 23 labels the test/pause race; slide 25 supplies the protected test and atomic wait pattern. This is distinct from SG01's erroneous proposed mask/wait/restore implementation.", '21, 23-25', '32',
    code='while (!pid)\n    pause();', modification='Removed the slide comment naming the diagnosis; retained the loop unchanged.', quote=None)

_sg(27, 'Handler behavior', 'Using these handlers and main, explain why SIGCHLD is blocked before pid is cleared, why Sigsuspend receives &prev, why the wait uses a loop, and which mask is active after Sigsuspend returns.',
    '- Blocking prevents child-exit handling before main has cleared pid.\n- &prev temporarily reinstalls the saved mask, allowing SIGCHLD through if it was originally unblocked, while atomically beginning the wait.\n- SIGINT can wake the wait through its empty handler without changing pid, so the loop must test the condition again.\n- After Sigsuspend returns, the mask from immediately before that call is restored: SIGCHLD is blocked again. The later SIG_SETMASK restores prev for the following main-program work.',
    'The example coordinates a condition check with signal receipt without spinning or leaving a check/pause window. Mask replacement while sleeping is temporary, and a wakeup is not by itself proof the child-completion condition holds.', '21, 24-25', '30, 36',
    code='volatile sig_atomic_t pid;\nvoid sigchld_handler(int s)\n{\n    int olderrno = errno;\n    pid = Waitpid(-1, NULL, 0); /* Main is waiting for nonzero pid */\n    errno = olderrno;\n}\nvoid sigint_handler(int s) { }\n\nint main(int argc, char **argv) {\n    sigset_t mask, prev;\n    Signal(SIGCHLD, sigchld_handler); Signal(SIGINT, sigint_handler);\n    Sigemptyset(&mask);  Sigaddset(&mask, SIGCHLD);\n    while (1) {\n        Sigprocmask(SIG_BLOCK, &mask, &prev); /* Block SIGCHLD */\n        if (Fork() == 0) exit(0);/* Child */\n        /* Wait for SIGCHLD to be received */\n        pid = 0; while (!pid) Sigsuspend(&prev);\n       /* Optionally unblock SIGCHLD */\n        Sigprocmask(SIG_SETMASK, &prev, NULL);\n\t/* Do some work after receiving SIGCHLD */\n        printf(".");\n    }\n    exit(0);}', modification=None, quote=None)


_sg(29, 'Handler behavior', 'What does this program do initially and when Ctrl-C invokes its handler after setup? Explain where execution resumes and whether exit(0) is reached.',
    '- Initially it prints starting, then repeatedly sleeps and prints processing....\n- Ctrl-C invokes the handler, which calls siglongjmp(buf, 1). The saved sigsetjmp returns 1, selecting the else branch and printing restarting. Execution enters the processing loop again.\n- The saved signal mask is restored because sigsetjmp was called with second argument 1.\n- exit(0) is not reached through this flow because the loop has no exit.',
    'Slide 30 shows signal-aware nonlocal control flow within the same process. It restarts the processing loop rather than creating a new process or terminating through the default SIGINT action. Exact numbers of processing messages depend on signal timing.', '26-30', '41',
    code='sigjmp_buf buf;\nvoid handler(int sig)\n{\n    siglongjmp(buf, 1);\n}\nint main()\n{\n    if (!sigsetjmp(buf, 1)) {\n        Signal(SIGINT, handler);\n\tSio_puts("starting\\n");\n    }\n    else\n        Sio_puts("restarting\\n");\n    while(1) {\n\tSleep(1);\n\tSio_puts("processing...\\n");\n    }\n    exit(0); /* Control never reaches here */\n}', modification=None, quote=None)
