# Flask-Madlibs-Exercise
Using Flask and Jinja create a madlibs mini-machine which generates a story based on the input values
## **Challenge**

Write a Flask app that imports the example story. Add a homepage for the application that shows a form prompting you for all the words in the story:
**Don’t hardcode this, though** — you want your form route to be able to ask for all of the questions required by the story, not for it to have a hard-coded form of asking these exact questions!

Add a route, ***/story***, that shows the resulting story for those answers, like this:

![story.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/25976165-e160-4458-9d2d-a32e0f42dfcf/story.png)

For now, don’t worry about having template inheritance or a ***base.html*** — later, in further study, you can refactor this to use template inheritance.

## **Further Study**

### **Use Template Inheritance**

Make a ***base.html*** template of common parts of your templates (like the ***<html>***, ***<body>***, and other common things, and change your templates so they inherit from this base template.
