angular.module('youmuApp', ['mm.foundation']);

var topBarCtrl = function ($scope) {
	$scope.logoUrl = "/static/img/youmu-seal.jpg";
};

var videoStoreCtrl = function ($scope) {
	$scope.logoUrl = "/static/img/youmu-circle.png";
	$scope.authorUrl = "/static/img/youmu-seal.jpg";
	$scope.videos = [
		{
			name: "测试视频1",
			visits: 132,
			logoUrl: "http://placehold.it/1000x1000&text=Thumbnail",
			videoUrl: "http://localhost:5000/videos/1",
		},
		{
			name: "测试视频2",
			visits: 231,
			logoUrl: "http://placehold.it/1000x1000&text=Thumbnail",
			videoUrl: "http://localhost:5000/videos/2",
		},
		{
			name: "测试视频3",
			visits: 312,
			logoUrl: "http://placehold.it/1000x1000&text=Thumbnail",
			videoUrl: "",
		},
		{
			name: "测试视频4",
			visits: 213,
			logoUrl: "http://placehold.it/1000x1000&text=Thumbnail",
			videoUrl: "",
		},
		{
			name: "测试视频5",
			visits: 321,
			logoUrl: "http://placehold.it/1000x1000&text=Thumbnail",
			videoUrl: "",
		},
	];
};
