# TrekApp: Python/PyQt5 OO assignment
![assets/trekapp-logo.png]
This repository is a copy of my assignment submission for Object Oriented Software Engineering (S1 2018):

> Design and implement an app for use by trekkers and climbers to view possible routes, and track their progress through them.
> For this assignment, this can just be either a console application (or a GUI app if you wish), ready to be converted into a mobile app by someone else once you’re finished.

The aim was to demonstrate good use of the design patterns taught in the unit. Read my [design justification](design.md) for an overview of the main patterns.

Functionality:

* load and parse route data from file
* view route information and select a route for tracking
* show current position/distance to next target
* update location via user input or GPS coordinates

Implementation of live GPS updates, downloading routes from server, and distance calculation weren't required for the assignment. Test versions were created with fake data (`gpslocator` & `geoutils`).

Final mark: 97.5%

## Running the program
```sh
pip install -r requirements.txt
./trekapp.py
```

The initial routes are loaded from `sampleroutes.txt`, but new routes can be loaded from the tools menu. GPS coordinates are read from `coords.txt` and passed to the tracker 2s apart. The coords just walk through the main route to confirm that GPS updates are correctly handled.

## GUI
The GUI was implemented with PyQt5. The original Qt Creator .ui files are under `qt` and the makefile in the main directory converts them to Python using `pyuic5`.

## Credits
Logo font: _Final Frontier Old Style_ by Allen R. Walden. Generated at <https://fontmeme.com/star-trek-font/>.

Go icon: made by Retinaicons from www.flaticon.com. <https://www.flaticon.com/free-icon/go_204098#term=go&page=1&position=80>