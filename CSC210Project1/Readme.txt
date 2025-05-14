CSC210
Project1

Wenbo Zhang
wzhang66@u.rochester.edu

How to Run:
Change directory to the repository on your local machine.
Install the required dependencies by running pip install -r requirements.txt from the root directory of the project.
Command: python3 app.py
1. Access the application through your web browser at http://127.0.0.1:5000/login
2. Once logged in, you can add new products by navigating to http://127.0.0.1:5000/add-product.
3. View all products by navigating to http://127.0.0.1:5000/products.
4. Click on a product to view its details, including the user who added it.

Features in this project:
You can create multiple accounts in this website. However, you can only logged into your account when your username and password match. All passwords
are hashed and stored in db so safety is secured.
Once you logged in, you can hit the button "Go to Products List". Then you may see all products listed. There could be products from other merchants, 
and there could be products from you if you ever added a new product before. If not, you can hit "Add a New Product", and then you can input your product's
name, description and price. 
You can hit the "Delete" and delete the items that only were added by yourself. You can't have any action on other merchants' goods.
You can see all users' email once you hit "List all users email".

I already have several users and product in my database.
Username: wzhang66
Password: 0000

Username: forestzhang001
Password: 8888

You can logged into those accounts and see how it work, or you are welcomed to create your own account and try to manage your own items!

I already used validations for all three type of languages and all passed the test. 

