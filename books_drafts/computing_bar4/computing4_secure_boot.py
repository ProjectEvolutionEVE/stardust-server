"""Secure Boot and Roots of Trust: a chain of checks at start-up, signed firmware, hardware roots of trust, measured boot, attestation, and recovery after a bad update."""
CODE = "computing4_secure_boot"
BOOK = {
    "title": "Secure Boot and Roots of Trust",
    "subtitle": "Checking every step of start-up before the device trusts it",
    "chapters": [
        ("A chain of checks",
         "When a device starts, each stage checks the signature of the next stage before running it. Only trusted code is loaded, one stage at a time."),
        ("Signed firmware",
         "Firmware carries a digital signature from its maker. The device refuses any firmware whose signature does not match."),
        ("Hardware roots of trust",
         "The chain starts in hardware that software cannot change. This hardware holds the first trusted keys, so the rest of the chain has a solid base."),
        ("Measured boot",
         "Measured boot records a hash of each stage as it starts. The device can then report exactly what it started with, not just whether it was allowed to start."),
        ("Attestation",
         "A device can prove its measured state to a remote checker, using keys held in its hardware. The server then decides whether to trust the device."),
        ("Recovery after a bad update",
         "If an update fails its check, the device falls back to a known-good image. It can still start, and it can be repaired."),
    ],
    "test": [
        ("What does each boot stage do?",
         [("a", "Plays a tune"), ("b", "Deletes the next stage"), ("c", "Checks the signature of the next stage before running it"), ("d", "Prints")], "c"),
        ("What is a root of trust?",
         [("a", "A tree in a park"), ("b", "The hardware-based start of the trusted checks"), ("c", "A user name"), ("d", "A cable")], "b"),
        ("What does measured boot record?",
         [("a", "Hashes of each stage"), ("b", "Player names"), ("c", "Weather"), ("d", "Prices")], "a"),
        ("What is attestation?",
         [("a", "Proof of measured state to a remote checker"), ("b", "A type of paint"), ("c", "A sign-up form"), ("d", "A cable")], "a"),
        ("What happens after a bad update?",
         [("a", "The device falls back to a known-good image"), ("b", "It stops forever"), ("c", "It erases itself"), ("d", "It sings")], "a"),
    ],
}
