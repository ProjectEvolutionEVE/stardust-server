"""Hypervisors and Virtual Machines: full and paravirtual machines, CPU and memory virtualisation, device passthrough, overcommit, live migration, and cost trade-offs."""
CODE = "computing4_hypervisors"
BOOK = {
    "title": "Hypervisors and Virtual Machines",
    "subtitle": "Running whole computers inside a computer, and the trade-offs",
    "chapters": [
        ("Full and paravirtual machines",
         "A full virtual machine runs an unmodified guest operating system. A paravirtual machine works with the hypervisor, usually through faster special calls, which gives better speed."),
        ("CPU and memory virtualisation",
         "The hypervisor shares the physical processors among the virtual ones, and maps each guest's memory to real memory. Modern processors include hardware help for this work."),
        ("Device passthrough",
         "A device can be assigned directly to one guest. This gives near-native speed, but that device can then no longer be shared with the other guests."),
        ("Overcommit",
         "A host can promise more memory or processor time to its guests than it physically has, because guests rarely use everything they are given. If they all demand their share at once, performance collapses."),
        ("Live migration",
         "A running guest can be moved to another host with only a brief pause. Memory is copied while the guest keeps running, and later changes are sent until the final switch is small."),
        ("Cost trade-offs",
         "Virtual machines give strong isolation and flexibility. But each one carries a full operating system, so it uses more memory and starts more slowly than a container does."),
    ],
    "test": [
        ("What is a full virtual machine?",
         [("a", "A paper machine"), ("b", "A printer"), ("c", "A kind of game"), ("d", "One that runs an unmodified guest operating system")], "d"),
        ("What does the hypervisor share?",
         [("a", "Pictures"), ("b", "Physical processors among the virtual ones"), ("c", "Jokes"), ("d", "Dishes")], "b"),
        ("What is the drawback of device passthrough?",
         [("a", "It is slower than emulation"), ("b", "The device can then no longer be shared"), ("c", "It breaks the network"), ("d", "It removes memory")], "b"),
        ("What is overcommit?",
         [("a", "Promising more memory or processor time than physically exists"), ("b", "Turning off the hypervisor"), ("c", "Buying too many keyboards"), ("d", "Sharing passwords")], "a"),
        ("What does live migration do?",
         [("a", "Deletes guests"), ("b", "Prints a report"), ("c", "Stops the host"), ("d", "Moves a running guest to another host with a brief pause")], "d"),
    ],
}
