# Random-Password-Generator
<h1>✅COMPLETE!</h1>
<h2>Notes:</h2>
<br>
⭐ Post request is used when we are dealing with crucial information, and we don't want hackers to steal from the URL of the website. Because using get request
will show it in the URL.
<br>
⭐ To target any input field from the form in the frontend to the backend, we use name attribute from the form.
<br>
⭐request.form gives you all the details present in the form
<br>
<br>
letters = "letters" in request.form
<br>
⭐this line means we are checking if user clicked on the checkbox having name letters, if user clicked on it then letters boolean variable will contain true otherwise false
<br>
⭐in/not in is a membership operator to check if something (string, int, char, checkbox, etc) is present in another thing (list, form, etc) and it returns true or false accordingly
<br>
⭐to seperate the logic of generating the password, we are making a new function called generate password
<br>
⭐a function has 2 parts; 1 is the function definition, and the other one is function calling, without function calling, function will be ignored by python
<br>
⭐we got all the values of letters (bool), lengths (int), symbols(bool), numbers(bool), which the user entered in the form, and then, passing it into the function calling so that they can be used in the logic of making the password
<br>
⭐generate password function is taking all the inputs from us and giving us the password as the output; that's why we are saying 
password = generate_password(length, letters, numbers, symbols)
<br>
⭐when we see the function call, we go to the function definition, and work on the logic part and make the password and get it out of the function
<br>
⭐the function has the last line which says return password and that means function is giving us password as output
<br>
⭐ return render_template("index.html", password = password)
<br>
⭐this line means we are sending the password to the frontend (index.html)
