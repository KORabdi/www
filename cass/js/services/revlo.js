app.factory('revlobot', ['$http', function($http) { 
  return $http({
	  method: 'GET',
	  url:'https://api.revlo.co/1/redemptions?page=1&refunded=false',
	  headers:{
		  'x-api-key' : 'YcFVQiXIwW0RBlNfYMuahA-uaCxQPyjUIWL4xHD0MI8'
	  }
  })
  .success(function(response) { 
	  return response.data; 
  })
  .error(function(err) { 
	  return err; 
  }); 
}]);

app.factory('revloPatch',['$http',function($http){
	var x = {};
	x.content = function(input,patch){
		$http.patch('https://api.revlo.co/1/redemptions/'+input,{"completed" : patch},{header:{'x-api-key' : 'YcFVQiXIwW0RBlNfYMuahA-uaCxQPyjUIWL4xHD0MI8'}})
	    .success(function(data) { 
	        return data; 
	      }) 
	      .error(function(err) { 
	        return err; 
	      });
	};
	return x;
}]);
/*
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "https://api.revlo.co/1/redemptions/1458481",
  "method": "PATCH",
  "headers": {
    "x-api-key": "0tgeppCMU0A7VSBzbLfLj9MPHoLeeuujaSVusOGWo_U",
    "accept": "application/json",
    "host": "api.revlo.co:443",
    "connection": "close",
    "cache-control": "no-cache",
    "postman-token": "dfce9da2-ddcd-d846-17f6-07dc5b736115"
  },
  "data": "{\"completed\": true}"
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
*/