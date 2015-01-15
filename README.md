# devlol - Landing Page

## Key Facts
* Fancy, clearly structured and easy to understand Homepage
* Quick Access to necessary Information
* A diary system to handle future and past events
* display status

## Diary System
This System should provide an easy and general approach to handle events and or news items on the page.
The Main Model is a ***DiaryItem*** which holds following attributes:

### DiaryItem
* title
* date
* time
* author
* location
* content
* images

***title***, ***date*** and ***time*** should be self-explaining.
***location*** holds all relevant information data (see below)
***content*** holds markdown text which can be parsed to display all kinds of information.
Altough it is possible to include images into markdown it is sometimes necessary to include a bunch of images.
That's why there will be a way to attach multiple images to an event.

###EventLocation
* name
* description
* gps

The Information in the diary then will be made accessible in following views:
#### event
A direct Link to display a certain DiaryItem, which can be included in mails or other media to give users direct access to an events details.

#### calendar
An overview page, displaying all events, upcoming and past in a current months calendar.
With Links to each days subpage.

#### date
A Link for displaying all events on a certain date.

### Optional additions
* Possibility to suggest events in a form, which will be reviewed by an admin
* Integration with devbot
* E-Mail Reminder for events
* ical export
* Publish to Facebook
* Anncounce on Twitter
