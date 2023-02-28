import threading

# Creating threads
def create_threads(iplist, function):

    threads = []

    for ip in iplist:
        th = threading.Thread(target = function, args = (ip,)) #args is a tuple with a single element
        th.start()
        threads.append(th)

    # Instruct program to wait for all threads to finish
    for th in threads:
        th.join()
