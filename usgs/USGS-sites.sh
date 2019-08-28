curl -s "https://waterservices.usgs.gov/nwis/iv/?format=rdb&stateCd="$1"&parameterCd=00060,00065&siteType=ST&siteStatus=active" | grep "#    USGS" | awk '{print $3}'
