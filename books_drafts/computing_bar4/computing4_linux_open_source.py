"""Linux and Open-Source Communities: how the kernel is developed, who decides, and how companies and communities sustain it."""
CODE = 'computing4_linux_open_source'
BOOK = {
    "title": 'Linux and Open-Source Communities',
    "subtitle": 'How the kernel is developed, who decides, and how it is sustained',
    "chapters": [
        ('Kernel development process',
         'The Linux kernel is the core of the Linux system. Changes are proposed on public mailing lists, reviewed by many people, and then merged in stages. This process is slow but it catches many problems before they reach users.'),
        ('Maintainers and hierarchy',
         'Maintainers look after parts of the kernel, and they decide which changes are accepted. Maintainers send their work up to others, in a chain that ends with the project lead. The structure gives clear responsibility without a single controller of every line.'),
        ('Licensing choices',
         'The Linux kernel is released under the GNU General Public License, version 2. This copyleft licence means changed versions that are distributed must share their source. The licence has helped keep the kernel open for everyone.'),
        ('Community governance',
         'Open-source communities govern themselves through written codes of conduct, voting rules and process documents. Some projects use committees and others a benevolent leader. Good governance is written down and applied fairly.'),
        ('Company involvement',
         'Many companies pay engineers to work on Linux, because it runs their products and services. Company involvement brings resources, but it can also shift priorities. Healthy projects balance paid and volunteer contributions.'),
        ('Sustainability',
         'Open-source projects depend on maintainers who have time and support. Burnout and unpaid work are real risks. Funding, shared duties and clear succession plans help a project last for decades.'),
    ],
    "test": [
        ('How are kernel changes usually proposed and reviewed?',
         [('a', 'On public mailing lists, by many reviewers'), ('b', 'In secret by one person'), ('c', 'Only by phone calls'), ('d', 'By paper forms')], 'a'),
        ('What is the job of a kernel maintainer?',
         [('a', 'To sell the kernel to shops'), ('b', 'To paint the office'), ('c', 'To look after parts of the kernel and decide which changes are accepted'), ('d', 'To write the company accounts')], 'c'),
        ('Which licence is the Linux kernel released under?',
         [('a', 'A private licence'), ('b', 'The GNU General Public License, version 2'), ('c', 'No licence at all'), ('d', 'A licence for music only')], 'b'),
        ('What is a risk for open-source projects?',
         [('a', 'Too many lunches'), ('b', 'Too much sunlight on servers'), ('c', 'Too many licences to read'), ('d', 'Burnout and unpaid work by maintainers')], 'd'),
        ('Why do companies pay engineers to work on Linux?',
         [('a', 'Because Linux runs their products and services'), ('b', 'Because Linux is illegal'), ('c', 'Because Linux is a paper product'), ('d', 'Because companies must fund holidays')], 'a'),
    ],
}
