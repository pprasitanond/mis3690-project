# Node: A Note Taking App 
## Description
Node is a simple note taking app that allows users to create a profile and use it to take notes. Each of these notes can be viewed on a user page.  The notes allow for a title of each note, as well as a timestamp of when the note was created. 

## Required Dependencies
*Library listed first, specific modules needed to run Node listed second*
1. **flask**: Flask, render_template, request, session, logging, url_for, redirect, flash
2. **sqlalchemy**: create_engine
3. **sqlalchemy.orm**: scoped_session, sessionmaker
4. **passlib.hash**: sha256_crypt
5. **wtforms**: StringField, PasswordField, SubmitField
6. **flask_wtf**: FlaskForm
7. **wtforms.validators**: InputRequired, Length, EqualTo, ValidationError

## Directions for Running Node on Local Device
1. The first thing that needs to be done is to create a local database on your computer in MySql in order to store the log in and note information. This requires first downloading the MySql Workbench from this [link](https://dev.mysql.com/downloads/workbench/). One *database* needs to be built which can be titled whatever you see fit. Two *tables* need to be built, one titled **users** and one titled **notes**. In the **users** table there needs to be one primary key called **user_id** with variable type INT, make sure to make it *unique* as well as *not null*. There needs to be 3 other columns called **name**, **username**, and **password**, each with varible type VARCHAR. In the **notes** table, there needs to be one primary key called **note_id** with variable type INT, make sure to make it *unique* as well as *not null*. There needs to be 4 other columns, 3 of them being **note_title**, **timestamp**, and **note**, each with variable type VARCHAR. The 4th column needs to be **user_id** as a foreign key from the **users** table. 

2. After the database is built correctly with all the names being exactly as above, the next step is to link the database into the *app.py* file. In line 7, the code starts with "engine = create_engine()". Inside the parentheses the format of the code needs to be: dialect+driver://username:password@host:port/database. Fill in the information and this will hook up the database to the app. 

3. After all of these steps are followed, run the app.py file through either the terminal or command prompt using this following command: 
 <br/>step 1:  **export FLASK_ENV=development** 
 <br/>step 2: **flask run**
<br/>Then follow the link to the URL and start taking notes!

## Directions for Running Node on the Cloud
1. Simply follow the URL for the application : https://nodetaking.herokuapp.com/ and start taking notes!


