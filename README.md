# Introduction 
Accepts POST and HEAD requests. POST Requests with and URI will render a XML Reponse with the CURRI instructions to play the annoucment with same name that is passed to the URI.

HEAD Requests are just for the keep alives that Cisco Communications Manager sends to check if the ECC URL is up or not.

# Example

https://localhost/MonitoringWarning_00055  will render an XML file that instructs the UCM to play an announcement with the name "MonitoringWarning_00055"

# HyeTech Networks
Designed by Jeff Metcalf 06/24/2021