A Minimal Python Password Manager

Specs:
64-bit AES encryption

## Setup:
1. Use the built-in c0d3sPl41n.txt file or make your own (technical users only),
   and fill it with passwords using the same format shown in the c0d3sPl41n.txt
   file.
   Optional, but run 'pip install textcrypt' to have the latest and greatest
   encryption protection.
2. Run `python encrypt.py` and enter a password string.
3. Feel free to delete c0d3sPl41n.txt. Your encrypted passwords are now stored
   by default in c0d3sC1ph3r.txt
4. Run 'python password.py' and then enter your password string.
5. Use its case insensitive search to find your account and password.
6. Profit!

## Web Version on Heroku:
The web version can be deployed to Heroku and all instances **must** use HTTPS
for password retrieval for proper security.
To setup on Heroku simply clone the repo and follow below commands:
* Run `heroku create`
* Enter `git push heroku master`
* Checkout your password manager by typing `heroku open`
* Optionally, create an SSL secured custom domain name for easier access
Possible paths:
* `/ - GET` - This is the default way to access your passwords in a GUI manner
* `/secure - POST` - This is the page the form on `/` submits to. More passwords
  can be retrieved from here as well.
* `/api/v1/retrieve - GET` - This API endpoint enables programmatic retrieval of
  data. Simply supply `pass` and `search` as GET parameters and it returns a
  JSON object with the key `data` representing returned password info.

Although the AES encryption should be strong enough for many tasks, I cannot
guarantee password security.
