"""HTTPS and Certificates: how a padlock shows that a connection is encrypted and that the server's identity has been checked."""
CODE = "computing3b_https_certificates"
BOOK = {
    "title": "HTTPS and Certificates",
    "subtitle": "How a secure connection is set up, and what the padlock really tells you",
    "chapters": [
        ("Why plain traffic is risky",
         "Data sent over an ordinary connection can be read by anyone along the path, such as the owner of a shared Wi-Fi network. HTTPS is the same web traffic wrapped in encryption. The S stands for secure."),
        ("Two problems to solve",
         "A secure connection has to solve two problems. The two sides must agree on secret keys that outsiders cannot learn. And the browser must be sure it is talking to the real server, and not to an impostor standing in the middle."),
        ("The handshake",
         "At the start, the browser and the server use public-key maths to agree a shared secret, without sending that secret in the open. Then they switch to a faster secret-key cipher for the rest of the talk. This two-step pattern is how most secure connections work."),
        ("What a certificate says",
         "A server shows a certificate. It names the website, holds the server's public key, and is signed by a certificate authority, an organisation the browser already trusts. If the name does not match, or the signature does not check, the browser warns you."),
        ("What the padlock does not promise",
         "The padlock says the connection is encrypted and the certificate checks out. It does not say the website is honest. A scam site can hold a valid certificate too, so always check the exact address before you trust a site with anything personal."),
        ("Expiry and revocation",
         "Certificates last for a fixed time, and a key that has leaked can be cancelled early. Browsers check the dates and warn when a certificate has expired. Renewing certificates is a routine job that keeps the connection trusted."),
    ],
    "test": [
        ("What does the S in HTTPS stand for?",
         [("a", "Standard"), ("b", "Speed"), ("c", "Secure"), ("d", "Server")], "c"),
        ("What is the main job of a certificate?",
         [("a", "To make pages load faster"), ("b", "To store the user's passwords"), ("c", "To count the visitors to a site"), ("d", "To name the website, hold its public key, and show a trusted authority signed it")], "d"),
        ("What does the padlock in a browser tell you?",
         [("a", "The website is honest and safe"), ("b", "The connection is encrypted and the certificate checks out, but not that the site is honest"), ("c", "Your data is stored in a bank"), ("d", "The site is free to use")], "b"),
        ("Why does HTTPS use public-key maths at the start of a connection?",
         [("a", "To print the page on the screen"), ("b", "To count the packets"), ("c", "To agree a shared secret without sending it in the open"), ("d", "To replace the server's name")], "c"),
        ("What should you do when a browser warns that a certificate's name does not match the site?",
         [("a", "Ignore it, because the site is probably fine"), ("b", "Enter your password quickly"), ("c", "Stop and take care, because you may be talking to an impostor"), ("d", "Turn off the padlock")], "c"),
    ],
}
