## Generated Story 255706069223404498
* greet
    - utter_greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "temp@gasf.com"}
    - slot{"email": "temp@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story 1993277579540566202
* greet
    - utter_greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_ask_for_email_to_send
* send_email{"email": "temp@gasf.com"}
    - slot{"email": "temp@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story 3320800183399695936
* greet
    - utter_greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - utter_ask_for_email_to_send
* send_email{"email": "temp@gasf.com"}
    - slot{"email": "temp@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot
* goodbye
    - utter_goodbye

## Generated Story -4639179087166749998
* greet
    - utter_greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 4963448062290237512
* greet
    - utter_greet
    - utter_ask_howcanhelp
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* inform{"budget": "1000"}
    - slot{"budget": "1000"}
    - action_search_restaurants
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Story_00914561
* greet
    - utter_greet
    - utter_ask_howcanhelp
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - utter_on_it
    - utter_ask_cuisine
* restaurant_search{"cuisine": "indian"}
    - slot{"cuisine": "indian"}
    - utter_ask_price
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

* greet
    - utter_greet
    - utter_ask_howcanhelp
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot