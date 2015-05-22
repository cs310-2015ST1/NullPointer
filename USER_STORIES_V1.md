===================================================================================================================================================
1. As a visiting tourist to Vancouver, I would like to see the website displaying a map of Vancouver with all the notable locations highlighted on the map.

notes: notable locations include parks, beaches, heritage sites, and sites useful to a potential visitor such as parking, water fountains, and restaurants.

Definitions of done:
- Displays a map of vancouver on the website layout
- Test calls to database returns list of data (i.e.: doesn't return an empty object)
- parser to parse the list of data into a usable format
- Plots locations around vancouver on map

Tasks: 
- implement map layout with Google Maps API
- write httprequest to call databases and return data
- build parser to parse list of data into usable format
- write functions to plot returned data onto Map
- update HTML/CSS

ETC: ~24 hours
===================================================================================================================================================
2. As a user, I would like to be able to click on the notable locations hightlighted on the map, and get descriptions pertaining to the location displayed.

notes: display may be in dialogue box, or popup, or as a textbox next to the location marker.

Definitions of done:
- Location markers are clickable.
- User clicks on a location and a dialogue box/popup box/textbox appears.
- the text displayed will be relevant to the marker clicked.
- no textbox will be displayed if a marker is not clicked.


Tasks:
- Write functions in source to allow locations markers to display information once clicked.
- write httprequest to call databases and return data based on place.
- build parser to parse list of data into usable format
- write functions to display returned data about the clicked location.
- intergrate function to display data with function to display information.
- update HTML/CSS

ETC: ~24 hours.
===================================================================================================================================================
3. As a user, I would like to be able to generate places of interest around a certain radius i click in the map and have them plotted onto the map.

Definitions of done:
- user able to click on map and start a search for locations based on place clicked.
- Test calls to database returns list of data (i.e.: doesn't return an empty object)
- write function to display dialog box if radius is too small (i.e.: doesn't return a meaningful list of data ex.: empty)
- parser to parse the list of data into a usable format
- Plots locations of Parks around vancouver on map relevant to where the user clicked.
- write function to draw searched radius on map.
- search by radius function should not interfere with #2 or #4.

Tasks: 
- write function to take user input (mouseclick) and modify httprequest to satisfy the radius requirement. (i.e: generate lat/lon of place clicked, then draw radius around it.)
- write httprequest to call databases and return data
- build parser to parse list of data into usable format
- write functions to plot returned data onto Map
- update HTML/CSS

ETC: ~24 hours
===================================================================================================================================================
4. As a user, I would like to be able to click on the notable locations hightlighted on the map, and get reviews pertaining to the location displayed.

notes: display may be in dialogue box, or popup, or as a textbox next to the location marker.

Definitions of done:
- Location markers are clickable.
- User clicks on a location and a dialogue box/popup box/textbox appears.
- the text displayed will be relevant to the marker clicked.
- no textbox will be displayed if a marker is not clicked.

Tasks:
- Write functions in source to allow locations markers to display information once clicked.
- write httprequest to call databases and return data based on place.
- build parser to parse list of data into usable format
- write functions to display returned data about the clicked location.
- intergrate function to display data with function to display information.
- update HTML/CSS

ETC: ~24 hours.
(note: similar to task 2; perhaps merge?)

