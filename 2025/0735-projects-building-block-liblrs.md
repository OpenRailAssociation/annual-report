### Building blocks (libLRS)

Linear referencing systems are used everywhere in the railway industry to describe the network. They hold the specifics of guided transportation and it is trivial to understand how the objects (switches, signals, etc.) are positioned. A coordinate is a simple distance — such as 12+340 – from a milestone on a given track.

It is easy to communicate orally where an object is located, and it seems such a trivial system, that many naive implementations exist across any company working on linear infrastructure.

However, the infrastructure is over a century old and has been developed over time. This means that the data is not always consistent and can be difficult to work with. There is always an exception to the rule, and libLRS provides a solution to this problem by providing a standard format for storing and manipulating linear referencing data.

When we designed libLRS, we wanted to create a simple, efficient and modern library that manages all the small quirks of the network. The development was made for the OSRD project, but we wanted it to be used by anyone having a similar problem.

When we contacted other sub-entities of SNCF Réseau, we noticed an interesting pattern: having defined an exchange format with the library allowed us to give immediately the data to other entities (a simple sharepoint link to the data file, no access to a database through a VPN and credentials that require weeks to obtain). With that file, they could test on the public demonstrator taking a shortcut compared to traditional IT projects. This accelerated the adoption.

In conclusion, the key for a successful adoption to libLRS, much more than the technical aspects, were:

- Data trivial to share
- A demonstrator that requires no setup
- The publication of the library on PyPI and NPM
