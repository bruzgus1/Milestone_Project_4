# Eatery Restaurant Website

[View the live project here.]()

This websites purpose is to showcase our menu to those wondering if they should eat at your establishment and if they wish to create a reservation so they don't have to wait for a table to free up and could be seated as soon as they arrive

**User Goals:**

- To see what kind og dishes our restaurant has to offer
- To be able to freely navigate the website
- to make a reservation

**Site Owner Goals:**

- To inform the user of the menu
- to help the user find what they are looking for
- to be able to accept and quickly manage reservations

![how the website looks on diffrent devices](/static/img/am-i-responsive.png)

- **Wireframes**
    - Home Page Wireframe - [View](/static/img/home.png)
    - Reservations Wireframe - [View](/static/img/reservations.png)
    - Make A Reservations Wireframe - [View](/static/img/make%20a%20reservation.png)


## Model Relationship Diagram

This is an updated version based on my mentors suggestions and feedback, the original one
was a bit different

![Model Relationship Diagram](/static/img/entity-relationship-diagram.png)

## Features

1. Home Page
    - Has our menu highlights
    - Reasons why you should eat at our establishment 
2. Make A reservation Page
    - Has a form to make a reservation
    - If applicable a list of dates when a reservation can't be made
    - A warning on what could cause the form to not be submitted 
3. Reservations Page
    - A list of the reservations you have created
    - Ability to edit the reservations you have created
    - Ability to delete the reservations you have created
    - A warning on what restrictions you have when editing a reservation
4. Edit Reservation Page
    - Has a form to edit a reservation
    - If applicable a list of dates when a reservation can't be made
    - A warning on what restrictions you have when editing a reservation

## Future Features

1. Automatically delete reservations that already happened so the page admin doesn't have to do it manually
2. Display a div with some text when there are no reservations so the page looks more clean (ran out of time to implement it)
3. Instead of username to make reservations, add First Name/Last Name input fields and the validation needed to make them work
4. In admin panel sort the reservations by date not by username
5. Ask the user if He/She really wants to delete a reservation


## Bugs

No Bugs were found, everything works as intended

## Console Errors

- When checking the console on Brave Browser the console gives an error, that does not happen on other browsers or in a private browser window, it's a Browser specific error and it happens on almost every website, that error is not part of my code

![Console Error](/static/img/error.png)

## Automated Testing

- Each page of the site was evaluated using Lighthouse to assess them on four metrics; Performance, Accessibility, Best Practices & Search Engine Optimization (SEO).

![lighthouse scores screenshot](/static/img/lighthouse-scores.png)

## Manual Testing

1. Tried to change the reservation under field that is read only
2. Tried to set a reservation in the past
3. Tried to give a negative number in the (guests) input
4. Tried to give a larger number in the (guests) input then specified
5. Tried to write my own reservation time instead of choosing one of the options
6. Tried to make a reservation when I wasn't logged in
7. Checked the website on different browsers (Safari, Chrome, Brave Browser)
8. Checked the website on different devices (PCs, Macbook, Different Iphone Models, Android Phones)


## Validation Testing

- PEP8 - no errors besides settings.py file line to long errors.
- W3C - HTML validation no errors were found.
- W3C - CSS validation no errors were found.

## Deployment

- Set the Debug Flag to False
- Set up Procfile
- Pushed the final code to github
- Create a new Heroku app.
- Set up my Config Vars
- Set up my database
- Link the Heroku app to repository.
- Click on **Deploy**.

## Content

- All images and dish descriptions were taken from google

## Plagiarism

- Parts of the code was taken from Django Blog Walkthrough Project as it was what I needed
- Some was taken from StackOverFlow questions that were relevant to me and edited to fit my project
- The CSS came with the template I was using and so I wouldn't have to do much designing, you can find the template [Here](https://github.com/StartBootstrap/startbootstrap-clean-blog/)


## Credits
- Code Institute Tutor Support - The best help anyone could ask for.
- Stack OverFlow - How do people create anything without using this is beyond me
- My Mentor.