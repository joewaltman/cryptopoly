pragma solidity ^0.4.0;

contract PropertyManagement{
    struct Property {
        string name;
        string latitude;
        string longitude;
        string venue_id;
        uint cost;
    }

    Property[] public properties;

    mapping(uint => address) public propertyToOwner;
    mapping(string => uint) private venueIdToProperty;
    mapping (address => uint) ownerPropertyCount;


    function buyProperty(string _name, string _latitude, string _longitude, string _venueId) public returns (uint){
        if(checkAvailability(_venueId)){
            if(isPropertyOwned(_venueId)){
                return uint(0);
            }
            else{
                propertyToOwner[venueIdToProperty[_venueId] - 1] = msg.sender;
                return uint(2);
            }
        }
        else{
            uint nextItem = properties.push(Property(_name, _latitude, _longitude, _venueId, 0));
            propertyToOwner[nextItem - 1] = msg.sender;
            venueIdToProperty[_venueId] = nextItem;
            ownerPropertyCount[msg.sender]++;
            return 1;
        }

    }

    function checkAvailability(string _venueId) public returns (bool){
        if(venueIdToProperty[_venueId] == 0){
            return false;
        }
        else{
            return true;
        }
    }

    function getOwnerDetails(string _venueId) public returns (address) {
        if(checkAvailability(_venueId)){
            return propertyToOwner[venueIdToProperty[_venueId]];
        }
    }

    function addProperty(string _name, string _latitude, string _longitude, string _venueId) public {
        if(checkAvailability(_venueId)){
            properties[venueIdToProperty[_venueId] - 1].cost++;
        }
        else{
            uint nextItem = properties.push(Property(_name, _latitude, _longitude, _venueId, 0));
            venueIdToProperty[_venueId] = nextItem;
        }
    }

    function getPropertyByVenue(string _venueId) public returns (uint) {
        if(checkAvailability(_venueId)){
            return venueIdToProperty[_venueId] - 1;
        }
    }

    function isPropertyOwned(string _venueId) public returns (bool) {
        if(!checkAvailability(_venueId)){
            return false;
        }
        else{
            if(propertyToOwner[venueIdToProperty[_venueId] - 1] == 0){
                return false;
            }
            else{
                return true;
            }
        }
    }
}