"""OAuth 2.0 and OpenID Connect: delegated access, authorisation grants, redirect flows, identity tokens, scopes and consent, and common implementation mistakes."""
CODE = "computing4_oauth_oidc"
BOOK = {
    "title": "OAuth 2.0 and OpenID Connect",
    "subtitle": "Letting an app act for a user, and proving who the user is",
    "chapters": [
        ("Delegated access",
         "OAuth lets an app act for a user with limited access to that user's data. The app never learns the user's password."),
        ("Authorisation grants",
         "A grant is the route by which an app gets its tokens. For most apps, including mobile and single-page apps, the authorisation code grant with PKCE is the recommended choice."),
        ("Redirect flows",
         "The user is sent to the authorisation server, signs in there, and is redirected back with a code. The app then exchanges that code for tokens. Registered redirect addresses must match exactly."),
        ("Identity tokens",
         "OpenID Connect adds an ID token, which is a signed statement about who the user is. The app checks its signature, its issuer, its audience and its expiry time."),
        ("Scopes and consent",
         "Scopes name the kinds of access requested. Users should see a clear consent screen, and apps should ask only for the access they need."),
        ("Common mistakes",
         "Common errors include accepting tokens meant for another audience, skipping the state check, leaking tokens in web addresses, and treating an access token as proof of who the user is."),
    ],
    "test": [
        ("What does OAuth allow?",
         [("a", "Free money"), ("b", "Sharing passwords"), ("c", "Reading minds"), ("d", "Delegated, limited access without sharing a password")], "d"),
        ("What does an ID token tell the app?",
         [("a", "Who the user is"), ("b", "The weather"), ("c", "The colour of a car"), ("d", "The price")], "a"),
        ("What must a registered redirect address do?",
         [("a", "Match exactly what was registered"), ("b", "Change each time"), ("c", "Be random"), ("d", "Point anywhere")], "a"),
        ("What is a scope?",
         [("a", "A microscope"), ("b", "A name for the access requested"), ("c", "A camera"), ("d", "A bowl")], "b"),
        ("What is a common mistake?",
         [("a", "Using a code grant"), ("b", "Reading the docs"), ("c", "Treating an access token as proof of who the user is"), ("d", "Checking expiry times")], "c"),
    ],
}
