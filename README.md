# HONEY_POT
A simple basic honey_pot design

a simple honeypot script in Python that listens on a specified port and logs incoming connection attempts.

In this script, we create a TCP socket, bind it to the specified IP address (0.0.0.0) and port, and listen for incoming connections. When a connection is made, it prints the source IP address and port to the console and logs it in a file called "honeypot_log.txt". 
You can change the port variable to the desired port number you want to use for your honeypot
