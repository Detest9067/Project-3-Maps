# Project 3 - GeoSpatial Data

## Required Dependencies
* Folium
* Pandas
* JSON
* Requests
* PyMongo

### Overview

This project consists of extracting Geospatial data via the foursquare API and evaluating locations for a new company headquarters for a video game company


### Approach:

For the purpose of this project, I imagined that our company is currently developing a car-racing game. We want to tap into the Formula1 fan network, therefore we will focus on building an office in a country with a racetrack on the F1 schedule. </br></br>
Once we know all the different countries we can choose from, we will look at the corporate tax rates in countries with an F1 circuit to decide where will build our new headquarters

### Data Sourcing/Wrangling

**STEP 1:** Via RapidAPI, connect to [F1 API](https://rapidapi.com/sportcontentapi/api/f1-live-motorsport-data) to extract all of the current (data set is from 2020) tracks on the F1 calendar</br>
**STEP 2** Download current Corporate tax-rates from the [Tax Foundation](https://taxfoundation.org/publications/corporate-tax-rates-around-the-world/) website</br>
**STEP 3** Combine the data sets to give us a picture of what the tax rate is per country with a F1 Circuit</br>
**STEP 4** Decide on a country (in this case, Singapore), and use the [Foursquare API](https://location.foursquare.com/developer/reference/places-api-overview) and to look for the ideal area in the city based off the employee criteria.

### Decision Criteria
* Close proximity to one/many Starbucks
* Abundance of schools for new/young families
* Close to a large airport for executive travel
* Basketball hoops nearby for our maintenance guy

### A look at the data

![Alt text](image.png)

As you can see, Bahrain is the clear cheapest option with a tax rate of 0%, with Hungary in 2nd place with a rate of 9%, and Singapore in 3rd with a rate of 17%. 

Next we take a look at this [trusty website](https://www.ura.gov.sg/maps/), which provides data about the zoning of Singapore


As you can see in the map, the Eastern/Western parts of Singapore are all a nice color of burgendy-esque red. This means they're zoned for business.

Now we use the Foursquare API to do some searching around Singapore, based off the decision criteria from above. 


