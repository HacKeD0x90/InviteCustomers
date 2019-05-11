#!/usr/bin/python
import json
import sys
from geopy.distance import great_circle



####Global Varriables#####
IntercomCoordinates= (53.339428 , -6.257664)
customers=sys.argv[1]

############### A class object to load the json data in to the class ###############
class Customer(object):
    def __init__(self, data):
	    self.__dict__ = json.loads(data)



################## Function to calculate the distance between Customer and Intercom ######################
def CalculateNearestPath(latitude,longitude):
	CustomerCoordinates=(latitude,longitude)
	return great_circle(IntercomCoordinates, CustomerCoordinates).km


################### Function to sort print Invited Customers ######################
def sortAndPrint(InvID,AllCust):
	for id in InvID:
		for y in AllCust:
			Inv=Customer(y)
			if Inv.user_id==id:
				print "Customer  " + Inv.name + " with UserID " + str(Inv.user_id) + " is within 100 KM " 
			else:
				pass




######################## Function to read the file and make necessary operations to get a list of Invited Customers ###############
def ReadFile(CustomersFile):

	print "Reading File With Name " + customers + "\r\n"
	count=0
	Length=0
	AllCustomers=[]
	InvitedCustomersID=[]
	InvitedCustomers=[]
	f = open(customers, "r")
	for x in f:
  		AllCustomers.insert(Length,x)
  		Length =Length+1 
		IntercomCustomer = Customer(x)
		DistanceFromIntercom = int(CalculateNearestPath(IntercomCustomer.latitude,IntercomCustomer.longitude))
		if DistanceFromIntercom <= 100:
			InvitedCustomersID.insert(count,IntercomCustomer.user_id)
			InvitedCustomers.insert(count,x)
			count=count+1
	InvitedCustomersID= sorted(InvitedCustomersID)
	sortAndPrint(InvitedCustomersID,AllCustomers)
	


################### Main Function Starts by reading the Customers.json File################
if __name__ == '__main__':
	ReadFile(customers)
