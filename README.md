# How do taxi trips relate to train infrastructure?

This is a "fun" project, I.e. there's no killer deadline for it, and it shouldn't take too long.

I'd like to know how we use taxis. This will give us some idea if we can make any policy changes that will reduce emissions, etc.

I have a dataset from CabCharge with details of all the taxi trips that Sydney BVN people have taken. There's something like seven thousand rows in the full dataset. I'm trying to get an even more complete set of data for the Brisbane people as well, that goes back in time even further.

Because I'm getting a better dataset soon, lets not blow up our minds by running on all 7k rows. I've included a 200 row sample file as well that will be safer and quicker to work on. (called `200taxis.xlsx`.) It's randomly sampled, so it should throw all the errors that the full dataset will throw!

I've included 3 files: 
1. one that queries the API, pulls the data, and saves it to a json file.
1. and one that read the data, and makes it available for processing.
1. a file that has all the pandas analysis that I've already done on this project.

These files should give you a pretty good starting point for this type of thing I guess. 

I've been using the Google Geocoding API, but I suspect that the [Directions API](https://developers.google.com/maps/documentation/directions/) is more useful. Geocoding just gives an address and coords, whereas directions gives coords of the start and end, but also a travel time.

It looks like you'll need to make 3 requests to get [driving, walking and train times (Google's docs on this)](https://developers.google.com/maps/documentation/directions/intro#TravelModes).
E.g.:

```
https://maps.googleapis.com/maps/api/directions/json?
origin=Clarence+Street,+Sydney+CBD,+New+South+Wales,+2000
&destination=Shipwright+Walk,+Barangaroo,+New+South+Wales,+2000
&key=AIzaSyCCNNwCQCx4yG60KJIFR8xzggoBCCNCnqw
```

gives driving directions for this particularly absurd taxi trip. (`"duration" : {"text" : "1 min",...`)

```
https://maps.googleapis.com/maps/api/directions/json?
origin=Clarence+Street,+Sydney+CBD,+New+South+Wales,+2000
&destination=Shipwright+Walk,+Barangaroo,+New+South+Wales,+2000
&mode=transit
&key=AIzaSyCCNNwCQCx4yG60KJIFR8xzggoBCCNCnqw
```

Public transport: `"duration" : {"text" : "8 mins",...`

```
https://maps.googleapis.com/maps/api/directions/json?
origin=Clarence+Street,+Sydney+CBD,+New+South+Wales,+2000
&destination=Shipwright+Walk,+Barangaroo,+New+South+Wales,+2000
&mode=walking
&key=AIzaSyCCNNwCQCx4yG60KJIFR8xzggoBCCNCnqw
```
Walking `"duration" : {"text" : "2 mins",...`

So, there is a slight possibility that the taxi was faster than walking, but it was 152m, which is pretty absurd. (We can only assume that it was a mistake.)

These three can go in as new columns into the dataset, there's loads of extra data that could go in now, e.g.:

[walk, drive, train, start_lat, start_lon, end_lat, end_lon, walking_distance, etc.]

You can make one request per trip, store the json and then query the json to make those columns (faster, more stable, cheaper)

The API has a tendency to drop out. I'll help you with that, but the general solution is to make sure that even if it gives a bad response that you store the data that you made the request with in the response-file, so that you can go back through it and try it again.

The API is cheap, __but__ if you have it in an inefficient loop, or you run it a lot, it gets un-cheap. Be careful that you have your data in a good format before you send it off, and that you're saving whatever you get back. Also, that API key is my API key and is a licence to spend my money, so don't share this code with people without taking it out first!

I'd imagine that the first stage of this is to modify `make_train_station_coords.py` to hit the directions API based on the _Drop Off_ and _Pick Up_ locations from `200taxis.xlsx`. You'll need to format the strings (with `replace`) so that each space is replaced with a `+`. I'd subset the data even further, down to 3 rows, until you have that bit worked out. You'll also need to be wary of rows that have a pick up of "SUBURBS", or some other non-specific pickup; just ignore those rows.

I've gone on too long, so if you want to talk this through, have a read of the code and give me a ring.

Ben
