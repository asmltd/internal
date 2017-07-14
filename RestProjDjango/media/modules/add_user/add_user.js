app.controller('add_user_controller', function($rootScope, $scope, $state, $http, $interval) {

    $scope.user = {};
    // calling our submit function.
    $scope.addUser = function() {
        // Posting data to php file
        $http({
                method: 'POST',
                url: '/api/Sessions/',
                data: $scope.user, //forms user object
            })
            .success(function(data) {
                if (data.errors) {
                    // Showing errors.
                    $scope.errorName = data.errors.name;
                    $scope.errorUserName = data.errors.username;
                    $scope.errorEmail = data.errors.email;
                } else {
                    $scope.message = data.message;
                }
            });

    }
});