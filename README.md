# django-ecom
## Python version: 3.11

## Instructions to run the Project

1. Goto the directory where you want to store your project.
2. Clone the git repository to the project directory.
3. Open the terminal and navigate to the project directory from the terminal.
4. This project dependencies managed by PDM https://pdm.fming.dev
    * If you don't have `PDM` installed then install it by typing `pip install --user pdm`.
5. Install the project dependencies by typing `pdm sync` on the terminal.
6. Migrate the database by typing `pdm migrate` on the terminal.
7. Create admin user if you want by typing `pdm createsuperuser` and give the required credentials on the terminal.
8. Now, Run the project from your **localhost** by typing `pdm start`
9. Navigate to the URL [127.0.0.1:8000/api](127.0.0.1:8000/api) or [localhost:8000/api](localhost:8000/api) from your browser.
10. You can terminate the server anytime by **CTRL+c**.

### Here are all the endpoints based on the provided URL configurations:

- For the main project's urls.py file:

  1.Admin site: http://127.0.0.1:8000/admin/
  2.Home page: http://127.0.0.1:8000/
  
- Product-related APIs:
  1. Get all products: http://127.0.0.1:8000/api/products/
  2. User-related APIs:
  3. Get all users: http://127.0.0.1:8000/api/users/
  4. Get user by ID: http://127.0.0.1:8000/api/users/<str:pk>/
  5. Update user by ID: http://127.0.0.1:8000/api/users/update/<str:pk>/
  6. Delete user by ID: http://127.0.0.1:8000/api/users/delete/<str:pk>/
  
- Order-related APIs:
  1. Get all orders: http://127.0.0.1:8000/api/orders/
  2. Add order items: http://127.0.0.1:8000/api/orders/add/
  3. Get logged-in user's orders: http://127.0.0.1:8000/api/orders/myorders/
  4. Update order status to "delivered" by order ID: http://127.0.0.1:8000/api/orders/<str:pk>/deliver/
  5. Get order by ID: http://127.0.0.1:8000/api/orders/<str:pk>/
  6. Update order status to "paid" by order ID: http://127.0.0.1:8000/api/orders/<str:pk>/pay/
  
- For the base.urls.product_urls file:
  1. Get all products: http://127.0.0.1:8000/
  2. Create a product: http://127.0.0.1:8000/create/
  3. Upload an image: http://127.0.0.1:8000/upload/
  4. Create a review for a product: http://127.0.0.1:8000/<str:pk>/reviews/
  5. Get top products: http://127.0.0.1:8000/top/
  6. Get product by ID: http://127.0.0.1:8000/<str:pk>/
  7. Update product by ID: http://127.0.0.1:8000/update/<str:pk>/
  8. Delete product by ID: http://127.0.0.1:8000/delete/<str:pk>/

- For the base.urls.user_urls file:

    - User authentication:
        1. Obtain user token: http://127.0.0.1:8000/login/
        2. User registration: http://127.0.0.1:8000/register/
- User profile:
   1. Get logged-in user's profile: http://127.0.0.1:8000/profile/
   2. Update logged-in user's profile: http://127.0.0.1:8000/profile/update/
- User-related APIs:
   1. Get all users: http://127.0.0.1:8000/
   2. Get user by ID: http://127.0.0.1:8000/<str:pk>/
   3. Update user by ID: http://127.0.0.1:8000/update/<str:pk>/
   4. Delete user by ID: http://127.0.0.1:8000/delete/<str:pk>/
### Note: The provided URLs assume the local development server is running on http://127.0.0.1:8000/. Make sure to replace it with the appropriate URL if you are hosting the project on a different server or domain.

