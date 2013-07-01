class KML: 
    
    def __init__(self):
        
        self.content = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"\
        "<kml xmlns=\"http://earth.google.com/kml/2.0\">\n"\
        "<Document>\n"\
        "<Style id='normalPlaceMarker'>\n"\
        "  <IconStyle>\n"\
        "    <Icon>\n"\
        "      <href>root://icons/palette-3.png</href>\n"\
        "      <x>96</x>\n"\
        "      <y>160</y>\n"\
        "      <w>32</w>\n"\
        "      <h>32</h>\n"\
        "    </Icon>\n"\
        "  </IconStyle>\n"\
        "</Style>\n"

    def close(self):
        self.content += "</Document>\n"\
        "</kml>"
        
    def addPlacemark(self, latitude, longitude, altitude = 0.0, description = " ", name = " ", range = 6000, tilt = 45, heading = 0):

        self.content += "<Placemark>\n"\
        "  <description>" + description + "</description>\n"\
        "  <name>" + name + "</name>\n"\
        "  <styleUrl>#normalPlaceMarker</styleUrl>\n <LookAt>\n"\
        "    <longitude>" + str(longitude) + "</longitude>\n"\
        "    <latitude>" + str(latitude) + "</latitude>\n"\
        "    <range>" + str(range) + "</range>\n"\
        "    <tilt>" + str(tilt) + "</tilt>\n"\
        "    <heading>" + str(heading) + "</heading>\n"\
        "  </LookAt>\n"\
        "  <visibility>1</visibility>\n"\
        "   <Point>\n"\
        "    <extrude>1</extrude>\n"\
        "    <altitudeMode>relativeToGround</altitudeMode>\n"\
        "    <coordinates>" + str(longitude) + "," + str(latitude) +", " +  str(altitude) + "</coordinates>\n"\
        "   </Point>\n"\
        " </Placemark>\n"