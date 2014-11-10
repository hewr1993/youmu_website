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

var personCtrl = function ($scope, $rootScope, $http, UserService) {
	$rootScope.$on('logined', function() {
	});

/*{var me;								//保存个人信息的
	var user_id = $("#user_id").val();	//当前要访问的是谁的页面
	$scope.is_me = false;				//判断是否访问的是自己的页面
	$scope.tab = 0;
	$http.get("/api/user/_me").success(
		function(data, status) {
			//alert($("#user_id").val() + " | " + data.id);
			me = data;
			if (user_id === data.id){
				$scope.is_me = true;
				//alert("is me");
			}
		}
	).error(
		function(data, status) {
			alert("获取个人信息失败");
		}
	);

	$scope.isSelected = function(checkTab){
		if ($scope.tab === checkTab)
			return true;
		else return false;
	};

	$scope.get_profile = function(){
		$scope.tab = 1;
		alert("获取当前用户信息");
		if ($scope.is_me){
			$scope.name = me.name;
		}
		else {
			$http.get("/api/user/" + user_id).success(
				function(data, status) {
					$scope.name = data.name;
				}
			).error(
				function(data, status) {
					alert("获取个人信息失败");
				}
			);
		}
	};

	$scope.get_videos = function(){
		$scope.tab = 2;
		alert("获取当前用户上传视频信息");
		$http.get("/api/videolist/owner/" + user_id).success(
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
				alert("失败了");
				$http.get("/api/video/").success(function(data, status) {		//用这行可查看大致效
					$scope.videos = [];
					for (var i = 0; i < data.length; ++i) {
						item = data[i];
						item.videoUrl = "/videos/" + item.video_id;
						$scope.videos.push(item);
					};
				});
			}
		);
	};

	$scope.get_audios = function(){
		$scope.tab = 3;
		alert("获取当前用户订阅音频信息");
	};

	$scope.get_notifications = function(){
		$scope.tab = 4;
		alert("获取通知");
		$scope.notifications = [
			{
				"is_comment": false,
				"content": "你已被屏蔽",
				"date": "2014/1/1",
			},
			{
				"is_comment": true,
				"content": "hwr12在5回复了你",
				"user_id": "hwr12",
				"comment_id": "1",
				"video_id": "5",		//111在
				"date": "2014/1/5",
			},
			{
				"is_comment": true,
				"content": "zxk12在1回复了你",
				"user_id": "zxk12",
				"comment_id": "1",
				"video_id": "1",		//111在
				"date": "2014/1/3",
			},
			{
				"is_comment": false,
				"content": "你已解除屏蔽",
				"date": "2014/1/4",
			},
		];
	};
}*/
};
