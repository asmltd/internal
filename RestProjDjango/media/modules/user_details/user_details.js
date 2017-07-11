app.controller('user_details', function ($rootScope, $scope, $state,$http, $interval) {
$scope.Details = [];
$http.get('/Sessions/', '')
            .success(function (data) {
                $scope.Details = data;
            })
});

