angular.module('homeAPIsApp', [])
    .controller('temperatureController', function($http) {

        var temperatureList = this;

        temperatureList.temperatures = [];

        $http.get("http://homeapis.mybluemix.net/api/temperatures")
            .then(function(response) {

                var keepGoing = true;
                var count = 0

                angular.forEach(response.data.reverse(), function(temperature) {
                    count++
                    if (keepGoing) {

                        if (count >= 5) {
                            keepGoing = false;
                        }

                        temperatureList.temperatures.push({
                            id: temperature.id,
                            timestamp: new Date(temperature.timestamp).toUTCString().substring(0, 26),
                            currentValue: temperature.currentValue
                        });

                    }
                });
            });

    }).controller('humidityController', function($http) {
       
        var humidityList = this;
       
        humidityList.humidities = [];
       
        $http.get("http://homeapis.mybluemix.net/api/humidities").then(function(response) {

            var keepGoing = true;
            var count = 0

            angular.forEach(response.data.reverse(), function(humidity) {
                count++
                if (keepGoing) {

                    if (count >= 5) {
                        keepGoing = false;
                    }

                    humidityList.humidities.push({
                        id: humidity.id,
                        timestamp: new Date(humidity.timestamp).toUTCString().substring(0, 26),
                        currentValue: humidity.currentValue
                    });

                }
            });

        });
    });