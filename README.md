# Shopping_Cart

1. Install Postman to interact with API of shopping cart
   https://www.postman.com/downloads/
   
2. The code creates an API which accepts POST data consiting of list of products purchased by customers.

Test cases:
Note: Please find the screenshot of all Test cases uploaded to the repo.

Test case 1


-  No.of T-shirts 2 , Jackets 1, Shoes 1

Input-{
    "products":["T-shirt","T-shirt","Jacket","Shoes"]
}
Output-{
    "Subtotal: Rs.": 8500,
    "Tax: Rs.": 1530.0,
    "10% off on Shoes: Rs.": 500.0,
    "50% off on Jacket: Rs.": 1250.0,
    "Total": 8280.0
}

=================================================================================================================
Test case 2


-  No.of T-shirts 1 , Trousers 1

Input-{
    "products":["T-shirt","Trousers"]
}
Output-{
    "Subtotal: Rs.": 2000,
    "Tax: Rs.": 360.0,
    "Total": 2360.0
}

=================================================================================================================
Test case 3


-  No.of T-shirts 2 , Jackets 2 Trousers 1
Though the number of jackets  are 2 , discount will be applicable only on one Jacket beacuse customer has only purchased 2 Tshirts.
Input-{
    "products":["T-shirt","T-shirt","Jacket","Jacket","Trousers"]
}
Output-{
    "Subtotal: Rs.": 7500,
    "Tax: Rs.": 1350.0,
    "50% off on Jacket: Rs.": 1250.0,
    "Total": 7600.0
}


================================================================================================================
Test case 4


- No of T-shirts 4 , Jacket 2, Shoes 1
Offer applicable on both the Jackets as User purchased 4 T-shirts. ALso, discount will be applicable for Shoes as well.

Input - {
    "products":["T-shirt","T-shirt","T-shirt","T-shirt","Jacket","Jacket","Shoes"]
}

Output -{
    "Subtotal: Rs.": 12000,
    "Tax: Rs.": 2160.0,
    "10% off on Shoes: Rs.": 500.0,
    "50% off on Jacket: Rs.": 2500.0,
    "Total": 11160.0
}

===================================================================================================================
Test case 5


- No of T-shirts 1 , Jacket 2
No discount applicable as number of T-shirts purchased is less than 2

Input - {
    "products":["T-shirt","Jacket","Jacket"]
}

Output -{
    "Subtotal: Rs.": 5500,
    "Tax: Rs.": 990.0,
    "Total": 6490.0
}



