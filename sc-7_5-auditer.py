
import socket
import yaml
from yaml.loader import SafeLoader
"""
Control Statement

The information system at managed interfaces denies network communications traffic by default and allows network communications traffic by exception (i.e., deny all, permit by exception).

Supplemental Guidance

This control enhancement applies to both inbound and outbound network communications traffic. A deny-all, permit-by-exception network communications traffic policy ensures that only those connections which are essential and approved are allowed.
"""

MEETS_CONTROL = 0
DOES_NOT_MEET_CONTROL = 1
UNDETERMINED_OUTCOME = 2

class auditTest:
    def __init__(self, ipAddress, portNum, exception):
        self.ipAddress = ipAddress
        self.portNum = portNum
        self.exception = exception

def loadExceptions():
    """
    TODO need to define how to read in the exceptions (guessing yaml?) or multiple times like a security group from aws?
    Currently, exceptions will be in a list of port # exceptions like
    exceptionsList = [21, 22, 80, 443]
    """

    pass

def loadConfig(configFileName):
    """
    this will tell the program what service to test against and how to get there, with eventual support for VPN/proxy/etc
    currently, will only be an ip address of target like
    targetIPAddress = "127.0.0.1"
    """
    try:
        with open(configFileName, 'r', encoding="utf-8") as f:
            configData = yaml.load(f, Loader=SafeLoader)
            #print(configData)

        #print("Length of configData: {}".format(len(configData)))

        return configData
    # TODO add better exception handling like file non-existing and invalid yaml
    except:
        print("[e] File not able to be read, check syntax and priv!")

def createTests(configData):
    """
    This function will create the list of tuples that will be iterated through.
    Currently the tuples in the list will take the form of (target = valid IP address, port = int 0 - 65535, exception = True | False)
    testTests = [("127.0.0.1", 21, True),("127.0.0.1", 22, True),("127.0.0.1", 80, True),("127.0.0.1", 443, True),("127.0.0.1", 445, False),("127.0.0.1", 8080, False)]
    """
    #numOfTargets = len(configData)

    # this creates a dict of dicts?
    for target in configData:

        for value in target.values():
            try:
                print(value['ipAddress'])

            except:
                print("error")

            try:
                print(value['exceptions'])

            except:
                print("error")

            
        #print(target.values())
        #print(type(target.values()))
        #print(target["exceptions"])
        #for portNum in range(1, 65535):



def executeAudit(exceptions, auditTarget):
    """
    This is where the port scan will happen, specifically testing all ports on all interfaces given as a scope
    deviation from this (including deviations from exceptions) will be logged


    """
    pass

def scanPort(currentTest: auditTest):

    ipAddress = currentTest.ipAddress
    portNum = currentTest.portNum
    exception = currentTest.exception

    # this is a TCP test maybe add a protocol?
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ipAddress, portNum))

        if (result == 0) and (exception == True):
            #print("Port {} is open, and has an exception (therefore okay to be open)".format(portNum))
            return MEETS_CONTROL

        elif (result == 0) and (exception == False):
            #print("Port {} is open and should not be (no exception passed in)".format(portNum))
            return DOES_NOT_MEET_CONTROL

        elif (result != 0) and (exception == False):
            #print("Port {} is closed and should be closed".format(portNum))
            return MEETS_CONTROL

        elif (result != 0) and (exception == True):
            #print("Port {} is closed and should be open".format(portNum))
            return UNDETERMINED_OUTCOME

        else:
            #print("Result is {}".format(result))
            return UNDETERMINED_OUTCOME

    except:
        #print("Exception raised")
        return UNDETERMINED_OUTCOME


def auditUnitTest():

    testExceptionsList = [21, 22, 80, 443]
    targetIPAddress = "127.0.0.1"
    testOfTest = [auditTest("127.0.0.1", 21, True), auditTest("127.0.0.1", 22, True), auditTest("127.0.0.1", 80, True), auditTest("127.0.0.1", 443, True), auditTest("127.0.0.1", 445, False), auditTest("127.0.0.1", 8080, False)]

    assert testOfTest[0].ipAddress == "127.0.0.1"
    assert testOfTest[0].ipAddress != "127.0.0.2"
    assert testOfTest[3].portNum == 443
    assert testOfTest[4].exception != True

    scanPort(testOfTest[0])

    x = list(map(scanPort, testOfTest))
    print(x)

    #exit(0)


#auditUnitTest()

testConfig = loadConfig("auditConfig.yaml")
createTests(testConfig)
