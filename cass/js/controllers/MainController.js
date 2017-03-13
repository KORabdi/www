app.controller('MainController', ['$scope','revlobot', function($scope,revlobot) {
	$scope.revlobot = revlobot.redemptions;
	revlobot.success(function(data) { 
	    $scope.revlobot = data;
	});
	$scope.redemptions = [ //prijaty dotaz
	    {
	        "reward_id": 333334,
	        "redemption_id": 1458481,
	        "created_at": "2016-12-11T20:02:29.298Z",
	        "refunded": false,
	        "completed": false,
	        "user_input": {
	          "song": "GMDqA3DkAEw"
	        },
	        "username": "lpebony"
	      },
	      {
	        "reward_id": 333334,
	        "redemption_id": 1456921,
	        "created_at": "2016-12-11T17:12:26.106Z",
	        "refunded": false,
	        "completed": true,
	        "user_input": {
	          "song": "UbQgXeY_zi4"
	        },
	        "username": "dark_lord3"
	      }
	];	
}]);



/*
app.controller('MainController', ['$scope', 'forecast', function($scope, forecast) {
  forecast.success(function(data) {
    $scope.fiveDay = data;
  });
}]);
*/