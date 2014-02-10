a3-jasnyder-zorahf
==================

## Team Members

1. Jeff Snyder jasnyder@uw.edu
2. Zorah Fung zorahf@uw.edu

## United States Migration Explorer


The United States Migration Explorer uses 2012 census data to allow you to explore migration patterns to and from states
in America.

By clicking on a state or country, a user can see where people from the selected region go from a colored map of destinations. The U.S. map is colored in seven quantiles, based on the ratio of the emigrants from the selected region to the population of the colored state. Darker colors signify a higher ratio. Once a region has been selected, users may hover over individual states to view the numerical representation of the ratio, as well the number of immigrants from the selected region. The map can be zoomed and translated via mouse clicks and drags.

A "mode" button toggles between "source" and "destination" modes. "Source" mode exhibits the behavior described above. "Destination" mode changes the selected region to show where the people currently living in the selected region come from.

## Running Instructions

Access our visualization at http://cse512-14w.github.io/a3-jasnyder-zorahf/ or download this repository and run `python -m SimpleHTTPServer 9000` and access this from http://localhost:9000/.

(If you put your work online, please also write [one-line description and put a link to your final work](http://note.io/1n3u46s) so people can access it directly from CSE512-14W page.)

## Story Board

[Storyboard pdf here](storyboard.pdf?raw=true). 

### Changes between Storyboard and the Final Implementation

As it turns out, our original idea was a bit more work than we anticipated (surprise!), epsecially given that we were not very familiar with d3 and javascript. Not only was the animation more work than we had time to deal with, having connecting lines between source and destination locations made the map extremely clustered and hard to read -- people go lots of different places! Dots to represent people would be even harder to read, especially given so many dots. This lead us to change the connection between regions to be visualized through color, which varies in darkness based on the ratio of people who moved from the source to the destination locations. At an intermediate step, we mapped color to the raw number of people from source to destination, however, this displayed the uninteresting trend that lots of people go to larger states. 

## Development Process

Everything took longer than we originally aniticipated. We spent several picking our data set, brainstorming
different questions based on a variety of attributes of the data, and iterating through visualization ideas until 
we settled on a final storyboard. We then spent few hours more hours sifting through geographic examples to both
give ourselves some base code, as well as give us an idea of what sorts of map visualizations could be created
with d3. While developing the visualization itself, we coded and updated our data somewhat in parallel. Most of our
time (several, several hours) was sunk into reformatting or modifying imperfect data, much of which had to be done manually. We worked through all of our problems together as a pair (rather than separately in parallel) from start to finish.
