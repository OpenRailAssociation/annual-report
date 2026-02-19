## How OpenRail Drives Impact

### Open Source in Production

Since 2023, OSRD has been operational at SNCF Réseau, proving that open-source software can support critical railway infrastructure management. With around **100 active users**, OSRD addresses diverse needs: **timetabling, operational studies, infrastructure management, and short-term capacity planning**. The platform offers a modern, web-based tool for collaborative timetable creation, integrating **both macroscopic and microscopic railway data**. This unified approach bridges high-level planning and detailed operational analysis, replacing outdated methods with a seamless, comprehensive solution.

The short-term capacity management module serves multiple railway companies. Users search daily for available train paths within France’s residual network capacity. When OSRD identifies viable options, requests are forwarded to SNCF Réseau’s validation and ordering tools. This accelerates processes by avoiding impossible requests and suggesting alternative options, enabling more trains to run on the network.

OSRD’s success in production stems from its **customizable integrations**. SNCF Réseau developed private connectors to process internal data before feeding it into OSRD, while the `railway_manager_interface` supports specific organization operations, such as importing proprietary timetable formats and exporting schedules to private IT systems. This flexibility demonstrates how open-source projects can integrate smoothly into complex enterprise environments without sacrificing specialized requirements.

Beyond operational gains, OSRD’s open-source model advances a strategic goal: creating a **standard platform** for **European-scale timetable collaboration**. Since many features requested by SNCF Réseau align with broader industry needs, the open development approach ensures improvements benefit all stakeholders, promoting interoperability and reducing redundant efforts across Europe.

At SNCF, OSRD runs on a scalable AWS Kubernetes cluster, using the project’s public Helm chart for efficient orchestration and maintenance. This infrastructure guarantees high availability and performance, essential for supporting a growing user base and intensive simulation requests.

Authentication integrates with SNCF’s internal identity provider, allowing users to access OSRD via their existing SNCF credentials through OpenID Connect. This simplifies onboarding and ensures compliance with security policies. Deployments use SNCF’s internal tools: public Docker images are mirrored internally, and updates are applied via Helm upgrades.

OSRD’s granular roles and permissions system assigns high-level functionalities through roles and fine grained access, such as permissions for specific railway infrastructures to users or groups. This ensures users only access relevant data and tools, matching the level of data protection desired by the company.

To improve accessibility, OSRD is fully localized in French and English, with partial support for German, Dutch, Portuguese, and Spanish. SNCF contributes to ongoing translations via Weblate, an open-source platform. This collaborative effort not only benefits French-speaking teams but also supports OSRD’s mission to enable cross-border railway interoperability.

![Timetabling module, Space Time Diagram, Train List and NGE integration][images/osrd_1.webp]
![Timetabling module, Space Time Diagram][images/osrd_2.webp]
![Timetabling module, NGE integration][images/osrd_3.webp]
