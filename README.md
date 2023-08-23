# sl0ppy-flood
A https & http flooder, hitting your servers with 503 server error, Other server errors it gives are 504, 502.

# https|http flooder
* Added bypass
* A list of 7k + User Agent to connect with, these consist out of a large customized list. 
* A referal list that needs to be worked on bit more. 
* Proxy list for connections, using the user agents to connect with 
* Proper load balanced site, nginx + apache + nginx-reuseport load balanced, will not stand a chance against this!!
* Throwing 503 server errors, on proper load balanced sites!!
* cloudflare bypass 

# Load balanced tested..
* nginx + apache + nginx-reuseport
* nginx + apache load balanced.
* Likely others, (not tested yet.)

# server errors 
* throws 503 server error
* throws 502 server error 
* throws 501 server error 
* throws 508 server error resource limited reached. 

# tested on cloudflare site.
* throws 508 server error resource limited reached. 



# Usage 
* `python sl0ppy-flood3.py`
* `enter host`
* `enter proxy list`
* `enter threads` (for legacy cpu, i5-5th-gen, or cpu with 4core use: 300|400 threads, for 6core or more use desired threads.)

# change log 
* Added more os.name for bypassing 



# Legal Disclaimer: 
* I am not responsible for U using it on non authorized systems, make sure u use it on systems u own or are authorized on. 

* x0xr00t 
