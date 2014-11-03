angular.module('youmuApp', ['mm.foundation']);

var topBarCtrl = function ($scope) {
	$scope.logoUrl = "/static/img/youmu-seal.jpg";
	$scope.login = function() {
		var username = $("#username").val();
		var passwd = $("#passwd").val();
		alert(username + " | " + passwd);
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
