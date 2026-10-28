"""eBPF in the Kernel: small, checked programs that run safely inside the operating system kernel."""
CODE = 'computing5_ebpf'
BOOK = {
    "title": 'eBPF in the Kernel',
    "subtitle": 'Small, checked programs that run safely inside the operating system kernel',
    "chapters": [
        ('Programs inside the kernel', 'eBPF lets a small program run inside the operating system kernel, to watch or change how it handles events. The program is loaded while the system runs, so there is no need to rebuild the kernel or restart the machine.'),
        ('The verifier', 'Before a program runs, the kernel verifier checks it. It makes sure the program ends, does not read memory it should not, and uses only allowed helpers. A program that fails the check is refused.'),
        ('Hooks for networking and tracing', 'eBPF programs attach to hooks, such as the points where network packets arrive or where system calls happen. A hook tells the program when to run. This makes eBPF useful for fast packet handling and for tracing.'),
        ('Maps', 'Maps are shared storage that eBPF programs can use to keep counts or settings. User programs can read and update maps too. Maps let the kernel side and the user side work together.'),
        ('Safety limits', 'The verifier limits the size and loops of programs, so they cannot hang the kernel. These limits make eBPF safe enough for production use, though they constrain what a program can do.'),
        ('Observability tools', 'Many monitoring and security tools now use eBPF to observe a system with little overhead. Engineers use it to see network traffic and slow calls without changing the application. It has become a common tool in modern operations.'),
    ],
    "test": [
        ('What does eBPF let a small program do?',
         [('a', 'Paint the desktop'), ('b', 'Print books'), ('c', 'Run safely inside the kernel'), ('d', 'Cook dinner')], 'c'),
        ('What does the verifier do?',
         [('a', 'Paints the screen'), ('b', 'Checks a program is safe before it runs'), ('c', 'Deletes the kernel'), ('d', 'Plays music')], 'b'),
        ('What do hooks do?',
         [('a', 'Tell the program when to run, such as on packet arrival'), ('b', 'Hang coats'), ('c', 'Lock doors'), ('d', 'Cut wires')], 'a'),
        ('What are maps used for in eBPF?',
         [('a', 'Coloured charts only'), ('b', 'Road maps'), ('c', 'Pictures of places'), ('d', 'Shared storage between kernel and user programs')], 'd'),
        ('Why are loops limited?',
         [('a', 'So programs can sing'), ('b', 'So programs print faster'), ('c', 'So programs cannot hang the kernel'), ('d', 'So screens stay bright')], 'c'),
    ],
}
