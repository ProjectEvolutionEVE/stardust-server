"""Physically Based Shading: surface materials that obey energy conservation, so they look right in any light."""
CODE = 'computing5_physically_based_shading'
BOOK = {
    "title": 'Physically Based Shading',
    "subtitle": 'Surfaces that never reflect more light than they receive',
    "chapters": [
        ('What physically based means',
         'Physically based shading describes materials with rules drawn from real optics. The aim is a surface that looks right under any lighting, not just under one lamp chosen by an artist. Energy conservation is the central rule.'),
        ('Energy conservation',
         'A surface cannot send out more light than it receives. The light that is reflected plus the light that is absorbed or transmitted must add up to what arrived. Following this rule keeps materials believable.'),
        ('Microfacet models',
         'Microfacet models treat a rough surface as many tiny mirrors pointing in different directions. Roughness sets how spread out those directions are. Most modern materials use a model of this kind.'),
        ('Roughness and metalness',
         'Roughness controls how sharp or blurred a reflection looks. Metalness separates metals, which tint their reflections, from non-metals, which reflect white light and show a diffuse colour. Artists set these two values to describe most surfaces.'),
        ('Texture pipelines',
         'Textures store values such as colour, roughness and surface detail. Colour data must be handled in the right colour space, or the lighting will look wrong. A consistent pipeline keeps textures predictable across tools.'),
        ('Real-time approximations and artists',
         'Real-time engines use fast approximations of the full models to keep the frame rate high. Artists work within these rules, which makes their results reusable across scenes. Shared rules let a whole team produce matching assets.'),
    ],
    "test": [
        ('What does energy conservation mean for a surface?',
         [('a', 'It cannot send out more light than it receives'), ('b', 'It must always be painted white'), ('c', 'It must glow in the dark'), ('d', 'It must be made of wood')], 'a'),
        ('What do microfacet models assume a rough surface is made of?',
         [('a', 'One large flat sheet of paper'), ('b', 'Liquid water only'), ('c', 'Many tiny mirrors pointing in different directions'), ('d', 'Sand with no structure')], 'c'),
        ('What does roughness control?',
         [('a', 'The size of the file on disk'), ('b', 'How sharp or blurred a reflection looks'), ('c', 'The speed of the mouse'), ('d', 'The name of the material')], 'b'),
        ('What does metalness separate?',
         [('a', 'Fast surfaces from slow surfaces'), ('b', 'Large objects from small ones'), ('c', 'Day from night'), ('d', 'Metals, which tint reflections, from non-metals')], 'd'),
        ('Why must colour data be handled in the right colour space?',
         [('a', 'Otherwise the lighting and colours will look wrong'), ('b', 'Because colour data cannot be stored'), ('c', 'Because only black textures are allowed'), ('d', 'Because textures must be printed')], 'a'),
    ],
}
