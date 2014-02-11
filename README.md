a3-jasnyder-zorahf
==================

## Team Members

1. Jeff Snyder jasnyder@uw.edu
2. Zorah Fung zorahf@uw.edu

## United States Migration Explorer


The United States Migration Explorer uses 2012 American Community Survey data to allow you to explore migration patterns to and from states in the US.

The map is colored in seven quantiles. In "source mode", by selecting a state or country, the user can see migration patterns from that region, or what state people born in the selected region currently live in. In this mode, states are colored by the ratio of (immigrants to that state from the selected region) / (that state's total population). Darker colors signify a higher ratio. 

In "destination mode", by selecting a state, the user can see migration patterns to that state, or what state or country residents of the selected state were born in. In this mode, regions are colored by the ratio of (emigrants from that region to the selected state) / (the selected state's total population). Again, darker colors signify a higher ratio. 

A toggle button switches modes. For both modes, we provide details on demand by hovering. The map can be zoomed and translated via mouse clicks and drags.

## Running Instructions

Access our visualization at http://cse512-14w.github.io/a3-jasnyder-zorahf/ or download this repository and run `python -m SimpleHTTPServer 9000` and access this from http://localhost:9000/.

## Story Board

[Storyboard pdf here](storyboard.pdf?raw=true). 

### Changes between Storyboard and the Final Implementation

As it turns out, our original idea was a bit more work than we anticipated (surprise!), epsecially given that we were not very familiar with d3 and javascript. Not only was the animation execessively complex to implement, displaying connecting lines between source and destination locations made the map extremely cluttered and hard to read -- our graph of connections is extremely dense! Using dots to represent individuals would have cluttered the screen even more, especially given that our original data has 15,000,000 rows. Therefore, we decided to change our mapping to a chloropleth color mapping. We originally mapped color to the raw number of people that migrated from source to destination. However, this displayed the uninteresting trend that larger states have more immigrants. Therefore, we changed to a ratio representation, where the value of the color scale represented the percentage of residents of a given state from the selected country. We believe that this highlights many interesting trends. Try it out and see for yourself!

## Development Process

Every part of the process took longer than we originally aniticipated. We spent a long time selecting and trimming our data set, brainstorming different questions that users might ask, and iterating through visualization ideas until we settled on a final storyboard. We then spent few hours more hours sifting through examples of geographic d3 visualizations, both to use as a base, as well as to give ourselves an idea of the range of possibilities. While developing the visualization itself, we coded and updated our data in parallel. Most of our time (many, many hours) was sunk into reformatting or modifying imperfect data, much of which had to be done either programmatically or manually. We worked through all of our problems together as a pair (rather than separately in parallel) from start to finish. Overall, we spent perhaps 40 man-hours dealing with data issues and 30 man-hours coding.
