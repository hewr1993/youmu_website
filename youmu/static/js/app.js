angular.module('youmuApp', ['mm.foundation'])
	.service('UserService', function() {
		var id = "", name = "";
		return {
			getID: function() {
				return id;
			},
			getName: function() {
				return name;
			},
			setUser: function(_id, _name) {
				id = _id;
				name = _name;
			},
			isLogin: function() {
				return id.length > 0;
			},
			logout: function() {
				id = "";
				name = "";
			}
		};
	});

var alertInfo = function(info) {
	$("#alertInfo").html(info);
	$("#alertModal").foundation("reveal", "open");
}

var topBarCtrl = function ($scope, $rootScope, $http, UserService) {
	$scope.logoUrl = "/static/img/youmu-seal.jpg";
	$scope.isLogin = false;
	$scope.checkLogin = function() {
		$http.get("/api/user/_me").success(
			function(data, status){
				if (data.hasOwnProperty("id")) {
					UserService.setUser(data.id, data.name);
					$scope.user_id = UserService.getID();
					$scope.username = UserService.getName();
					$scope.logout = function() {
						$http.post("/api/user/_logout").success(		
							function(data, status) {
								UserService.logout();
								$scope.checkLogin();
							}
						).error(
							function(data, status) {
								alertInfo("登出失败");
							}
						);	
					};
					$rootScope.$emit('logined');
				} else {
					$('#loginForm').on('valid.fndtn.abide', function() {
						$("#loginButton").attr("disabled", "disabled");
						var user_id = $("#user_id").val();
						var password = $("#password").val();
						$http.post("/api/user/_login", 
							{
								"username": user_id,
								"password": password
							}).success(
								function(data, status) {
									$("#loginButton").removeAttr("disabled");
									if (data.state === "ok") {
										$('#loginModal').foundation('reveal', 'close');
										$scope.checkLogin();
									} else {
										$("#loginFormFieldset").append(
											'<div data-alert class="alert-box alert radius">'+
												'用户名或密码错误'+
												'<a href="#" class="close">&times;</a>'+
											'</div>'
										).foundation();
									}
								}
							).error(
								function(data, status) {
									$("#loginButton").removeAttr("disabled");
									$("#loginFormFieldset").append(
										'<div data-alert class="alert-box warning radius">'+
											'服务器繁忙，请稍候再试'+
											'<a href="#" class="close">&times;</a>'+
										'</div>'
									).foundation();
								}
							);
					});
				}
				$scope.isLogin = UserService.isLogin();
			}
		).error(
			function(data, status){
				alertInfo("获取用户信息出错");
			}
		);
	};
	$scope.checkLogin();
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
};

var personalCenterCtrl = function ($scope, $rootScope, $http, UserService) {
	$rootScope.$on('logined', function() {
		$scope.username = UserService.getName();
		$scope.user_id = UserService.getID();
		$scope.get_videos = function(){
			//$http.get("/api/videolist/").success(
			$http.get("/api/videolist/owner/" + $scope.user_id).success(
				function(data, status) {
					$scope.videos = [];
					for (var i = 0; i < data.length; ++i) {
						item = data[i];
						item.videoUrl = "/videos/" + item.video_id;
						$scope.videos.push(item);
					};
				}
			).error(
				function(data, status) {
					alertInfo("获取上传视频列表失败");
				}
			);
		};
		$scope.get_videos();
	});
};
