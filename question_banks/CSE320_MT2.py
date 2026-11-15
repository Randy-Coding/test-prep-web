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
_pc(4, "General", "What are the three OS states a process can be in?",
    "- Running: currently executing on the CPU.\n"
    "- Ready: runnable but not currently executing. A running process enters the ready state when the scheduler preempts it, and it waits to be scheduled again.\n"
    "- Blocked: unable to run until an external event occurs, such as completion of an I/O operation.",
    "The scheduler chooses a ready process to run. Preemption moves a process from running to ready even though it can still execute. A blocked process is not runnable yet because it is waiting for an event such as disk input.", "16")
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
