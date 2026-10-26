"""3D printing: parts built layer by layer, the main methods, and why a printed part is stronger in some directions than others."""
CODE = 'engineering3b_3d_printing'
BOOK = {
    "title": '3D Printing: Parts Built Layer by Layer',
    "subtitle": 'Additive making, the main methods, and why a printed part is weaker in some directions than others',
    "chapters": [
        ('Adding instead of cutting',
         '3D printing, also called additive manufacturing, builds a part by adding thin layers one on top of another. A computer model is sliced into hundreds or thousands of layers, and the printer builds each one in turn. It can make shapes that would be hard to cut from a solid block, such as hollow lattices.'),
        ('Three common methods',
         'Fused deposition melts plastic and pushes it through a nozzle, a simple and slow method. Resin printers cure liquid resin one layer at a time with light, for fine detail. Powder printers use a laser or heat to fuse powder, and metal powder printers can make strong metal parts.'),
        ('Layers and their weak seams',
         'Each layer bonds to the one below it, and that bond is usually weaker than the material itself. A printed part is often weakest when it is pulled apart between the layers. Engineers orient the part so the main load runs along the layers, not across them.'),
        ('Supports for overhangs',
         'A printer cannot print in thin air, so an overhang needs support material underneath it. Supports are removed afterwards and can leave marks on the surface. Designers angle or round overhangs so that fewer supports are needed.'),
        ('Speed and cost per part',
         'A large part can take many hours on a printer, and its cost grows with the time and the material it uses. For one or a few copies, printing can beat the cost of making a mould or die. For thousands of identical parts, a process such as casting or moulding is usually cheaper.'),
        ('Prototypes and money',
         'A printed prototype lets a designer test a shape in days rather than months, before paying for tooling. Track the cost of material by weight, machine time by the hour, and finishing. Finding a problem with a test print costs far less than finding it after a production run.'),
    ],
    "test": [
        ('What is 3D printing also called?',
         [('a', 'Subtractive machining'), ('b', 'Forging'), ('c', 'Additive manufacturing'), ('d', 'Die casting')], 'c'),
        ('Which method melts plastic and pushes it through a nozzle?',
         [('a', 'Resin curing'), ('b', 'Powder fusing'), ('c', 'Die casting'), ('d', 'Fused deposition')], 'd'),
        ('Why are printed parts often weakest between their layers?',
         [('a', 'The bonds between layers are usually weaker than the material itself'), ('b', 'The layers are made of glass'), ('c', 'The printer cools them in ice'), ('d', 'The layers never touch')], 'a'),
        ('What are supports used for in printing?',
         [('a', 'To hold the printer steady on the desk'), ('b', 'To hold up overhangs that would sag in thin air'), ('c', 'To make the part heavier'), ('d', 'To glue the part to the bed for good')], 'b'),
        ('When is printing usually cheaper than making a mould or die?',
         [('a', 'For thousands of identical parts'), ('b', 'Always, for any part'), ('c', 'Only for gold parts'), ('d', 'For one or a few copies, where a mould would cost more')], 'd'),
    ],
}
