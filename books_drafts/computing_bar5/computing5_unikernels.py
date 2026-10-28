"""Unikernels: one application packed with just the operating system parts it needs."""
CODE = 'computing5_unikernels'
BOOK = {
    "title": 'Unikernels',
    "subtitle": 'One application packed with just the operating system parts it needs',
    "chapters": [
        ('One application per image', 'A unikernel is an image that holds one application together with only the operating system parts it needs. It runs directly on a hypervisor or on hardware, with no general-purpose system underneath. The result is a single-purpose machine.'),
        ('Library operating systems', 'Unikernels are built from libraries, so the application and its operating services are linked together at build time. This is sometimes called a library operating system. Nothing unused is included.'),
        ('Boot time', 'Because there is so little to start, unikernels can boot in a very short time in favourable cases. Quick starts are useful for scaling up services or for short-lived tasks. Measured times depend on the platform.'),
        ('Attack surface', 'A smaller image has less code that could contain bugs, so there is less to attack. Without a shell or many services, many common intrusions have fewer places to land. The reduction is a real benefit, though not a complete defence.'),
        ('Deployment trade-offs', 'Unikernels can be harder to debug, since normal tools may be missing, and each application needs its own build. Changing or rebuilding can take more effort than in a standard system. Teams weigh smaller, faster images against that extra work.'),
        ('Tooling', 'Tooling for unikernels has grown, with build systems that produce images for common clouds and hypervisors. The tools are still less common than those for ordinary containers, so teams should check support before choosing one.'),
    ],
    "test": [
        ('What does a unikernel hold?',
         [('a', 'One application with the OS parts it needs'), ('b', 'Every game ever made'), ('c', 'Ten operating systems'), ('d', 'Only photos')], 'a'),
        ('How are unikernels built?',
         [('a', 'By hand-painting'), ('b', 'From paper'), ('c', 'By random chance'), ('d', 'From libraries linked together at build time')], 'd'),
        ('Why do unikernels often boot fast?',
         [('a', 'They never boot'), ('b', 'There is little to start'), ('c', 'They are painted quickly'), ('d', 'They skip the power')], 'b'),
        ('What does a smaller attack surface mean?',
         [('a', 'More doors'), ('b', 'Bigger images'), ('c', 'More shells'), ('d', 'Less code that could contain bugs')], 'd'),
        ('What is a drawback of unikernels?',
         [('a', 'They are always free'), ('b', 'They cannot run any application'), ('c', 'Harder to debug, since normal tools may be missing'), ('d', 'They use more memory than anything')], 'c'),
    ],
}
