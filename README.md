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
* **/**
Static html
* **/goals/**
Sequence of goals
* **/goals/<goal_id>/**
Some goal
* **/notes/**
Sequence of notes
* **/notes/<note_id>/**
Some note
* **/schedules/**
Sequence of schedules
* **/schedules/<schedule_id>/**
Some schedule
</br>
**For sequence you can use only GET method.** If want to change some object then use POST method.
**For urls that listed below use only POST method:**
* **/login/**
* **/logout/**
* **/signup/**
