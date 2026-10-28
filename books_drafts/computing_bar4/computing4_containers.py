"""Containers and Namespaces: process isolation with namespaces, control groups, image layers, container runtimes, security boundaries, and the limits of containers."""
CODE = "computing4_containers"
BOOK = {
    "title": "Containers and Namespaces",
    "subtitle": "Isolated processes sharing one kernel, and where that isolation stops",
    "chapters": [
        ("Process isolation with namespaces",
         "Namespaces give a process its own view of things such as process IDs, network interfaces, mount points and host names. The process cannot see the rest of the system through that view."),
        ("Control groups",
         "Control groups, usually called cgroups, limit and account for the processor time, memory and other resources a group of processes may use."),
        ("Image layers",
         "A container image is built from stacked layers, and each layer is a set of file changes. Layers shared between images are stored once and reused, which saves space and download time."),
        ("Container runtimes",
         "A container runtime sets up the namespaces and control groups, and then starts the process. Several runtimes exist, and they share standard image formats."),
        ("Security boundaries",
         "Containers share the host's kernel. A flaw in that kernel can break the boundary between containers. For hostile code, containers give weaker isolation than separate machines do."),
        ("Limits of containers",
         "Containers do not run their own kernel, and they cannot run every operating system. Their isolation depends on careful setup, such as dropping unneeded privileges and limiting access."),
    ],
    "test": [
        ("What do namespaces give a process?",
         [("a", "A new kernel for each program"), ("b", "A printer"), ("c", "Free memory"), ("d", "A separate view of process IDs, network and mounts")], "d"),
        ("What do control groups do?",
         [("a", "Limit and account for resources such as processor time and memory"), ("b", "Draw images"), ("c", "Send email"), ("d", "Store passwords")], "a"),
        ("Why are image layers shared?",
         [("a", "They cost more"), ("b", "They cannot be copied"), ("c", "Shared layers are stored once and reused"), ("d", "They are secret")], "c"),
        ("Why are containers weaker than separate machines for hostile code?",
         [("a", "They are slower"), ("b", "They have no memory"), ("c", "They share the host kernel, so a kernel flaw can break the boundary"), ("d", "They use paper")], "c"),
        ("What is a container runtime?",
         [("a", "Something that sets up namespaces and control groups and starts the process"), ("b", "A type of cable"), ("c", "A game"), ("d", "A printer driver")], "a"),
    ],
}
