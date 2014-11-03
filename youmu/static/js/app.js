angular.module('youmuApp', ['mm.foundation']);

var topBarCtrl = function ($scope) {
	$scope.logoUrl = "/static/img/youmu-seal.jpg";
};

var videoStoreCtrl = function ($scope, $http) {
	$scope.logoUrl = "/static/img/youmu-circle.png";
	$scope.authorUrl = "/static/img/youmu-seal.jpg";
	$http.get("/api/video/").success(function(data, status) {
		$scope.videos = [];
		for (var i = 0; i < data.length; ++i) {
			item = JSON.parse(data[i]);
			item.videoUrl = "/videos/" + item.video_id;
			$scope.videos.push(item);
		};
	});
};

var videoDataCtrl = function ($scope) {
	$scope.likeVideo = function() {
		alert("like");
	};
}
