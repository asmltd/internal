app.controller('user_details', function($rootScope, $scope, $state, $http, $interval,$window) {
    $scope.Details = [];

    $scope.loadUser = function() {
        $http.get('api/employe_details/', '')
            .success(function(data) {
                $scope.Details = data;
            })
    }

    $scope.loadUser();

    $scope.del_user = function(id) {
        $http({
                method: 'DELETE',
                url: 'api/employe_details/' + id + "/",
            })
            .success(function(data) {
                $scope.loadUser();
                bootbox.alert("Deleted");
            });
    }
});