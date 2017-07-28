app.controller('dashboard_box', function ($rootScope, $scope, $state, $interval,$http) {

    $scope.Details = [];

    $scope.loadUser = function() {
        $http.get('api/employe_details/', '')
            .success(function(data) {
                $scope.Details = data;
                console.log('data:' + $scope.Details)
            })
    }
$scope.loadUser();

})