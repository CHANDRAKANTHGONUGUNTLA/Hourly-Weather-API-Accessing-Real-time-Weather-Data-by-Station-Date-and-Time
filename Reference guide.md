
# Weather Data Format Guide

### Control Data Section
  - The beginning of each record provides information about the report including date, time, and station location information. Data fields will be in positions identified in the applicable data definition. Control data section is fixed length and is 60 characters long.

### Mandatory Data Section
  - The mandatory data section contains meteorological information on the basic elements such as winds, visibility, and temperature. These are the most commonly reported parameters and are available most of the time. The mandatory data section is fixed length and is 45 characters long.

### Additional Data Section
  - Variable length data are provided after the mandatory data. These additional data contain information of significance and/or which are received with varying degrees of frequency. Identifiers are used to note when data are present in the record. If all data fields in a group are missing, the entire group is usually not reported. If no groups are reported the section will be omitted. The additional data section is variable in length with a minimum of 0 characters and a maximum of 637 (634 characters plus a 3 character section identifier) characters. Note: Specific information (where applicable) pertaining to each variable group of data elements is provided in the data item definition.

### Remarks Data
  - The numeric and character (plain language) remarks are provided if they exist. The data will vary in length and are identified in the applicable data definition. The remarks section has a maximum length of 515 (512 characters plus a 3 character section identifier) characters. Element Quality Data Section - The element quality data section contains information on data that have been determined erroneous or suspect during quality control procedures. Also, some of the original data source codes and flags are stored here. This section is variable in length and contains 16 characters for each erroneous or suspect parameter. The section has a minimum length of 0 characters and a maximum length of 1587 (1584 plus a 3 character section identifier) characters.

### Missing Values
  - Missing values for any non-signed item are filled (i.e., 999). Missing values for any signed item are positive filled (i.e., +99999). Longitude and Latitude Coordinates - Longitudes will be reported with negative values representing longitudes west of 0 degrees, and latitudes will be negative south of the equator. Although the data field allows for values to a thousandth of a degree, the values are often only computed to the hundredth of a degree with a 0 entered in the thousandth position.

### WIND-OBSERVATION direction angle
  - The angle, measured in a clockwise direction, between true north and the direction from which the wind is blowing.
  - MIN: 001 MAX: 360 UNITS: Angular Degrees
  - SCALING FACTOR: 1
  - DOM: A general domain comprised of the numeric characters (0-9).
  - 999 = Missing. If type code (below) = V, then 999 indicates variable wind direction.

### WIND-OBSERVATION direction quality code
  - The code that denotes a quality status of a reported WIND-OBSERVATION direction angle.
  - DOM: A specific domain comprised of the characters in the ASCII character set.
  - 0 = Passed gross limits check
  - 1 = Passed all quality control checks
  - 2 = Suspect
  - 3 = Erroneous
  - 4 = Passed gross limits check, data originate from an NCEI data source
  - 5 = Passed all quality control checks, data originate from an NCEI data source
  - 6 = Suspect, data originate from an NCEI data source
  - 7 = Erroneous, data originate from an NCEI data source
  - 9 = Passed gross limits check if element is present

### WIND-OBSERVATION type code
  - The code that denotes the character of the WIND-OBSERVATION.
  - DOM: A specific domain comprised of the characters in the ASCII character set.
  - A = Abridged Beaufort
  - B = Beaufort
  - C = Calm
  - H = 5-Minute Average Speed
  - N = Normal
  - R = 60-Minute Average Speed
  - Q = Squall
  - T = 180 Minute Average Speed
  - V = Variable
  - 9 = Missing
  - NOTE: If a value of 9 appears with a wind speed of 0000, this indicates calm winds.

### WIND-OBSERVATION speed rate
  - The rate of horizontal travel of air past a fixed point.
  - MIN: 0000 MAX: 0900 UNITS: meters per second
  - SCALING FACTOR: 10
  - DOM: A general domain comprised of the numeric characters (0-9).
  - 9999 = Missing.

### WIND-OBSERVATION speed quality code
  - The code that denotes a quality status of a reported WIND-OBSERVATION speed rate.
  - DOM: A specific domain comprised of the characters in the ASCII character set.
  - 0 = Passed gross limits check
  - 1 = Passed all quality control checks
  - 2 = Suspect
  - 3 = Erroneous
  - 4 = Passed gross limits check, data originate from an NCEI data source
  - 5 = Passed all quality control checks, data originate from an NCEI data source
  - 6 = Suspect, data originate from an NCEI data source
  - 7 = Erroneous, data originate from an NCEI data source
  - 9 = Passed gross limits check if element is present

### SKY-CONDITION-OBSERVATION ceiling height dimension
- The height above ground level (AGL) of the lowest cloud or obscuring phenomena layer aloft with 5/8 or more summation total sky cover, which may be predominantly opaque, or the vertical visibility into a surface-based obstruction. Unlimited = 22000.
    - MIN: 00000 
    - MAX: 22000 
    - UNITS: Meters 
    - SCALING FACTOR: 1 
    - DOM: A general domain comprised of the numeric characters (0-9). 
    - 99999 = Missing.

### SKY-CONDITION-OBSERVATION ceiling quality code
- The code that denotes a quality status of a reported ceiling height dimension.
    - DOM: A specific domain comprised of the characters in the ASCII character set.
    - 0 = Passed gross limits check
    - 1 = Passed all quality control checks
    - 2 = Suspect
    - 3 = Erroneous
    - 4 = Passed gross limits check, data originate from an NCEI data source
    - 5 = Passed all quality control checks, data originate from an NCEI data source
    - 6 = Suspect, data originate from an NCEI data source
    - 7 = Erroneous, data originate from an NCEI data source
    - 9 = Passed gross limits check if element is present

### SKY-CONDITION-OBSERVATION ceiling determination code
- The code that denotes the method used to determine the ceiling.
    - DOM: A specific domain comprised of the characters in the ASCII character set.
    - A = Aircraft
    - B = Balloon
    - C = Statistically derived
    - D = Persistent cirriform ceiling (pre-1950 data)
    - E = Estimated
    - M = Measured
    - P = Precipitation ceiling (pre-1950 data)
    - R = Radar
    - S = ASOS augmented
    - U = Unknown ceiling (pre-1950 data)
    - V = Variable ceiling (pre-1950 data)
    - W = Obscured
    - 9 = Missing

### SKY-CONDITION-OBSERVATION CAVOK code
- The code that represents whether the 'Ceiling and Visibility Okay' (CAVOK) condition has been reported.
    - DOM: A specific domain comprised of the characters in the ASCII character set.
    - N = No
    - Y = Yes
    - 9 = Missing

### VISIBILITY-OBSERVATION distance dimension
- The horizontal distance at which an object can be seen and identified.
    - MIN: 000000 
    - MAX: 160000 
    - UNITS: Meters 
    - DOM: A general domain comprised of the numeric characters (0-9). 
    - Missing = 999999
    - NOTE: Values greater than 160000 are entered as 160000

### VISIBILITY-OBSERVATION distance quality code
- The code that denotes a quality status of a reported distance of a visibility observation.
    - DOM: A specific domain comprised of the characters in the ASCII character set.
    - 0 = Passed gross limits check
    - 1 = Passed all quality control checks
    - 2 = Suspect
    - 3 = Erroneous
    - 4 = Passed gross limits check, data originate from an NCEI data source
    - 5 = Passed all quality control checks, data originate from an NCEI data source
    - 6 = Suspect, data originate from an NCEI data source
    - 7 = Erroneous, data originate from an NCEI data source
    - 9 = Passed gross limits check if element is present

### VISIBILITY-OBSERVATION variability code
- The code that denotes whether or not the reported visibility is variable.
    - DOM: A specific domain comprised of the characters in the ASCII character set.
    - N = Not variable
    - V = Variable
    - 9 = Missing

### VISIBILITY-OBSERVATION quality variability code
- The code that denotes a quality status of a reported VISIBILITY-OBSERVATION variability code.
    - DOM: A specific domain comprised of the characters in the ASCII character set.
    - 0 = Passed gross limits check
    - 1 = Passed all quality control checks
    - 2 = Suspect
    - 3 = Erroneous
    - 4 = Passed gross limits check, data originate from an NCEI data source
    - 5 = Passed all quality control checks, data originate from an NCEI data source
    - 6 = Suspect, data originate from an NCEI data source
    - 7 = Erroneous, data originate from an NCEI data source
    - 9 = Passed gross limits check if element is present

### AIR-TEMPERATURE-OBSERVATION air temperature
- The temperature of the air.
    - MIN: -0932 
    - MAX: +0618 
    - UNITS: Degrees Celsius 
    - SCALING FACTOR: 10 
    - DOM: A general domain comprised of the numeric characters (0-9), a plus sign (+), and a minus sign (-). 
    - +9999 = Missing.

### AIR-TEMPERATURE-OBSERVATION air temperature quality code
- The code that denotes a quality status of an AIR-TEMPERATURE-OBSERVATION.
    - DOM: A specific domain comprised of the characters in the ASCII character set.
    - 0 = Passed gross limits check
    - 1 = Passed all quality control checks
    - 2 = Suspect
    - 3 = Erroneous
    - 4 = Passed gross limits check, data originate from an NCEI data source
    - 5 = Passed all quality control checks, data originate from an NCEI data source
    - 6 = Suspect, data originate from an NCEI data source
    - 7 = Erroneous, data originate from an NCEI data source
    - 9 = Passed gross limits check if element is present
    - A = Data value flagged as suspect, but accepted as a good value
    - C = Temperature and dew point received from Automated Weather Observing System (AWOS) are reported in whole degrees Celsius. Automated QC flags these values, but they are accepted as valid.
    - I = Data value not originally in data, but inserted by validator
    - M = Manual changes made to value based on information provided by NWS or FAA
    - P = Data value not originally flagged as suspect, but replaced by validator
    - R = Data value replaced with value computed by NCEI software
    - U = Data value replaced with edited value

### AIR-TEMPERATURE-OBSERVATION dew point temperature
- The temperature to which a given parcel of air must be cooled at constant pressure and water vapor content in order for saturation to occur.
    - MIN: -0982 
    - MAX: +0368 
    - UNITS: Degrees Celsius 
    - SCALING FACTOR: 10 
    - DOM: A general domain comprised of the numeric characters (0-9), a plus sign (+), and a minus sign (-). 
    - +9999 = Missing.

### AIR-TEMPERATURE-OBSERVATION dew point quality code
- The code that denotes a quality status of the reported dew point temperature.
    - DOM: A specific domain comprised of the characters in the ASCII character set.
    - 0 = Passed gross limits check
    - 1 = Passed all quality control checks
    - 2 = Suspect
    - 3 = Erroneous
    - 4 = Passed gross limits check, data originate from an NCEI data source
    - 5 = Passed all quality control checks, data originate from an NCEI data source
    - 6 = Suspect, data originate from an NCEI data source
    - 7 = Erroneous, data originate from an NCEI data source
    - 9 = Passed gross limits check if element is present
    - A = Data value flagged as suspect, but accepted as a good value
    - C = Temperature and dew point received from Automated Weather Observing System (AWOS) are reported in whole degrees Celsius. Automated QC flags these values, but they are accepted as valid.
    - I = Data value not originally in data, but inserted by validator
    - M = Manual changes made to value based on information provided by NWS or FAA
    - P = Data value not originally flagged as suspect, but replaced by validator
    - R = Data value replaced with value computed by NCEI software
    - U = Data value replaced with edited value

### ATMOSPHERIC-PRESSURE-OBSERVATION sea level pressure
- The air pressure relative to Mean Sea Level (MSL).
    - MIN: 08600 
    - MAX: 10900 
    - UNITS: Hectopascals 
    - SCALING FACTOR: 10 
    - DOM: A general domain comprised of the numeric characters (0-9). 
    - 99999 = Missing.

### ATMOSPHERIC-PRESSURE-OBSERVATION sea level pressure quality code
- The code that denotes a quality status of the sea level pressure of an
ATMOSPHERIC-PRESSURE-OBSERVATION.
    - DOM: A specific domain comprised of the characters in the ASCII character set.
    - 0 = Passed gross limits check
    - 1 = Passed all quality control checks
    - 2 = Suspect
    - 3 = Erroneous
    - 4 = Passed gross limits check, data originate from an NCEI data source
    - 5 = Passed all quality control checks, data originate from an NCEI data source
    - 6 = Suspect, data originate from an NCEI data source
    - 7 = Erroneous, data originate from an NCEI data source
    - 9 = Passed gross limits check if element is present



