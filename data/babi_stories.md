<!-- good bye stories -->
## Generated Story -277470545592324679
* goodbye
    - utter_goodbye
    - action_restart_bot

## Generated Story -277470545592325679
* goodbye
    - utter_goodbye
    - action_restart_bot
    - action_restart_bot

## Generated Story -277470545592327679
* goodbye
    - utter_goodbye
    - action_restart_bot

## Generated Story -277470545592328679
* goodbye
    - utter_goodbye
    - action_restart_bot

## Generated Story -277470545592329679
* goodbye
    - utter_goodbye
    - action_restart_bot

## Generated Story -277470545592323679
* goodbye
    - utter_goodbye
    - action_restart_bot

<!-- good bye stories -->


<!-- deny stories -->
## Generated Story -277470145592323679
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story -277470245592323679
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story -277470345592323679
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story -277470445592323679
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story -277470645592323679
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story -277470745592323679
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story -277470845592323679
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story -277470945592323679
* deny
    - utter_no_email_sent
    - action_restart_bot
<!-- deny stories -->


<!-- stories starting with only bare restaurant_search with complete restaurant_search and email -->
## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story 2732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "kanpur"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story 3732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "jaipur"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story 4732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot
<!-- stories starting with only bare restaurant_search with complete restaurant_search and email -->

<!-- stories starting with only bare restaurant_search with complete restaurant_search and no email -->
## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

<!-- stories starting with only bare restaurant_search with complete restaurant_search and no email -->





<!-- stories starting with location restaurant_search with complete restaurant_search and sent email -->
## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Amritsar"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Nagpur"}
    - slot{"location": "Nagpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Nagpur"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "699"}
    - slot{"budget": "699"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot
<!-- stories starting with location restaurant_search with complete restaurant_search and sent email -->


<!-- stories starting with location restaurant_search with complete restaurant_search and no sent email -->
## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Amritsar"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Nagpur"}
    - slot{"location": "Nagpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Nagpur"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "699"}
    - slot{"budget": "699"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot


<!-- stories starting with location restaurant_search with complete restaurant_search and no sent email -->


<!-- stories starting with cuisine restaurant_search with complete restaurant_search and sent email -->

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* send_email{"email": "zjiom@gasf.co.in"}
    - slot{"email": "zjiom@gasf.co.in"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"budget": "701"}
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

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"budget": "699"}
    - slot{"budget": "699"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "Gwalior"}
    - slot{"location": "Gwalior"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Gwalior"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "Surat"}
    - slot{"location": "Surat"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Surat"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot
<!-- stories starting with cuisine restaurant_search with complete restaurant_search and sent email -->

<!-- stories starting with cuisine restaurant_search with complete restaurant_search and no sent email -->

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - utter_ask_price
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"budget": "699"}
    - slot{"budget": "699"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "Gwalior"}
    - slot{"location": "Gwalior"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Gwalior"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "Surat"}
    - slot{"location": "Surat"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Surat"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

<!-- stories starting with cuisine restaurant_search with complete restaurant_search and no sent email -->



<!-- stories starting with cuisine and location restaurant_search, with complete restaurant_search and sent email -->
## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Chandigarh"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Chandigarh"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Chandigarh"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot


## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot


## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Patna"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Patna"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Guwahati"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Guwahati"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Guwahati"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Patna"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Patna"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

<!-- stories starting with cuisine and location restaurant_search, with complete restaurant_search and sent email -->


<!-- stories starting with cuisine and location restaurant_search, with complete restaurant_search and no sent email -->

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story -2126870891193165514
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Bhopal"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bhopal"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Bhopal"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot

## Generated Story -2126870891193165654
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
    - action_restart_bot


## Generated Story -2126870891193165634
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot


## Generated Story -2126870891193165610
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Kozhikode"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kozhikode"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Kozhikode"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot


## Generated Story -2126870891193165613
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai", "location": "mumbai"}
    - slot{"cuisine": "thai"}
    - slot{"location": "mumbai"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
    - action_restart_bot
<!-- stories starting with cuisine and location restaurant_search, with complete restaurant_search and no sent email -->

<!-- misc -->
## Generated Story -277470545592326629
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    - action_restart_bot
    - action_restart_bot

## Generated Story -277470545592326629
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    - action_restart_bot
    - action_restart_bot

## Generated Story -277470545592326629
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    - action_restart_bot
    - action_restart_bot

## Generated Story -277470545592326629
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    - action_restart_bot
    - action_restart_bot

## Generated Story -277470545592326379
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* goodbye
    - utter_goodbye
    - action_restart_bot
    - action_restart_bot

## Generated Story -277470545592326379
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* goodbye
    - utter_goodbye
    - action_restart_bot
    - action_restart_bot

## Generated Story -277470545592326379
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* goodbye
    - utter_goodbye
    - action_restart_bot
    - action_restart_bot

## Generated Story -277470545592326379
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* goodbye
    - utter_goodbye
    - action_restart_bot
    - action_restart_bot

## Generated Story -277470545592326379
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* goodbye
    - utter_goodbye
    - action_restart_bot
    - action_restart_bot


<!-- misc -->
<!-- leave in between -->


## Generated Story -277470545592426679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
    - action_restart_bot
    - action_restart_bot

## Generated Story -277470545592426679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
    - action_restart_bot
    - action_restart_bot

## Generated Story -277470545592426679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
    - action_restart_bot
    - action_restart_bot

## Generated Story -277470545592426679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
    - action_restart_bot
    - action_restart_bot


## Generated Story -277470545595326679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
    - action_restart_bot

## Generated Story -277470545595326679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
    - action_restart_bot

## Generated Story -277470545595326679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
    - action_restart_bot

## Generated Story -277470545595326679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
    - action_restart_bot

## Generated Story -277470545595326679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
    - action_restart_bot

## Generated Story -277470545595326679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
    - action_restart_bot

## Generated Story -277470545595326679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
    - action_restart_bot

## Generated Story -277470545596326679
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - utter_ask_price
* goodbye
    - utter_goodbye
    - action_restart_bot

## Generated Story -277470545792326679
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* goodbye
    - utter_goodbye
    - action_restart_bot

## Generated Story -277470548592326679
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* goodbye
    - utter_goodbye
    - action_restart_bot

## Generated Story -277470545502322679
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
    - action_restart_bot

<!-- leave in between -->




<!-- condition checkpoints -->

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - utter_location_not_found
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - utter_location_not_found
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - utter_location_not_found
* restaurant_search{"location": "Banglaore"}
    - slot{"location": "Banglaore"}
    - utter_location_not_found
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot


## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - utter_location_not_found
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - utter_location_not_found
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - utter_location_not_found
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - utter_location_not_found
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - utter_location_not_found
* restaurant_search{"location": "Nashiqw"}
    - slot{"location": "Nashiqw"}
    - utter_location_not_found
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - utter_location_not_found
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - utter_location_not_found
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - utter_location_not_found
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - utter_ask_price
* restaurant_search{"budget": "399"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot


## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

<!-- all restaurant_search in one go. -->



<!-- starting with budget and location -->

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

<!-- starting with cuisine and budget -->

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ack_dosearch
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "test@hai.com"}
    - slot{"email": "test@hai.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_bot