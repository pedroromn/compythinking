# private.py
""" Class with public and private attributes. """

class PrivateClass:
    """ Class with public and private attributes. """
    
    def __init__(self):
        """ Initialize the public and private attributes. """
        self.public_data = "public"         # public attribute
        self.__private_data = "private"     # private attribute
        
    @property
    def private_data(self):
        return self.__private_data
    
    def __private_method(self):
        self.__private_data = "other private string"
        
    def public_method(self):
        self.__private_method()
        print("OK!!")
        
        
        

def main():
    my_object = PrivateClass()
    print(f"my_object.public_data: {my_object.public_data}")
    #print(f"my_object.__private_data: {my_object.__private_data}")
    #my_object._PrivateClass__private_data = 'modified'
    #print("+"*50)
    #print(f"my_object._PrivateClass__private_data: {my_object._PrivateClass__private_data}")
    print("+"*50)
    print(f"my_object.private_data: {my_object.private_data}")
    print("+"*50)
    my_object.public_method()
    #my_object.__private_method()
    print(f"my_object.private_data: {my_object.private_data}")
    
    
if __name__ == "__main__":
    main()