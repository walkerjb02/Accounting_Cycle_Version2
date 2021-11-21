# In the first iteration of my accounting cycle program, I talked about adding in a blockchain component that allows the user to verify the inegrity of any infomation that's in the storage. So, using my remake of the SHA-256 algorithm, I added the aforementioned feature into the program. I didn't add in a PoW protocol as there's only one node (the user) in the chain. Futhermore, because my remake of SHA-256 is in Python, as opposed to C which is what hashlib is written in, adding PoW would make the program very, very slow. I would like to maybe learn C so I could make a faster version but that will not be happening for a little bit. I think it would also be neat to add a UDP socket component that would actually allow one to include multiple nodes in the program.
# Going back to the accounting program, though, you will see it is geared more toward financial accounting. I would like to add components that focus on the managerial side of things like budgets, CVP, etc. So, stay tuned for that feature. Lastly, I decided to include a sample storage and hash bank with the program incase you wanted to see how I configured it without copying the code onto your computer and entering journal entries yourself. If you do want to create everything yourself, just follow the instructions that are displayed when you run the program.
# Note: must have Accounting_Cycle_V2, Blockchain, and Hashbank in the same folder for everything in the program to work.
