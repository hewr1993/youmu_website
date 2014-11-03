angular.module('youmuApp', ['mm.foundation']);

var topBarCtrl = function ($scope, $http) {
	$scope.logoUrl = "/static/img/youmu-seal.jpg";
	$scope.isLogin = true;
	$scope.login = function() {
		var username = $("#username").val();
		var passwd = $("#passwd").val();
		$http.post("/api/user/_login", 
			{
				"username": username,
				"password": passwd
			}).success(		
			function(data, status) {
				if (data.state == "ok"){
					alert(username);
					$http.get("/api/user/{username}").success(function(data, status)
					{
						//alert(data.state);					
					});
				}
			}
		);	
	};

	$scope.logout = function() {
		$http.get("/api/user/_logout").success(		
			function(data, status) {
				alert(data.state);
			}
		).error(
			function(data, status) {
				alert("登出失败");
			}
		);	
	};
};

var videoStoreCtrl = function ($scope, $http) {
	$scope.logoUrl = "/static/img/youmu-circle.png";
	$scope.authorUrl = "/static/img/youmu-seal.jpg";
	$http.get("/api/video/").success(function(data, status) {
		$scope.videos = [];
		for (var i = 0; i < data.length; ++i) {
			item = data[i];
			item.videoUrl = "/videos/" + item.video_id;
			$scope.videos.push(item);
		};
	});
};

var videoDataCtrl = function ($scope, $http) {
	$http.get("/api/video/" + $("#video_id").val()).success(function(data, status) {
		$scope.video = data;
	});
	$scope.likeVideo = function() {
		alert("like");
	};
}

var profileCtrl = function ($scope, $http) {
	var username = null;
	$http.get("/api/user/_me").success(
		function(data, status) {
			username = data.username;
			$scope.username = username;
		}
	).error(
		function(data, status) {
			alert("获取个人信息失败");
		}
	);
	
	$scope.save = function() {
		$http.put("/api/user/_me",
			{
				"username": $("#username").val(),
			}
		).success(
			function(data, status) {
				username = $("#username").val();
				alert("修改信息成功");
			}
		).error(
			function(data, status) {
				alert("修改信息失败");
			}
		);
	};

	$scope.reset = function() {
		$scope.username = username;
	};

};

