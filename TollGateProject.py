def add_vehicle(vehicle_number, vehicle_type):
    print('..........Added Successfully.............')
def calculate_toll_fee(vehicle_type):
    no_wheels=int(input('Enter no of wheels'))
    if no_wheels==2:
        pay2=int(input('Pay Rs 100'))
        paid=pay2
    elif no_wheels==4:
        pay4=int(input('Pay Rs 200'))
        paid=pay4
    elif no_wheels==6:
        pay6=int(input('Pay Rs 400'))
        paid=pay6
    elif no_wheels==2:
        pay8=int(input('Pay Rs 600'))
        paid=pay8
    else:
        print('Enter a Valid Details')
def display_vehicle_details(vehicle_number):
    print('Vehicle Number\tVehicle Type\Fee Paid')
    print('%d\t%s\t%d'%(vno,vtye,paid))
while True:
    print('1.Add 2.Calculate 3.Display 4.Exit')
    ch=int(input('Enter Your Choice'))
    if ch==1:
        vno=input('Enter Vehicle Number')
        vtye=input('Enter Vehicle Type')
        add_vehicle(vno,vtye)
    elif ch==2:
        calculate_toll_fee()
    elif ch==3:
        display_vehicle_details()
    elif ch==4:
        break






'''
#Mini Project_2: Toll Gate(2,7)
# Function to add a new vehicle
def add_vehicle(vehicle_number, vehicle_type):
# Function to calculate toll fees based on vehicle type
def calculate_toll_fee(vehicle_type):
# Function to display vehicle details
def display_vehicle_details(vehicle_number):
# Function to display total revenue
def display_total_revenue():'''
