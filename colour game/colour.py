#creating the class
class colourgame:
    def __init__(self):
        #inputing colour of element
        self.colour = {
            "red":["ink","blood","apple"],
            "black":["ink","sky"],
            "yellow":["banana","frog"],
            "green":["apple","banana"],
            "blue":["sky","frog"],
            "white":["salt"]
        }
        #flags values of each element and it's False as in starting no element is subscribed
        self.subscriber = {
            "banana":False,
            "ink":False,
            "salt":False,
            "frog":False,
            "blood":False,
            "sky":False,
            "apple":False}
        
        
    #evaluating the user input and shifting the control to specific functions
    def task_evaluation(self,user_command):
        if type(user_command)==str:
            if user_command=="list":
                return str(self.List())
            if user_command[0]=="+" and user_command[1:] in self.subscriber:
                return self.subscribeUnsubscribe(user_command[1:],True)
            elif user_command[0]=="-" and user_command[1:] in self.subscriber:
                return self.subscribeUnsubscribe(user_command[1:],False)
            #invalid input entered
            elif user_command[0]=="+" or user_command[0]=="-":
                return "Invalid Input"
            elif user_command in self.colour:
                return self.printcolour(user_command)
            else:
                return ""
        else:
            return ""
        
    #check function... 
    def subscribeUnsubscribe(self,element , value):
        if self.subscriber[element]==value==True:
            return "already subscribed"
        elif self.subscriber[element]==value==False:
            return "already Unsubscribed"

        self.subscriber[element] = value
        if value:
            return f"subscribing {element}"
        else:
            return f"unsubscribing {element}"
        
    #outputting the message and appending the element to list  
    def printcolour(self,user_command):
        outputcolours = []
        for element in self.colour[user_command]:
            if self.subscriber[element]:
                #exception case
                if element=="frog":
                    outputcolours.append(f"i'm {element}! I am {user_command} today")
                #general case
                else:
                    outputcolours.append(f"i'm {element}! I'm sometimes {user_command}")
        return outputcolours

    #listing all the subscribed elements
    def List(self):
        return [ele for ele in self.subscriber if self.subscriber[ele]]
        
#driving function   
def start(): 
    #creating instance of  
    colourgameobject = colourgame()
    user_command = input("Enter your command : ")
    while user_command!="exit":
        
        if user_command=='':
            pass
        else:
            output = colourgameobject.task_evaluation(user_command)   

            if type(output)==list:
                for i in output:
                    print(i)
            else:
                print(output)


        user_command = input()


if __name__ == "__main__":
    print("-----Welcome to Colour game----")
    start()           