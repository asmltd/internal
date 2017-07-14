app.controller('dashboard_box', function ($rootScope, $scope, $state, $interval,$http) {
$scope.Details = [];
$http.get('api/employe_details/', '')
            .success(function (data) {
                $scope.Details = data;
            })
});

