# FRONTEND (index.html)

1)The title is "Image Classifier".

2)I created a form with a file type button which will upload the image from your local repository.

3)Then I have created another <div> for the predict button which should be visible after the image is uploaded.

4)Then comes another two buttons for review as satisfied or not-satisfied which should be visible after getting the prediction results.

5)Then comes the Try again button which should be visisble after the review from the users.

6)Then comes the <span> tags for displaying the Results and reviews.


# FRONTEND (base.html)

1)This page is the extensionfor the index.html page and the title is Image Prediction".

2)Then we will link the css styles for the webpage.

3)Then we will link the script for Jquery.

4)Then I will give the navigation bar as "Predicting an image of daily used things" along with a help button.

5)Inside the script we will attach the clent side validation in form of Jquery.

6)I have hidden all the buttons except choose.

7)Once the image is uploaded and the function changes I will show the predict button.

8)On click predict button the uploaded file should go to the @app./predict route function in python file.

9)The returned value from the predict function is printed is printed and the satisfication buttons are made visisble.

10)On click satisfied button it should return "Thanks for the review" and the pic should be saved in satisfied folder.

11)On click Not satisfied button is should return some "...some message " and the pic should be saved in unsatisfied folder.

12) If we click any of the above two buttons we need to show the Try again buttion which will reload the page.




#BACKEND(app.py)

