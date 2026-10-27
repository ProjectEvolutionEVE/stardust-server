"""Passkeys and WebAuthn: public-key login with devices, challenges and origins, phishing resistance, account recovery, attestation, and rollout."""
CODE = "computing4_passkeys"
BOOK = {
    "title": "Passkeys and WebAuthn",
    "subtitle": "Logging in with a key on your device instead of a shared secret",
    "chapters": [
        ("Public-key login with devices",
         "A passkey is a key pair kept on a device. The private key stays on the device. The website keeps only the public key."),
        ("Challenges and origins",
         "The site sends a random challenge, and the device signs it. The signature is tied to the site's origin, so it works only for the right site."),
        ("Phishing resistance",
         "The device signs only for the real origin. A fake copy of a site cannot obtain a login that works on the real one."),
        ("Account recovery",
         "Recovery is the hard part. Teams plan backup methods, such as a second passkey or one-time recovery codes, and check the person's identity carefully before allowing a recovery."),
        ("Attestation",
         "Attestation lets a site learn what type of authenticator was used. Many sites do not need it, and it raises privacy questions."),
        ("Rollout",
         "Teams add passkeys alongside the existing logins, guide users through clear steps, and retire passwords only once the new method is well used."),
    ],
    "test": [
        ("Where is a passkey's private key kept?",
         [("a", "In a newspaper"), ("b", "In an email"), ("c", "On the device"), ("d", "On the site")], "c"),
        ("What does the signed challenge bind to?",
         [("a", "The site's origin"), ("b", "The weather"), ("c", "The user's shoe size"), ("d", "Nothing")], "a"),
        ("Why does a passkey resist phishing?",
         [("a", "It only signs for the real origin"), ("b", "It has no signature"), ("c", "It is typed in"), ("d", "It is public")], "a"),
        ("What is hard about passkeys?",
         [("a", "Account recovery"), ("b", "Turning on the device"), ("c", "Lighting"), ("d", "Sending letters")], "a"),
        ("What is attestation?",
         [("a", "A type of paint"), ("b", "A sign-up form"), ("c", "A cable"), ("d", "Information about the authenticator type, with privacy questions")], "d"),
    ],
}
