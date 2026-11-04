"""Quantum Wavefunctions and Tunnelling: how a quantum particle is described by a wave, how it can pass through barriers, and how this shapes real technology."""
CODE = "science4_phys_tunnelling"
BOOK = {
    "title": "Quantum Wavefunctions and Tunnelling",
    "subtitle": "Waves of probability, barriers that are not solid, and what they make possible",
    "chapters": [
        ("Wavefunctions",
         "A quantum particle is described by a wavefunction. The wavefunction spreads through space and changes in time according to the Schrödinger equation. It holds everything there is to know about the particle’s state."),
        ("Probability density",
         "The square of the wavefunction gives the probability density, which tells us the chance of finding the particle in a region. The probability is never a certainty until a measurement is made. Where the density is high, the particle is more likely to be found."),
        ("Barrier tunnelling",
         "A particle can pass through a barrier that it classically could not climb over. Its wavefunction leaks through the barrier, and there is a small chance of appearing on the far side. This effect is called tunnelling."),
        ("Alpha decay",
         "Alpha particles inside a heavy nucleus can tunnel through the nuclear barrier and escape. This explains why alpha decay can happen at all. The tunnelling probability depends strongly on the energy and the width of the barrier."),
        ("Tunnelling microscopes",
         "The scanning tunnelling microscope measures a tiny current that flows across a gap between a sharp tip and a surface. The current depends very strongly on the gap width. By scanning the tip, scientists can map individual atoms."),
        ("Energy quantisation in wells",
         "A particle trapped in a well can only have certain energy levels, because its wavefunction must fit inside the well. These discrete levels are the origin of many atomic and electronic properties. The levels are a direct sign of quantum behaviour."),
    ],
    "test": [
        ("What describes a quantum particle?",
         [("a", "A ruler"), ("b", "A clock"), ("c", "A bucket"), ("d", "A wavefunction")], "d"),
        ("What does the square of the wavefunction give?",
         [("a", "The probability density, the chance of finding the particle in a region"), ("b", "The mass of the particle"), ("c", "The colour of the particle"), ("d", "The temperature of the room")], "a"),
        ("What is tunnelling?",
         [("a", "Digging a physical hole through rock"), ("b", "A train inside a mountain"), ("c", "A particle passing through a barrier it could not classically climb over"), ("d", "Light turning off")], "c"),
        ("What does a scanning tunnelling microscope measure?",
         [("a", "The weight of a sample"), ("b", "The sound of a surface"), ("c", "A tiny current that flows across a gap"), ("d", "The colour of a flower")], "c"),
        ("Why does a trapped particle have only certain energy levels?",
         [("a", "Because it is always at rest"), ("b", "Its wavefunction must fit inside the well"), ("c", "Because energy is never quantised"), ("d", "Because the well is painted")], "b"),
    ],
}
