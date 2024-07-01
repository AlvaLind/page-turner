## Manual Testing

### General Testing

| Action | Expected results | Yes/No | Comments |
|--------|-----------------|--------|----------|
| Verify that the homepage loads correctly.| The page should load with all elements (logo, navigation bar, featured books). | Yes |  |
| Check the responsiveness on different devices (desktop, tablet, mobile). | The website should change images and styles to accomodate smaller screens | Yes |  |
| Ensure all navigation links work. | All the links should direct to the correct pages. | Yes |  |
| Test the dropdown menus and links within them. | Drop downs like navbar, status update, and filter function should redirect, update and filter. | Yes |  |


## User Testing
| Action | Expected results | Yes/No | Comments |
|--------|-----------------|--------|----------|
|  | Sign Up |  |  |
| Click on "Register" in the navbar. | User should get redirected to Register page. | Yes |  |
| Click on "Create an account now" button in the "Discover banner". | User should get redirected to Register page. | Yes |  |
| Click on "Create account" on Request a Book page. | User should get redirected to Register page. | Yes |  |
| Enter valid username. | Username has to be unique. | Yes |  |
| Enter valid emailadress (optional). | Field will only accept email address format. | Yes |  |
| Enter valid password. | Field will only accept secure passwords, must contain at least 8 characters and it can't be entirely numeric. | Yes |  |
| Enter valid password confirmation. | Field will only accept the same password from the previous field. | Yes |  |
| Click on the Sign Up button. | User should be redirected to the homepage with a confirmation message saying that they are logged in. | Yes |  |
|  | Log in |  |  |
| Click on Login in the navbar| User should get redirected to Login page. | Yes |  |
| Click on "Log in" on Request a Book page. | User should get redirected to Login page. | Yes |  |
| Enter valid username. | Field will only accept a valid username | Yes |  |
| Enter valid password. | Field will only accept a valid password to the username. | Yes |  |
| Click on the Sign In button | User should be redirected to the homepage with a confirmation message saying that they are logged in.| Yes |  |
|  | Log out |  |  |
| Click Log out from navbar| User should get redirected to a log out page to confirm logout. | Yes |  |
| Click "Logout" button in the center of the page. | Redirects user to home page. | Yes |  |
| Click browser back button. | User should still be logged out from the account. | Yes |  |
|  | Navbar |  |  |
| Click on "Home". | User should be taken to the home page. | Yes | Available to everyone. |
| Click on "Books". | User should get taken to the books page. | Yes | Available to everyone. |
| Click on "Request a book". | User should be taken to the "Request a book" page. If user is not logged in the options to login or register an account will appear and redirect the user. | Yes | Only available to registered users. |
| Click on "About us". | User should be taken to the "About us" page. | Yes | Available to everyone. |
| Click on the "search bar". | User should be able to start typing to search for a book or an author. | Yes | Available to everyone. |
| Click on the "user profile" icon. | User should be taken to their user profile and booklist. | Yes | Only available to registered users. |
|  | Books page |  |  |
| Click on "Filter by Genre". | User should be able to filer books by choosing a genre. | Yes | |
| Click on "next". | There should only be 9 books per page. When clicking next user should get redirected to the next page of books. | Yes |  |
| Click on "prev" | The user should get taken back to the previous page of books. | Yes |  |
| Click on a book | User should get taken to the book details page. | Yes |  |
|  | Book details |  |  |
| Click on "Add to Bookshelf". | Book should get added to the users Bookshelf and the button update to "Remove from Bookshelf". | Yes | Only available to registered users. | 
| Click "Remove from Bookshelf". | The book should get removed from the booklist and the button update to "add to bookshelf". | Yes | Only available for registered users. |
| Leave a comment/review | User can leave a comment on the book. | Yes | Only available for registered users. | 
| Click "Submit" to submit the comment. | The text "Your comment has been submitted and is awaiting approval" will appear. The user can then see their pending comment in the comment section. | Yes | Only available for registered users. |
| Click "Edit" button on comment. | The user should be able to edit the comment. If the comment has already been approved the changes will have to await approval. The timestamp of the comment will update. | Yes | Only available for registered users. |
| Click "Delete" button on comment. | There will be a pop-up asking you to verify that the comment should be deleted. | Yes | Only available for registered users. |
| Click "Close" on the pop-up | The pop-up will close and the comment will not be deleted. | Yes | Only available for registered users. |
| Click "delete" on the pop-up. | The comment will be deleted. | Yes | Only available for registered users. |
| Rate the book by clicking on the empty stars. | The stars should get coloured and the average rating of the book update. | Yes | Only available for registered users. |
| Change rating by clicking on the stars again. | The rating and average rating should update. | Yes | Only available for registered users. |
| Clicking the back button. | Takes you back to the previous page. | Yes |  |
| Clicking the back button after submitting a comment/rating or added a book to the bookshelf. | User should be taken back to the previous page without affecting the changes made by the user. | Yes |  |
|  | Request a book |  |  |
| Input title | The field is required and accepts a max length of 60 charachers. | Yes | Only available for registered users. |
| Input Author. | The field is required and accepts a max length of 60 charachers. | Yes | Only available for registered users. |
| Input Published Year. | The field is required and only accepts numeric values. | Yes | Only available for registered users. |
| Input Discription. | This field is not required. | Yes | Only available for registered users. |
| Click "Submit". | The book request gets submitted and a message saying "Thank you for your book recommendation!" | Yes | Only available for registered users. |
|  | User Profile |  |  |
| Click on "username" field and input new username. | Username will only update if the current password has been entered. | Yes | Only available for Registered Users |
| Click on "First name" field and input a first name. | First name is not required and will only update/register if the current password has been entered. | Yes | Only available for Registered Users |
| Click on "Last name" field and input a last name. | Last name is not required and will only update/register if the current password has been entered. | Yes | Only available for Registered Users |
| Click on "email" field and input/edit the email address. | Email address is not required and will only update/register if the current password has been entered. | Yes | Only available for Registered Users |
| Click on "New password" field and input a new password. | The password will only update if the current password and the confirm password has been entered. | Yes | Only available for Registered Users |
| Click on "Confirm password" field and input/confirm the new password. | The password will only update if the current password and new password field has been entered. | Yes | Only available for Registered Users |
| Click on "Save Changes". | The changes will only be updated if the form and the required fields are valid. | Yes | Only available for Registered Users |
| Click "delete" button. | Redirect to delete profile page. | Yes | Only available for Registered Users |
|  | Bookshelf |  |  |
| Click on "Set status" and pick one of the alternatives. | The status of the book should be updated. | Yes | Only available for Registered Users |
| Click on the book. | User should get redirected t the book details page. | Yes | Only available for Registered Users |
| Click "Remove from Bookshelf". | The book will be removed from the bookshelf. | Yes | Only available for Registered Users |
| Click the back button on book details page. | User should get taken back to the user profile with the changes to the bookshelf. | Yes | Only available for Registered Users |
| Click "Remove Book" button. | The book will be removed from the bookshelf and the message "This book has been removed from your Bookshelf!" will appear. | Yes | Only available for Registered Users |




