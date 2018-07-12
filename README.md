# Useful Schedule
It's just single page application that you can use as diary, notebook and schedule!

## Usage
### Usage for users
When you want to note your ideas, you can use this application. On main page you will see three buttons: Goals, Notes, Schedules.
If you've touched on a button from set listed abobe then you are seeing list on objects: your goals, your notes, your scheduels.
If you've touched on a object then you can see description the object.

### Usage for Front-end Developers
You can see urls that returns data about objects. All urls returns JSON string unless **/**.
If response was success then you've get :
`{
  status: 'ok',
  some_object_or_sequence: { ... },
}`
In another variant you can get this result:
`{
  status: 'error',
  message: 'message about what is error',
  code: 12
}`
### Only GET
* **/goals/**
Sequence of goals
* **/notes/**
Sequence of notes
### GET and POST
* **/schedules/**
Sequence of schedules
* **/goals/<goal_id>/**
The goal
* **/notes/<note_id>/**
The note
* **/schedules/<schedule_id>/**
The schedule
### Only POST
* **/login/**
Log in
* **/logout/**
Log uot
* **/signup/**
Sign up
