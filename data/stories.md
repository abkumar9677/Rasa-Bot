<!-- Booking stories -->
## Story path 1
* greet
  - utter_greet
* booking
  - utter_enquiry_seat_no
* seat_no
  - utter_enquiry_seat_type
* choose{"seat_type": "Non-AC"}
  - utter_time_book
* schedule_time
  - utter_confirmation
* thank
  - utter_thank

## Story path2
* greet
  - utter_greet
* booking
  - utter_enquiry_seat_no
* seat_no
  - utter_enquiry_seat_type
* choose{"seat_type": "AC"}
  - utter_time_book
* schedule_time
  - utter_confirmation

## Story path 3
* greet
  - utter_greet
* book+seat_no
  - utter_enquiry_seat_type
* choose{"seat_type": "AC"}
  - utter_time_book
* schedule_time
  - utter_confirmation
* thank
  - utter_thank

## Story path 4
* greet
  - utter_greet
* book+seat_no
  - utter_enquiry_seat_type
* choose{"seat_type": "Non-AC"}
  - utter_time_book
* schedule_time
  - utter_confirmation
* thank
  - utter_thank


## Story path 5
* greet
  - utter_greet
* book+seat_no+time
  - utter_confirmation
* thank
  - utter_thank
  
## Story path 6
* greet
  - utter_greet
* thank
  - utter_thank
  <!-- FAQ -->
## Story path 7
* open_days
  - action_days
## Story path 9
* special
  - action_special
## Stroy path 10
* cancelreservation
  - action_cancel
## Story path 11
* restauranttimings
  - action_open_time
  <!-- GOODBYE -->

## Story path 12
* goodbye
  - utter_bye

<!-- ## Story path 13
* seat_no
  - utter_enquir -->

## Story path 13
* booking
  - utter_enquiry_seat_no
* seat_no
  - utter_enquiry_seat_type
* choose{"seat_type": "Non-AC"}
  - utter_time_book
* schedule_time
  - utter_confirmation
* thank
  - utter_thank

## Story path 15
* book+seat_no+time
  - utter_confirmation
* thank
  - utter_thank

## Story path 16
* book+seat_no
  - utter_enquiry_seat_type
* choose{"seat_type": "Non-AC"}
  - utter_time_book
* schedule_time
  - utter_confirmation
* thank
  - utter_thank