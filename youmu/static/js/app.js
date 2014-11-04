angular.module('youmuApp', ['mm.foundation']);

var topBarCtrl = function ($scope, $http) {
	$scope.logoUrl = "/static/img/youmu-seal.jpg";
	$scope.isLogin = true;
	$scope.login = function() {
		var user_id = $("#user_id").val();
		var password = $("#password").val();
		$http.post("/api/user/_login", 
			{
				"username": user_id,
				"password": password
			}).success(
				function(data, status) {
					if (data.state === "ok")
						alert("登录成功");
					else	
						alert("登录失败");
				}
			).error(
				function(data, status) {
					alert("post失败");
				}
			);
	};

	if ($scope.isLogin === true){
		$http.get("/api/user/_me").success(
			function(data, status){
				$scope.user_id = data.id;
				$scope.name = data.name;
				//alert(data.name);				
			}
		).error(
			function(data, status){
				alert("获取个人信息失败");
			}
		);
	}

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
	$http.post("/api/comment/" + $("#video_id").val()).success(function(data, status) {
		$scope.comments = data;
	});
	$scope.likeVideo = function() {
		alert("like");
	};
}

var personCtrl = function ($scope, $http) {
	$scope.user_id = "luz12";
}


var profileCtrl = function ($scope, $http) {
	$scope.user_id = $("#user_id").val();
	$http.get("/api/user/_me").success(
		function(data, status) {
			name = data.name;
			$scope.name = name;
			//alert(name + " | " + data.id);
		}
	).error(
		function(data, status) {
			alert("获取个人信息失败");
		}
	);
	
	$scope.save = function() {
		$http.put("/api/user/_me",
			{
				"name": $("#name").val(),
			}
		).success(
			function(data, status) {
				name = $("#name").val();
				alert("修改信息成功：" + name);
			}
		).error(
			function(data, status) {
				alert("修改信息失败");
			}
		);
	};

	$scope.reset = function() {
		$scope.name = name;
	};

};


var myVideosCtrl = function ($scope, $http) {
	$http.get("/api/video/").success(function(data, status) {		//用这行可查看大致效果
	//$http.get("/api/videolist/owner/{id}").success(function(data, status) {		//这里id还不知道怎么获取
		$scope.videos = [];
		for (var i = 0; i < data.length; ++i) {
			item = data[i];
			item.videoUrl = "/videos/" + item.video_id;
			$scope.videos.push(item);
		};
	});
};


var myNotificationsCtrl = function ($scope, $http) {
	$scope.logoUrl = "/static/img/youmu-circle.png";
	$scope.authorUrl = "/static/img/youmu-seal.jpg";
	$http.get("/api/notification/").success(function(data, status) {
		$scope.notifications = [];
		for (var i = 0; i < data.length; ++i) {
			item = data[i];
			$scope.videos.push(item);
		};
	});

	$scope.get_notification = function(nid){
		$http.get("/api/notice/" + nid).error(		//尚不知返回的内容
			function(data, status){
				alert("获取通知失败");
		});
	};
};
