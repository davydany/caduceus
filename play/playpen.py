import sys
import inspect

def trace_calls(frame, event, arg):

    # print("Frame: ", frame.f_code)
    # print("Event: ", event)
    # print("Arg:   ", arg)
    co = frame.f_code
    func_name = co.co_name
    print("function: ", func_name)
    print('\t - ', len(inspect.getouterframes(frame)))


def boo():
    print "Called from B"
    d = "D"
    e = "E"
    f = "F"

def aux():
    print "Called from A"
    a = "A"
    b = "B"
    c = "C"
    boo()


sys.settrace(trace_calls)

aux()