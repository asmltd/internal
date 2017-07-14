app.controller('user_details', function($rootScope, $scope, $state, $http, $interval) {
    $scope.Details = [];

    $scope.loadUser = function() {
        $http.get('/api/Sessions/', '')
            .success(function(data) {
                $scope.Details = data;
            })
    }

    $scope.loadUser();

    $scope.del_user = function(id) {
        $http({
                method: 'DELETE',
                url: '/api/Sessions/' + id + "/",
            })
            .success(function(data) {
                $scope.loadUser();
            });
    }
});