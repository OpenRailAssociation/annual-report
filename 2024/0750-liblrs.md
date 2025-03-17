### Library for Linear Reference Systems {.project}

**libLRS is a library to manipulate linear coordinates and convert them from and to geographical coordinates. It helps to localize objects along curves (e.g. signals on a train track).**

The library started as a need for a clean sheet design and a library that focuses on those type of coordinates. There are multiple ad-hoc implementation at SNCF. However there are many little edge cases that those implementation handle differently, which made the integration painful.

The core is written in rust for soundness and performance reasons. Bindings in python and javascript allow to use the library in data processing pipelines and web applications.

So far the library is used on the [OSRD project](https://github.com/OpenRailAssociation/osrd) in the data preparation pipeline (converting infrastructure elements such as switches, signals, reference points… from milestone+offset to geographical coordinates that will be displayed on a map), but also to hold the topology of the rail network for a display on a webpage.

We had some initial discussions with other teams from the railway world (display the exact position of a train car on the platform, help emergency services to reach by car the spot where an intervention is required), but also outside of rail: libLRS could be used to localize amenities (camping sites, shops…) along cycle roads where a distance in kilometers is very relatable to cyclists. However, so far we didn’t hear of an actual adoption of libLRS.

We expect that libLRS will be continue to be used in OSRD for more tasks. We hope also to hear about an adoption by other business units of SNCF and groups from the OpenRail community. We would be very happy to learn about the integration of libLRS in non-railway related projects.

Further information:

* [libLRS on github](https://github.com/OpenRailAssociation/liblrs)
* [Documentation for rust](https://docs.rs/liblrs/latest/liblrs/)
* [Documentation for python](https://pypi.org/project/liblrs-python/)
* [Example how to build the LRS with Swiss rail open data](https://gist.github.com/Tristramg/b3338aaa11dbb5c1ee5882bd270ffd5f)
