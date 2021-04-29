# Rasa-Bot
## Sample Flows
### Flow 1: Booking an AC room at an allowed time

Step 1

User: I want to reserve a table

Bot: How many seats would you like to reserve

Step 2

User: 2 seats

Bot: Which section would you like to book

AC
Non-AC
Step 3

User: (Clicks on Button 1)

Bot: When would you like to book a reservation? (We are only open from 7pm to 10pm)

Step 4 (Assuminig conversation time is 7:10pm)

User: In half an hour

Bot: You have reserved 2 seats in our AC section for 7:30pm. Thanks!

### Flow 2: Booking a Non-AC room at a disallowed time

Step 1+2

User: I want to reserve a table for a party of 4

Bot: Which section would you like to book

AC
Non-AC
Step 3

User: (Clicks on Button 2)

Bot: When would you like to book a reservation? (We are only open from 7pm to 10pm)

Step 4 (Assuminig conversation time is 5pm)

User: In half an hour

Bot: We are not open at that time. We are only open from 7pm to 10pm

Bot: When would you like to book a reservation? (We are only open from 7pm to 10pm)

User: 7:30 pm

Bot: You have reserved 4 seats in our Non-AC section for 7:30pm. Thanks!
