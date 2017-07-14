app.controller('dashboard_box', function ($rootScope, $scope, $state, $interval,$http) {
$scope.Details = [];
$http.get('/api/Sessions/', '')
            .success(function (data) {
                $scope.Details = data;
            })
});

