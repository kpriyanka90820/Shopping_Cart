from flask import *
from flask_cors import CORS
import re, json, requests, socket
global IPAddr

## Get Hostname inorder to run the script on your machine's IP
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

app = Flask(__name__)

## extension for handling Cross Origin Resource Sharing 
CORS(app)

@app.route('/cart', methods=['POST'])
def shopping():
    if request.method == 'POST':
        result = {}
        res = json.loads(request.data)
        products_list = res['products']
        
        ## Count number of each Products to calculate billing amount
        no_of_Tshirts = products_list.count('T-shirt')
        no_of_Trousers = products_list.count('Trousers')
        no_of_Shoes = products_list.count('Shoes')
        no_of_Jacket = products_list.count('Jacket')
        
        ## Calculate Total amount, Tax and Discount
        subtotal = no_of_Tshirts * 500 + no_of_Trousers * 1500 + no_of_Shoes * 5000 + no_of_Jacket * 2500
        tax = subtotal * 0.18
        discount = 0
        shoes_discount = 0   ## Calculate Shoe Discount
        jacket_discount = 0  ## Calculate Jacket discount
        
        """ Discount will be applied on Shoes if the customer purchase 1 or more number of shoes.
            If number of shoes is 0, no discount will be given """
        if ( no_of_Shoes > 0 ):
            shoes_discount = 0.1 * (no_of_Shoes * 5000)
            discount = discount + shoes_discount
            print( discount )
            
        """ If number of T-shirts purchased is 2 or more, discount will be applied on Jacket.
            1. Divide the number of T-shirts by 2 and get the int value for the same to avoid any decimal values.
            2. If number of T-shirts purchased is 2, 50% discount will be apllied on purchase of 1 Jacket. """
        if ( no_of_Tshirts >= 2 ):
            discount_on_tshirts = int(no_of_Tshirts/2)
            discounted_Jackets = min( no_of_Jacket , discount_on_tshirts ) 
            jacket_discount = 0.5 * ( discounted_Jackets * 2500 )
            discount = discount * jacket_discount
            print( discount ) 
            
        ## Calculate Total after adding Tax and reducing discounted amount
        Total = subtotal + tax - discount
        result['Subtotal: Rs.'] =  subtotal
        result['Tax: Rs.'] =  tax
        if ( shoes_discount > 0 ):
            result['10% off on Shoes: Rs.'] = shoes_discount
        if ( jacket_discount > 0 ):
            result['50% off on Jacket: Rs.'] = jacket_discount
        result['Total'] = Total
        
        ## Create API
        return json.dumps(result) , 200 , {'content-type':'application/json',}


if __name__ == '__main__':
    app.run(host = IPAddr , port = 5001);





