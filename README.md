Introduction:
As part of the capstone project in Module 1 at Purwadhika, students are challenged to design and implement a system using Python, which incorporates the CRUD (Create, Read, Update, Delete) operations. The objective is to put into practice the foundational principles of programming while trying to optimize the effectiveness of the system. In this post, we'll be reviewing a Python-based Library System, assessing its code structure, functionalities, and identifying areas of improvement to enhance its performance and effectiveness.

Understanding the Code:
The Library System project is a simple yet effective demonstration of a CRUD application. The system allows users to perform key operations, such as adding new books to the library (Create), viewing all books or specific book details (Read), borrowing and returning books (Update), and deleting books from the library (Delete). The code is organized into several functions, each of which is responsible for a specific operation.

Create Operation: The create_book function and add_new_book function are responsible for creating and adding new books to the library.
Read Operation: The view_all_books function and view_book_details function allow users to view the details of all books in the library or a specific book.
Update Operation: The borrow_book and return_book functions facilitate updating the book's status when a user borrows or returns a book.
Delete Operation: The delete_book function enables removing a book from the library.
Recommendations for Improvement:
While the initial implementation is functional and aligns with the CRUD requirement of the capstone project, there are a few areas that can be improved upon:

Use Object-Oriented Programming: Encapsulate the library system into a class to avoid using global variables. This will also make the system more organized and scalable.
Input Validation & Error Handling: Enhance the system’s robustness by adding input validation checks and error handling to avoid crashes due to unexpected user input.
Code Refactoring: Extract repeated logic into separate helper functions to make the code more DRY (Don't Repeat Yourself) and improve readability.
Decomposition of Functions: Break down complex functions into smaller ones, each with a single responsibility. This would improve the code maintainability and readability.
Add More Comments: Enhance the readability of the code by adding comments that provide more context about the function or operation.
In conclusion, it's commendable that the Python-based Library System effectively implements the CRUD operations as part of the capstone project at Purwadhika. However, refining and enhancing code is a continual process. We hope the recommendations provided here help in fine-tuning this project, and also serve as valuable insights for future programming endeavors. Happy coding!
