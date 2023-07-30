# sl0ppy-flood
A https & http flooder, hitting your servers with 503 server error, Other errors it gives 504, 502.

# https|http flooder
* Added bypass
* A list of 7k + User Agent to connect with, these consist out of a large customized list. 
* A referal list that needs to be worked on bit more. 
* Proxy list for connections, using the user agents to connect with 
* Proper load balanced site, nginx + apache + nginx-reuseport load balanced, will not stand a chance against this!!
* Throwing 503 server errors, on proper load balanced sites!!

# Load balanced tested..
* nginx + apache + nginx-reuseport
* nginx + apache load balanced.
* Likely others, (not tested yet.)

# Usage 
* `python sl0ppy-flood3.py`
* `enter host`
* `enter proxy list`
* `enter threads` (for legacy cpu, i5-5th-gen, or cpu with 4core use: 300|400 threads, for 6core or more use desired threads.)

# change log 
* Added more os.name for bypassing 
* fixed colors for stdout sum times this showed red or yellow, should now be fixed
* Added extra sqeez for the the ddos impact on load balanced sites see the following
* `  1.) Increase Concurrent Requests: To increase the impact, we can increase the number of concurrent requests sent by each thread.

   2.) Randomize User-Agent and Referer: Load-balancers often detect and block common User-Agent and Referer strings. We can use a larger and more diverse list of User-Agent and Referer headers to make the requests appear more legitimate and difficult to detect.

   3.) Add Random Delays: Adding random delays between requests can simulate human behavior and make the attack harder to mitigate.`
  
# Legal Disclaimer: 
* I am not responsible for U using it on non authorized systems, make sure u use it on systems u own or are authorized on. 

* x0xr00t 
