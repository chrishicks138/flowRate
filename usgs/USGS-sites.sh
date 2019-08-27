curl -s "https://waterservices.usgs.gov/nwis/iv/?format=rdb&stateCd=id&parameterCd=00060,00065&siteType=ST&siteStatus=active" | grep "#    USGS" | awk '{print $3}'
