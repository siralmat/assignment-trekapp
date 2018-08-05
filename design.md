# Design patterns
## Architecture: Model View Controller
The assignment goal was to create an application that would be converted to a mobile app by another team of developers. The converted app would presumably require an entirely new user interface, with little being reused from the original UI. With that in mind, I aimed to keep the bulk of application code uncoupled to the view to maximise reusability.

The general approach I used to determine the responsibilities of each component:

* The model is the base of the application and encompasses entity representation, data storage, and resource control (e.g. communicating with servers).
* The controller acts as a Strategy for the view, determining how to respond to high level events like "load a file" or "start navigation". It exposes interactions with the model to the view.
* The view translates user input into events, which are passed to the controller. The view listens to model updates and uses the update information to redraw itself.

An alternative design I considered was to move all model interactions and logic out of the view and into the controller, creating a [passive view](https://martinfowler.com/eaaDev/PassiveScreen.html). Minimising view logic benefits testability and maximises reusability, as essential logic such like state transition is not tied as closely to the view implementation.

I found this was a difficult design to approach with Qt, which is built around a [Model/View](https://doc.qt.io/qt-5/model-view-programming.html) pattern. Many of Qt's features work best when following this pattern, and my final design ended up with a good deal of logic in the view component.

## Routes: Composite pattern
**Routes** are constructed as composites of **Segments** and **SubrouteSegments**. Segments are equivalent to leaves, storing information about a section on a route such as the distance and start/end points. SubrouteSegments inherit from Segment and adding logic to traverse inside another route. The parent routes don't know whether a particular segment points to a subroute or not. When constructing a generator, the route calls `yield from` on its segments: normal segments will yield themselves, and subroute segments will silently hand over to the subroute generator.

One issue this poses is that the waypoint indicating the start of a subroute may only _roughly_ correspond with the actual subroute's starting location (within 10m horizontally and 2m vertically). The original starting location is stored in the SubrouteSegment but ignored. I felt that this was a valid interpretation of the specification, but in a practical application this might be an unacceptable loss of precision.

Another issue is that all subroute segments are treated as if they are part of the parent route. It might be valuable to know whether or not a segment is part of a subroute, and the current implementation of route traversal does not make this information accessible.

## Route parsing: Factory method pattern
Routes are generated from raw text through **RouteParser**. The parser delegates each step of the route building process to a separate method:

* `splitChunks()`: Split data into chunks representing each route
* `buildRoutes()`: Search each chunk for subroutes/dependencies and ensure they are processed in order (route created only if all subroutes created)
* `buildRoute()`: Split a route chunk into segments
* `buildSegment()`: Create a segment from start/end coordinates and description
* `buildWaypoint()`: Build waypoints for the start and end of each segment

By placing all object creation in RouteParser, the rest of the program is disconnected from the specific details of route construction. If the route format changes, only the parser needs to be updated.

## Model/view communication: Observer pattern
There are two areas of the system where changes may occur during runtime:

* Loading/reloading routes in a RouteCollection
* Updating position on a route with a Tracker

Both of these events must be communicated to the view as soon as they happen, so it was a natural fit for the Observer pattern. The pattern is implemented with an **Observable** class that RouteCollection and Tracker inherit from. Views can register callbacks on Observables and associate them with an event name. When an event occurs, all registered callbacks are executed with an optional list of arguments.

Because Observable uses callbacks, observers do not need to implement a predefined interface. Callbacks are stored with weak references so should be gracefully removed when an observer is destroyed.

The Observable class is generic and does not define any specific events or arguments (except for the default 'ALL' event name). Available events and their arguments are listed in class documentation.