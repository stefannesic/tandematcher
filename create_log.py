import datetime

# global variabel log file
logfile = open("tandematcher.log", "w");

"""
 logs an error message in tandematcher.log with timestamp, error code, 
 name of source functionm, and an error message
"""
def add_err_msg (err_code, fn_name, err_msg):
    timestamp = str(datetime.datetime.now())
    err_string = timestamp + "| Tandematcher Error [{}]: in {}, {}\n".format(
        err_code, fn_name, err_msg)

    logfile.write(err_string);
