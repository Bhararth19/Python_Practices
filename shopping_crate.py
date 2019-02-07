
class Shopping_Cart:
    "it will create a class of shopping cart"
    def __init__(self,item,piece):
        "it will create a function"
        self.my_dict={}
        self.item=item
        self.piece=piece

    def add_item(self):
        "it will create a function add_item"
        self.my_dict[self.item]=self.piece
        return self.my_dict

if __name__=="__main__" :
        shopping_cart_object=Shopping_Cart('apple',10)
        shopping_cart_object=Shopping_Cart('mango',20)
        shopping_cart_object=Shopping_Cart('banana',15)

        my_dict=shopping_cart_object.add_item()
        print(my_dict)