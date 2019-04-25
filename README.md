# FRONTEND (index.html)

1)The title is "Image Classifier".

2)I created a form with a file type button which will upload the image from your local repository.

3)Then I have created another div tag for the predict button which should be visible after the image is uploaded.

4)Then comes another two buttons for review as satisfied or not-satisfied which should be visible after getting the prediction results.

5)Then comes the Try again button which should be visisble after the review from the users.

6)Then comes the span tags for displaying the Results and reviews.


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




# BACKEND(app.py)

1)We need to import all the packages that are required during the preparation of our model.You can either buid your own model (or) Import the alreday trained models from keras  (or) Train with your features with the already imported  model.You can save your model any time and load it to make predictions.

2)You need to define a flask app to make use of the flask properties.

3)I am using the already trained model ResNet50 which we can import as "from keras.applications.resnet50 import ResNet50".

4)Then I have created a function model_predict() which will load a particular image from the path(which we need to provide as argument along with the model we are using)preprocess the image in such a way that we can directly pass the value and predict the outcomes.

5)Once we have the outcomes in our desired format we can return them as the RETURN value for the model_predict().

6)I have a created a flask app.route(/) with GET method which will return my FRONTEND(index.html) as return value from my index().

7)I have a created a flask app.route(/predict) with GET,POST methods which will take the image  and store it in the desired path and call the model_predict() with that specific path and decode the predictions along with their labels and propabailities and store the desired output into a variable and return that to my FRONTEND(index.html) as return value from my model_predict().

8)I have a created a flask app.route(/satisfy) with GET,POST methods which will take the image and store it in the satisfied directory if the user clicks the satisfied button in the frontend page.

9)I have a created a flask app.route(/notsatisfy) with GET,POST methods which will take the image and store it in the unsatisfied directory if the user clicks the not-satisfied button in the frontend page.

 


