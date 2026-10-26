"""Client and server: how an app asks a server for something, and what the answer means."""
CODE = 'computing3a_api'
BOOK = {
    "title": 'Client and Server',
    "subtitle": 'How an app asks a server for something, and what the answer means',
    "chapters": [
        ('Two sides of a conversation',
         'A client is the app on your screen, such as a browser or a phone app. A server is a program somewhere else that holds the shared data and keeps the rules. The two talk through an API, a set of agreed addresses and message formats.'),
        ('Requests and responses',
         'The client sends a request. It names a method, such as GET to read or POST to send data, along with an address, and sometimes a body of data. The server sends back a response. A GET asks for something; a POST asks the server to act on what was sent.'),
        ('Addresses that name the thing',
         'A good API address tells you what it is about. In the game, the addresses begin with /api/dfg/ and then name the part, such as /market, /auctions or /library. Clear addresses make an API easier to learn.'),
        ('Status codes',
         'Every response carries a status code. Codes from 200 to 299 mean success. A 401 means the sign-in is missing or has expired. A 404 means nothing is at that address. A 500 means the server itself went wrong. A client should react to the code, not guess.'),
        ('One wrapper for every call',
         'The game\'s client wraps every call in one function. That function returns whether the call worked, the status code, the data and a message to show. Each screen can then wait for its calls one at a time, and every failure shows the same kind of message.'),
        ('The server keeps the rules',
         'A client can ask for a trade, but the server checks the sign-in, the price and the funds before it changes anything. A client that is altered or out of date must never be trusted to set a price or move credits on its own.'),
    ],
    "test": [
        ('What is the client in a client-server design?',
         [('a', 'The database only'), ('b', 'The file storage'), ('c', 'The program that asks for something, such as the app on your screen'), ('d', 'The router')], 'c'),
        ('What does a POST request usually do?',
         [('a', 'Reads a page without changing anything'), ('b', 'Sends data to the server, asking it to act'), ('c', 'Deletes the internet connection'), ('d', 'Clears the screen')], 'b'),
        ('What does a 401 status code usually mean?',
         [('a', 'The page was found'), ('b', 'The server is broken'), ('c', 'The address was moved'), ('d', 'The sign-in is missing or has expired')], 'd'),
        ('What does a 404 status code mean?',
         [('a', 'Nothing is at that address'), ('b', 'The call succeeded'), ('c', 'The server is overloaded'), ('d', 'The data was sent twice')], 'a'),
        ('Why should the server check every change, not only the client?',
         [('a', 'Clients are always slower'), ('b', 'Servers have no memory'), ('c', 'A client can be altered, so the server must check the sign-in, the price and the funds'), ('d', 'Clients cannot show results')], 'c'),
    ],
}
