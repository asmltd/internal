app.controller('dashboard_box', function ($rootScope, $scope, $state, $interval,$http) {
$scope.Details = [];
$http.get('/Sessions/', '')
            .success(function (data) {
                $scope.Details = data;
            })
});

